from pprint import pprint
from jnpr.junos import Device

with Device(host='34.208.13.114', user='pyez', password='Juniperpyez!') as dev:
    pprint(dev.facts)
