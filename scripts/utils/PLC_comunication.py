from opcua import Client, ua

def write_value_bool(client, node_id, value):
    node = client.get_node(node_id)
    dv = ua.DataValue(ua.Variant(value, ua.VariantType.Boolean))
    node.set_value(dv)
    print(f"Wrote BOOL to {node_id}: {value}")
 
def write_value_int(client, node_id, value):
    node = client.get_node(node_id)
    dv = ua.DataValue(ua.Variant(value, ua.VariantType.Int16))
    node.set_value(dv)
    print(f"Wrote INT to {node_id}: {value}")
 
def read_value_bool(client, node_id):
    node = client.get_node(node_id)
    return node.get_value()
 
def read_value_int(client, node_id):
    node = client.get_node(node_id)
    return node.get_value()

def read_value_float(client, node_id):
    node = client.get_node(node_id)
    return node.get_value()

def write_value_float(client, node_id, value):
    node = client.get_node(node_id)
    dv = ua.DataValue(ua.Variant(value, ua.VariantType.Float))
    node.set_value(dv)
    print(f"Wrote FLOAT to {node_id}: {value}")