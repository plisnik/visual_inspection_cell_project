from opcua import Client, ua

def write_value_bool(client: Client, node_id: str, value: bool):
    node = client.get_node(node_id)
    dv = ua.DataValue(ua.Variant(value, ua.VariantType.Boolean))
    node.set_value(dv)
    print(f"Wrote BOOL to {node_id}: {value}")
 
def write_value_int(client: Client, node_id: str, value: int):
    node = client.get_node(node_id)
    dv = ua.DataValue(ua.Variant(value, ua.VariantType.Int16))
    node.set_value(dv)
    print(f"Wrote INT to {node_id}: {value}")

def write_value_dint(client: Client, node_id: str, value: int):
    node = client.get_node(node_id)
    dv = ua.DataValue(ua.Variant(value, ua.VariantType.Int32))
    node.set_value(dv)
    print(f"Wrote INT to {node_id}: {value}")    
 
def read_value_bool(client: Client, node_id: str) -> bool:
    node = client.get_node(node_id)
    return node.get_value()
 
def read_value_int(client: Client, node_id: str) -> int:
    node = client.get_node(node_id)
    return node.get_value()

def read_value_float(client: Client, node_id: str) -> float:
    node = client.get_node(node_id)
    return node.get_value()

def write_value_float(client: Client, node_id: str, value: float):
    node = client.get_node(node_id)
    dv = ua.DataValue(ua.Variant(value, ua.VariantType.Float))
    node.set_value(dv)
    print(f"Wrote FLOAT to {node_id}: {value}")