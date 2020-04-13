class Switch():
    """

    Switch module
    

    Returns all the interfaces of the switch in dictionary format(interface name:interface object)

    :return: Returns all the interfaces(Fc and PortChannel) on the switch in dictionary format(interface name:interface object)
    :rtype: dict(name:Interface(Fc or PortChannel)
    :example:
        >>> allint = switch_obj.interfaces
        >>> print(allint)
        {'fc1/1': <mdslib.fc.Fc object at 0x10bd5da90>, 'fc1/2': <mdslib.fc.Fc object at 0x10bde4050>, 'fc1/3': <mdslib.fc.Fc object at 0x10bd5d650>,
         'fc1/4': <mdslib.fc.Fc object at 0x10bd5df90>, 'fc1/5': <mdslib.fc.Fc object at 0x10bd5d9d0>, .....
         'port-channel212': <mdslib.portchannel.PortChannel object at 0x10d88ee90>, 'port-channel213': <mdslib.portchannel.PortChannel object at 0x10d88eed0>,
         'port-channel214': <mdslib.portchannel.PortChannel object at 0x10d88ef50>}
        >>>
        
    :example:
        >>>
        >>> intcounters = int_obj.counters
        >>> print(intcounters.total_stats)
        {'rx_total_frames': 14970, 'tx_total_frames': 14831, 'rx_total_bytes': 2235488, 'tx_total_bytes': 1733508, 'rx_total_multicast': 0,
        'tx_total_multicast': 0, 'rx_total_broadcast': 0, 'tx_total_broadcast': 0, 'rx_total_unicast': 14970, 'tx_total_unicast': 14831,
        'rx_total_discard': 0, 'tx_total_discard': 0, 'rx_total_error': 0, 'tx_total_error': 0, 'rx_c_2_frames': 0, 'tx_c_2_frames': 0,
        'rx_c_2_bytes': 0, 'tx_c_2_bytes': 0, 'rx_c_2_discards': 0, 'rx_c_2_port_rjt_frames': 0, 'rx_c_3_frames': 14962, 'tx_c_3_frames': 14823,
        'rx_c_3_bytes': 2235072, 'tx_c_3_bytes': 1733092, 'rx_c_3_discards': 0, 'rx_c_f_frames': 8, 'tx_c_f_frames': 8, 'rx_c_f_bytes': 416,
        'tx_c_f_bytes': 416, 'rx_c_f_discards': 0}
        >>>

    """

   
