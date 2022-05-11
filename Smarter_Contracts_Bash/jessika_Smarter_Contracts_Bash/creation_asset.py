#This code defines an asset creation process on the Algorand Blockchain. 
#It is configured to create Choice Coin, however, the asset_details may be altered.

from algosdk import account, encoding, mnemonic,algod
from algosdk.future.transaction import AssetConfigTxn
from algosdk.v2client import algod

#Configure your Algorand Client here. 
#This code was tested on the PureStake API.
algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#Initializes Client for node
headers = {"X-API-Key": algod_token }
algod_client = algod.AlgodClient(algod_token,algod_address,headers)
creator_address = "" #Put in main creator address here. This is the account that you want to be the manager of the asset.
creator_mnemonic = "" #Put in main creator mnemonic here.
creator_key = mnemonic.to_private_key(creator_mnemonic)
#Details of the asset creation transaction.
#Alter these details as you wish. 
#Keep the manager, reserve, freeze, and clawback address the same as these point back to the variable defined at the beginning.
asset_details = {
	"asset_name": "",
	"unit_name": "",
	"total": 100000000000,
	"decimals": 2,
	"default_frozen": False,
	"manager": creator_address,
	"reserve": creator_address,
	"freeze": creator_address,
	"clawback": creator_address,
	"url": ""#Add a url for your asset here,
}

#Creates the asset.
#To run on the Python Terminal, import the creator_address,creator_key,and the creator_mnemonic.
#Finally, import the create_asset function and run as specified (without any inputs). 
#Go to the algoexplorer link that is returned to get a validated transaction. Record the asset_id and any other details you want.
def create_asset():
	params = algod_client.suggested_params()
	transaction = AssetConfigTxn(creator_address, params, **asset_details)
	signature = transaction.sign(creator_key)
    #Signs the transaction with the sender's private key
	algod_client.send_transaction(signature)
	transaction_id = transaction.get_txid()
	transaction_id = str(transaction_id)
	print("Your transaction information is at https://testnet.algoexplorer.io/tx/" + transaction_id)

create_asset()
