from web3 import Web3
import json
import requests
import math



# add your blockchain connection information
chain = input("What chain you want to query(eth or bsc)?: ")
bsc = 'https://speedy-nodes-nyc.moralis.io/88f9e10ecc7056e5ba53e173/' + chain + '/mainnet'   
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())


tokenAddress = web3.toChecksumAddress(input("Enter TokenAddress: "))

erc20balance = 'https://deep-index.moralis.io/api/v2/'+ tokenAddress + '/erc20?chain=' + chain



headers = {
  'x-api-key': 'YOUR MORALIS API KEY'
}

response = requests.request("GET", erc20balance, headers=headers)
 

resp = response.json()
#print(resp)

for i in resp:
    print(i['token_address'])
    print(i['balance'])
