from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable

dev = Device(host='34.208.13.114', user='pyez', password='Juniperpyez!', gather_facts=False)
dev.open()

tbl = RouteTable(dev)
tbl.get()
print(tbl)
for item in tbl:
    print('protocol:', item.protocol)
    print('age:', item.age)
    print('via:', item.via)
    print()

dev.close()
