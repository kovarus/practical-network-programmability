"""
 NX-API-BOT
"""
import requests
import json
import getpass
import argparse

"""
Modify these please
"""


def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface',
                        required=True,
                        action='store',
                        help='Placeholder for help')

    args = parser.parse_args()
    return args

def make_request(url, payload, myheaders, switchuser, switchpassword):
    response = requests.post(url,
                             data=json.dumps(payload),
                             headers=myheaders,
                             auth=(switchuser, switchpassword)).json()

    return response

def main():
    args = getargs()
    switchpassword = getpass.getpass("What's your password dude: ")

    url = 'http://10.1.0.2/ins'
    switchuser = 'rpope'

    myheaders = {'content-type': 'application/json'}
    payload = {
        "ins_api": {
            "version": "1.2",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show ip route ",
            "output_format": "json"
        }
    }

    response = make_request(url, payload, myheaders, switchuser, switchpassword)
    for route in response["ins_api"]["outputs"]["output"]["body"]["TABLE_vrf"]["ROW_vrf"]["TABLE_addrf"]["ROW_addrf"][
        "TABLE_prefix"]["ROW_prefix"]:
        # print(route)
        # print(route["TABLE_path"]["ROW_path"].keys())
        if type(route["TABLE_path"]["ROW_path"]) == list:
            # print("hi!")
            pass
        else:
            # print(route)
            if "ifname" in route["TABLE_path"]["ROW_path"].keys():
                # print(route)
                if route["TABLE_path"]["ROW_path"]["ifname"] == args.interface:
                    print(route["TABLE_path"]["ROW_path"]["ifname"], route["ipprefix"])


# main()
if __name__ == "__main__":
    main()
# #

# print(json.dumps(response, indent=4))

# We just discovered this path is good so now lets do something interesting!
# print(json.dumps(response["ins_api"]["outputs"]["output"]["body"]["TABLE_vrf"]["ROW_vrf"]["TABLE_addrf"]["ROW_addrf"]["TABLE_prefix"]["ROW_prefix"]))
# ["TABLE_path"]["ROW_path"]["ifname"]

    # print(json.dumps(route, indent=4))


