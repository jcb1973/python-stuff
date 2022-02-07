import requests
import json
import argparse

base_url = 'https://mpc.getswish.net/qrg-swish'
endpoint = '/api/v1/prefilled'
headers = {'Content-type': 'application/json'}
wheellab_swish_number = "1230628701"

request_body = '''
{
    "format": "png",
    "payee": {
        "value": "wheellab-swish-number will be set here",
        "editable": "False"
    },
    "amount": {
      "value": "amount here supplied from command line",
      "editable": "False"
    },
    "message": {
      "value": "client name here supplied from command line",
      "editable": "False"
    },
    "size": "600"
}
'''

parser = argparse.ArgumentParser("Generate Swish QR code for client and amount")
parser.add_argument('--client', required=True)
parser.add_argument('--amount', required=True)
parser.add_argument('--dir', required=False, default="/tmp/")
args = parser.parse_args()

client = args.client
amount = args.amount

body = json.loads(request_body)
body['message']['value'] = client
body['amount']['value'] = amount
body['payee']['value'] = wheellab_swish_number

r = requests.post(base_url + endpoint, json=body, headers=headers)

if r.status_code == 200:
    with open(args.dir + client+'.png', 'wb') as out_file:
        out_file.write(r.content)
else:
    print (r)
