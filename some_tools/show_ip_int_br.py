import requests
import json

"""
 
 I modified these!
 
"""
url='http://192.168.49.10/ins'
switchuser='admin'
switchpassword='!Passw0rd'

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show ip int br",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

# Adding a print!

print(response)