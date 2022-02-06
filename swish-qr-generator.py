import requests
import json
import argparse

base_url = 'https://mpc.getswish.net/qrg-swish'
endpoint = '/api/v1/prefilled'
headers = {'Content-type': 'application/json'}

request_body = '''
{
    "format": "png",
    "payee": {
        "value": "1230628701",
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
args = parser.parse_args()

client = args.client
amount = args.amount

body = json.loads(request_body)
body['message']['value'] = client
body['amount']['value'] = amount

r = requests.post(base_url + endpoint, json=body, headers=headers)

if r.status_code == 200:
    with open(client+'.png', 'wb') as out_file:
        out_file.write(r.content)
else:
    print (r)
