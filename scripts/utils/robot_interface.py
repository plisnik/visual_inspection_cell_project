import rtde_control
import rtde_receive
import rtde_io
from opcua import Client, ua
import numpy as np
import time
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.robotiq_gripper_control import RobotiqGripper
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
            PLC_comunication.write_value_float(self.client,'ns=3;s="URO"."Reg 1".Floats.Register[0]', pose[0])
            PLC_comunication.write_value_float(self.client,'ns=3;s="URO"."Reg 1".Floats.Register[1]', pose[1])
            PLC_comunication.write_value_float(self.client,'ns=3;s="URO"."Reg 1".Floats.Register[2]', pose[2])
            PLC_comunication.write_value_float(self.client,'ns=3;s="URO"."Reg 1".Floats.Register[3]', pose[3])
            PLC_comunication.write_value_float(self.client,'ns=3;s="URO"."Reg 1".Floats.Register[4]', pose[4])
            PLC_comunication.write_value_float(self.client,'ns=3;s="URO"."Reg 1".Floats.Register[5]', pose[5])
            PLC_comunication.write_value_bool(self.client,'ns=3;s="GlobalDB"."Execute"', True)
            while True:
                value = PLC_comunication.read_value_int(self.client,'ns=3;s="FBMain_DB".Main')
                print(f"Read value from FBMain_DB.Main: {value}")
                if value == 10:
                    print("Value reached 10.")
                    break
                time.sleep(1)
            print("MoveL and Execute set.")
            return True

    def moveJ(self, joints, speed=0.5, acceleration=0.5):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            result = rtde_c.moveJ(joints, speed, acceleration)
            time.sleep(0.1)
            rtde_c.disconnect()
            return result
        elif self.mode == "plc_opcua":
            return

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
            return

    def freedriveMode(self):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            rtde_c.freedriveMode()
            status = rtde_c.getRobotStatus()
            time.sleep(0.1)
            rtde_c.disconnect()
            return status
        elif self.mode == "plc_opcua":
            return

    def endFreedriveMode(self):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            rtde_c.endFreedriveMode()
            status = rtde_c.getRobotStatus()
            time.sleep(0.1)
            rtde_c.disconnect()
            return status
        elif self.mode == "plc_opcua":
            return

    def setStandardDigitalOutput(self, output_id: int, bool: bool):
        if self.mode == "rtde":
            rtde_IO = rtde_io.RTDEIOInterface(self.ip)
            success = rtde_IO.setStandardDigitalOut(output_id, bool)
            time.sleep(0.1)
            rtde_IO.disconnect()
            return success
        elif self.mode == "plc_opcua":
            return
        
    def getStandardDigitalOutput(self, output_id: int):
        if self.mode == "rtde":
            rtde_r = rtde_receive.RTDEReceiveInterface(self.ip)
            state = rtde_r.getDigitalOutState(output_id)
            time.sleep(0.1)
            rtde_r.disconnect()
            return state
        elif self.mode == "plc_opcua":
            return
        
    def isConnected(self):
        if self.mode == "rtde":
            rtde_r = rtde_receive.RTDEReceiveInterface(self.ip)
            state = rtde_r.isConnected()
            time.sleep(0.1)
            rtde_r.disconnect()
            return state
        elif self.mode == "plc_opcua":
            return
        
    def getRobotStatus(self):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            status = rtde_c.getRobotStatus()
            time.sleep(0.1)
            rtde_c.disconnect()
            return status
        elif self.mode == "plc_opcua":
            return
        
    def gripper_activate(self):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            gripper = RobotiqGripper(rtde_c)
            gripper.activate()
            time.sleep(0.1)
            rtde_c.disconnect()
            return
        elif self.mode == "plc_opcua":
            return
        
    def gripper_set_speed(self, speed: int = 50):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            gripper = RobotiqGripper(rtde_c)
            gripper.set_speed(speed)
            time.sleep(0.1)
            rtde_c.disconnect()
            return
        elif self.mode == "plc_opcua":
            return
        
    def gripper_open(self):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            gripper = RobotiqGripper(rtde_c)
            gripper.open()
            time.sleep(0.1)
            rtde_c.disconnect()
            return
        elif self.mode == "plc_opcua":
            return
        
    def gripper_close(self):
        if self.mode == "rtde":
            rtde_c = rtde_control.RTDEControlInterface(self.ip)
            gripper = RobotiqGripper(rtde_c)
            gripper.close()
            time.sleep(0.1)
            rtde_c.disconnect()
            return
        elif self.mode == "plc_opcua":
            return