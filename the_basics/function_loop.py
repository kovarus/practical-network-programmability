import requests

def get_routes(switchuser, switchpassword, url):
    myheaders = {'content-type': 'application/json'}
    payload = {
      "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show ip route",
        "output_format": "json"
      }
    }
    response = requests.post(url,
                             data=json.dumps(payload),
                             headers=myheaders,
                             auth=(switchuser, switchpassword)).json()
    return response

switchuser = "admin"
switchpassword = "!Passw0rd"

switches = ["http://192.168.49.10/ins", "http://192.168.49.11/ins"]

for switch in switches:
    print(get_routes(switchuser=switchuser, switchpassword=switchpassword, url=switch))
