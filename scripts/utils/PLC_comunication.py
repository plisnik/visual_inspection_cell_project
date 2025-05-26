from opcua import Client, ua


def write_value_bool(client: Client, node_id: str, value: bool) -> None:
    """
    Writes a boolean value to an OPC UA node.

    Parameters:
        client (Client): OPC UA client instance
        node_id (str): Node identifier string
        value (bool): Boolean value to write

    Returns:
        None
    """
    node = client.get_node(node_id)
    dv = ua.DataValue(ua.Variant(value, ua.VariantType.Boolean))
    node.set_value(dv)
    print(f"Wrote BOOL to {node_id}: {value}")


def write_value_int(client: Client, node_id: str, value: int) -> None:
    """
    Writes a 16-bit integer value to an OPC UA node.

    Parameters:
        client (Client): OPC UA client instance
        node_id (str): Node identifier string
        value (int): Integer value to write (16-bit)

    Returns:
        None
    """
    node = client.get_node(node_id)
    dv = ua.DataValue(ua.Variant(value, ua.VariantType.Int16))
    node.set_value(dv)
    print(f"Wrote INT to {node_id}: {value}")


def write_value_dint(client: Client, node_id: str, value: int) -> None:
    """
    Writes a 32-bit integer value to an OPC UA node.

    Parameters:
        client (Client): OPC UA client instance
        node_id (str): Node identifier string
        value (int): Integer value to write (32-bit)

    Returns:
        None
    """
    node = client.get_node(node_id)
    dv = ua.DataValue(ua.Variant(value, ua.VariantType.Int32))
    node.set_value(dv)
    print(f"Wrote (D)INT to {node_id}: {value}")


def read_value_bool(client: Client, node_id: str) -> bool:
    """
    Reads a boolean value from an OPC UA node.

    Parameters:
        client (Client): OPC UA client instance
        node_id (str): Node identifier string

    Returns:
        bool: Boolean value read from the node
    """
    node = client.get_node(node_id)
    return node.get_value()


def read_value_int(client: Client, node_id: str) -> int:
    """
    Reads an integer value from an OPC UA node.

    Parameters:
        client (Client): OPC UA client instance
        node_id (str): Node identifier string

    Returns:
        int: Integer value read from the node
    """
    node = client.get_node(node_id)
    return node.get_value()


def read_value_float(client: Client, node_id: str) -> float:
    """
    Reads a float value from an OPC UA node.

    Parameters:
        client (Client): OPC UA client instance
        node_id (str): Node identifier string

    Returns:
        float: Float value read from the node
    """
    node = client.get_node(node_id)
    return node.get_value()


def write_value_float(client: Client, node_id: str, value: float) -> None:
    """
    Writes a float value to an OPC UA node.

    Parameters:
        client (Client): OPC UA client instance
        node_id (str): Node identifier string
        value (float): Float value to write

    Returns:
        None
    """
    node = client.get_node(node_id)
    dv = ua.DataValue(ua.Variant(value, ua.VariantType.Float))
    node.set_value(dv)
    print(f"Wrote FLOAT to {node_id}: {value}")