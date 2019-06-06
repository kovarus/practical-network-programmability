from pprint import pprint
from jnpr.junos import Device

with Device(host='34.208.13.114', user='pyez', password='Juniperpyez!', gather_facts=False) as dev:
    print(dev.cli("show interface terse", warning=False))
