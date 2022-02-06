import requests
import json
import argparse

base_url = 'https://mpc.getswish.net/qrg-swish'
endpoint = '/api/v1/prefilled'
headers = {'Content-type': 'application/json'}

parser = argparse.ArgumentParser("Generate Swish QR code for client and amount")
parser.add_argument('--client', required=True)
parser.add_argument('--amount', required=True)
args = parser.parse_args()

client = args.client
amount = args.amount

with open("swish.json") as fh:
    string = fh.read()
body = json.loads(string)
body['message']['value'] = client
body['amount']['value'] = amount

r = requests.post(base_url + endpoint, json=body, headers=headers)

if r.status_code == 200:
    with open(client+'.png', 'wb') as out_file:
        out_file.write(r.content)
else:
    print (r)
