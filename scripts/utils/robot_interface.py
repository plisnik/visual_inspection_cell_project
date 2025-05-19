import rtde_control
import rtde_receive
import rtde_io
from opcua import Client, ua
import numpy as np
import time
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import PLC_comunication

class RobotInterface:
    def __init__(self, ip_address: str, mode="rtde"):
        self.ip = ip_address
        self.mode = mode

        if self.mode not in ["rtde", "plc_opcua"]:
            raise ValueError(f"Neznámý mód ovládání robota: {mode}")

        if mode == "plc_opcua":
            # OPC UA setup
            client_str = "opc.tcp://" + self.ip
            self.client = Client(client_str)
            # self.client = Client("opc.tcp://192.168.0.1:4840")
            self.client.connect()
            print("Connected to robot.")

    def moveL(self, pose, speed=0.25, acceleration=0.25):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            result = rtde_c.moveL(pose, speed, acceleration)
            time.sleep(0.1)
            rtde_c.disconnect()
            return result
        elif self.mode == "plc_opcua":
            PLC_comunication.write_value_float(self.client,'ns=3;s="FB_DB".UserDataInput."Real".Register[0]', pose[0])
            PLC_comunication.write_value_float(self.client,'ns=3;s="FB_DB".UserDataInput."Real".Register[1]', pose[1])
            PLC_comunication.write_value_float(self.client,'ns=3;s="FB_DB".UserDataInput."Real".Register[2]', pose[2])
            PLC_comunication.write_value_float(self.client,'ns=3;s="FB_DB".UserDataInput."Real".Register[3]', pose[3])
            PLC_comunication.write_value_float(self.client,'ns=3;s="FB_DB".UserDataInput."Real".Register[4]', pose[4])
            PLC_comunication.write_value_float(self.client,'ns=3;s="FB_DB".UserDataInput."Real".Register[5]', pose[5])
            PLC_comunication.write_value_int(self.client,'ns=3;s="FB_DB"."FunctionID"', 1) #moveL
            PLC_comunication.write_value_bool(self.client,'ns=3;s="FB_DB"."Execute"', True)
            while True:
                value = PLC_comunication.read_value_int(self.client,'ns=3;s="FBMain_DB".Main')
                print(f"Read value from FBMain_DB.Main: {value}")
                if value == 10:
                    print("Value reached 10.")
                    break
                time.sleep(1)
            print("MoveL and Execute set.")
            return True

    def moveJ(self, pose, speed=0.25, acceleration=0.25):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            result = rtde_c.moveJ(pose, speed, acceleration)
            time.sleep(0.1)
            rtde_c.disconnect()
            return result
        elif self.mode == "plc_opcua":
            PLC_comunication.write_value_float(self.client,'ns=3;s="FB_DB".UserDataInput."Real".Register[0]', pose[0])
            PLC_comunication.write_value_float(self.client,'ns=3;s="FB_DB".UserDataInput."Real".Register[1]', pose[1])
            PLC_comunication.write_value_float(self.client,'ns=3;s="FB_DB".UserDataInput."Real".Register[2]', pose[2])
            PLC_comunication.write_value_float(self.client,'ns=3;s="FB_DB".UserDataInput."Real".Register[3]', pose[3])
            PLC_comunication.write_value_float(self.client,'ns=3;s="FB_DB".UserDataInput."Real".Register[4]', pose[4])
            PLC_comunication.write_value_float(self.client,'ns=3;s="FB_DB".UserDataInput."Real".Register[5]', pose[5])
            PLC_comunication.write_value_int(self.client,'ns=3;s="FB_DB"."FunctionID"', 2) # moveJ
            PLC_comunication.write_value_bool(self.client,'ns=3;s="FB_DB"."Execute"', True)
            while True:
                value = PLC_comunication.read_value_int(self.client,'ns=3;s="FBMain_DB".Main')
                print(f"Read value from FBMain_DB.Main: {value}")
                if value == 10:
                    print("Value reached 10.")
                    break
                time.sleep(1)
            print("MoveJ and Execute set.")
            return True

    def get_actual_tcp_pose(self):
        if self.mode == "rtde":
            rtde_r = rtde_receive.RTDEReceiveInterface(self.ip)
            pose = rtde_r.getActualTCPPose()
            time.sleep(0.1)
            rtde_r.disconnect()
            return pose
        elif self.mode == "plc_opcua":
            x = PLC_comunication.read_value_float(self.client,'ns=3;s="URI".TCP."TCP Position (X,Y,Z) [m]"[0]')
            y = PLC_comunication.read_value_float(self.client,'ns=3;s="URI".TCP."TCP Position (X,Y,Z) [m]"[1]')
            z = PLC_comunication.read_value_float(self.client,'ns=3;s="URI".TCP."TCP Position (X,Y,Z) [m]"[2]')
            rx = PLC_comunication.read_value_float(self.client,'ns=3;s="URI".TCP."TCP Position (RX,RY,RZ) [rad]"[0]')
            ry = PLC_comunication.read_value_float(self.client,'ns=3;s="URI".TCP."TCP Position (RX,RY,RZ) [rad]"[1]')
            rz = PLC_comunication.read_value_float(self.client,'ns=3;s="URI".TCP."TCP Position (RX,RY,RZ) [rad]"[2]')
            time.sleep(1)
            return np.array([x,y,z,rx,ry,rz])

    def get_actual_joints(self):
        if self.mode == "rtde":
            rtde_r = rtde_receive.RTDEReceiveInterface(self.ip)
            joints = rtde_r.getActualQ()
            time.sleep(0.1)
            rtde_r.disconnect()
            return joints
        elif self.mode == "plc_opcua":
            j1 = PLC_comunication.read_value_float(self.client,'ns=3;s="URI".Joints."Joint position [rad]"[0]')
            j2 = PLC_comunication.read_value_float(self.client,'ns=3;s="URI".Joints."Joint position [rad]"[1]')
            j3 = PLC_comunication.read_value_float(self.client,'ns=3;s="URI".Joints."Joint position [rad]"[2]')
            j4 = PLC_comunication.read_value_float(self.client,'ns=3;s="URI".Joints."Joint position [rad]"[3]')
            j5 = PLC_comunication.read_value_float(self.client,'ns=3;s="URI".Joints."Joint position [rad]"[4]')
            j6 = PLC_comunication.read_value_float(self.client,'ns=3;s="URI".Joints."Joint position [rad]"[5]')
            return np.array([j1,j2,j3,j4,j5,j6])

    def freedriveMode(self):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            rtde_c.freedriveMode()
            status = rtde_c.getRobotStatus()
            time.sleep(0.1)
            rtde_c.disconnect()
            return status
        elif self.mode == "plc_opcua":
            PLC_comunication.write_value_int(self.client,'ns=3;s="FB_DB"."FunctionID"', 3) # freedrive enable
            PLC_comunication.write_value_bool(self.client,'ns=3;s="FB_DB"."Execute"', True)
            while True:
                value = PLC_comunication.read_value_int(self.client,'ns=3;s="FBMain_DB".Main')
                print(f"Read value from FBMain_DB.Main: {value}")
                if value == 10:
                    print("Value reached 10.")
                    break
                time.sleep(1)
            print("Freedrive enabled.")
            return 7

    def endFreedriveMode(self):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            rtde_c.endFreedriveMode()
            status = rtde_c.getRobotStatus()
            time.sleep(0.1)
            rtde_c.disconnect()
            return status
        elif self.mode == "plc_opcua":
            PLC_comunication.write_value_int(self.client,'ns=3;s="FB_DB"."FunctionID"', 4) # freedrive disable
            PLC_comunication.write_value_bool(self.client,'ns=3;s="FB_DB"."Execute"', True)
            while True:
                value = PLC_comunication.read_value_int(self.client,'ns=3;s="FBMain_DB".Main')
                print(f"Read value from FBMain_DB.Main: {value}")
                if value == 10:
                    print("Value reached 10.")
                    break
                time.sleep(1)
            print("Freedrive disabled.")
            return 1

    def setStandardDigitalOutput(self, output_id: int, bool: bool):
        if self.mode == "rtde":
            rtde_IO = rtde_io.RTDEIOInterface(self.ip)
            success = rtde_IO.setStandardDigitalOut(output_id, bool)
            time.sleep(0.1)
            rtde_IO.disconnect()
            return success
        elif self.mode == "plc_opcua":
            if output_id == 0:
                PLC_comunication.write_value_bool(self.client,'ns=3;s="FB_DB".UserDataInput."Bool".Register[0]', bool)
                PLC_comunication.write_value_int(self.client,'ns=3;s="FB_DB"."FunctionID"', 5) # set digital output 0
                PLC_comunication.write_value_bool(self.client,'ns=3;s="FB_DB"."Execute"', True)
                while True:
                    value = PLC_comunication.read_value_int(self.client,'ns=3;s="FBMain_DB".Main')
                    print(f"Read value from FBMain_DB.Main: {value}")
                    if value == 10:
                        print("Value reached 10.")
                        break
                    time.sleep(1)
                print("Digital output 0 set.")
                return True
            elif output_id == 1:
                PLC_comunication.write_value_bool(self.client,'ns=3;s="FB_DB".UserDataInput."Bool".Register[0]', bool)                
                PLC_comunication.write_value_int(self.client,'ns=3;s="FB_DB"."FunctionID"', 6) # set digital output 1
                PLC_comunication.write_value_bool(self.client,'ns=3;s="FB_DB"."Execute"', True)
                while True:
                    value = PLC_comunication.read_value_int(self.client,'ns=3;s="FBMain_DB".Main')
                    print(f"Read value from FBMain_DB.Main: {value}")
                    if value == 10:
                        print("Value reached 10.")
                        break
                    time.sleep(1)
                print("Digital output 1 set.")
            return
                
    def getStandardDigitalOutput(self, output_id: int):
        if self.mode == "rtde":
            rtde_r = rtde_receive.RTDEReceiveInterface(self.ip)
            state = rtde_r.getDigitalOutState(output_id)
            time.sleep(0.1)
            rtde_r.disconnect()
            return state
        elif self.mode == "plc_opcua":
            if output_id == 0:
                PLC_comunication.read_value_bool(self.client,'ns=3;s="FB_DB".UserDataOutput."Bool".Register[0]') # read digital output 0
                return True
            elif output_id == 1:
                PLC_comunication.read_value_bool(self.client,'ns=3;s="FB_DB".UserDataOutput."Bool".Register[1]') # read digital output 1
            return
        
    def isConnected(self):
        if self.mode == "rtde":
            rtde_r = rtde_receive.RTDEReceiveInterface(self.ip)
            state = rtde_r.isConnected()
            time.sleep(0.1)
            rtde_r.disconnect()
            return state
        elif self.mode == "plc_opcua":
            PLC_comunication.read_value_bool(self.client,'ns=3;s="URI".State.Robot."PW: Is power on"') # cita ci je robot pripojeny a zapnuty - bool - ak ano tak true
            return
        
    def getRobotStatus(self):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            status = rtde_c.getRobotStatus()
            time.sleep(0.1)
            rtde_c.disconnect()
            return status
        elif self.mode == "plc_opcua":
            PLC_comunication.read_value_bool(self.client,'"URI".State.Robot."Robot mode"') #  -  "URI".State.Robot."Robot mode"
            return
        
    # def gripper_activate(self): # netreba - gripper sa aktivuje na zaciatku programu
    #     if self.mode == "rtde":
    #         rtde_c = rtde_control.RTDEControlInterface(self.ip)
    #         gripper = RobotiqGripper(rtde_c)
    #         gripper.activate()
    #         time.sleep(0.1)
    #         rtde_c.disconnect()
    #         return
    #     elif self.mode == "plc_opcua":
    #         return
        
    # def gripper_set_speed(self, speed: int = 50):
    #     if self.mode == "rtde":
    #         rtde_c = rtde_control.RTDEControlInterface(self.ip)
    #         gripper = RobotiqGripper(rtde_c)
    #         gripper.set_speed(speed)
    #         time.sleep(0.1)
    #         rtde_c.disconnect()
    #         return
    #     elif self.mode == "plc_opcua":
    #         return
        


# Zatial nepouzivame


    def gripper_open(self):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            # gripper = RobotiqGripper(rtde_c)
            # gripper.open()
            time.sleep(0.1)
            rtde_c.disconnect()
            return
        elif self.mode == "plc_opcua":
            PLC_comunication.write_value_int(self.client,'ns=3;s="FB_DB"."FunctionID"', 7) # gripper open
            PLC_comunication.write_value_bool(self.client,'ns=3;s="FB_DB"."Execute"', True)
            while True:
                value = PLC_comunication.read_value_int(self.client,'ns=3;s="FBMain_DB".Main')
                print(f"Read value from FBMain_DB.Main: {value}")
                if value == 10:
                    print("Value reached 10.")
                    break
                time.sleep(1)
            print("MoveL and Execute set.")
            return
        
    def gripper_close(self):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            # gripper = RobotiqGripper(rtde_c)
            # gripper.close()
            time.sleep(0.1)
            rtde_c.disconnect()
            return
        elif self.mode == "plc_opcua":
            PLC_comunication.write_value_int(self.client,'ns=3;s="FB_DB"."FunctionID"', 8) # gripper close
            PLC_comunication.write_value_bool(self.client,'ns=3;s="FB_DB"."Execute"', True)
            while True:
                value = PLC_comunication.read_value_int(self.client,'ns=3;s="FBMain_DB".Main')
                print(f"Read value from FBMain_DB.Main: {value}")
                if value == 10:
                    print("Value reached 10.")
                    break
                time.sleep(1)
            print("MoveL and Execute set.")
            return