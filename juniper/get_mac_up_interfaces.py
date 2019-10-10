from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.op.phyport import PhyPortTable

with Device(host='34.208.13.114', user='pyez', password='Juniperpyez!', gather_facts=False) as dev:
    intf_status = PhyPortTable(dev)
    intf_status.get()
    for intf in intf_status:
        if intf.oper == 'up':
            print(f"Interface {intf.name} is up and has MAC address {intf.macaddr}")