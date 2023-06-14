import hvac
import urllib3
import sys
import os

os.environ['VAULT_TOKEN'] = ''

urllib3.disable_warnings()

# Authentication
client = hvac.Client(
    url='',
    token=os.environ['VAULT_TOKEN'],
    verify=False,
)

# Reading a secret
read_response = client.secrets.kv.read_secret_version(path='/creds')

database = read_response['data']['data']['database']
login = read_response['data']['data']['login']
password = read_response['data']['data']['password']

print(database)
print(login)
print(password)