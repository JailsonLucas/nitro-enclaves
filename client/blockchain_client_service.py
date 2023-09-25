import os
import json
from web3 import Web3
from contract_abi import ABI
from dotenv import load_dotenv

load_dotenv()

INFURA_KEY = os.getenv("INFURA_KEY")
INFURA_URL_KEY = "https://sepolia.infura.io/v3/"+INFURA_KEY
SIGNER_ADDRESS = os.getenv("SIGNER_ADDRESS")
CLIENT_ADDRESS = os.getenv("CLIENT_ADDRESS")
ERC20_CONTRACT_ADDRESS = os.getenv("ERC20_CONTRACT_ADDRESS")

class BlockchainClientService:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(INFURA_URL_KEY))


    def get_ERC20_Contract(self):
        web3 = self.web3
        brl_contract = web3.eth.contract(address= ERC20_CONTRACT_ADDRESS, abi=ABI)
        return brl_contract
    

    def deposit_transaction(self):
        web3 = self.web3
        brl_contract = self.get_ERC20_Contract()

        deposit = brl_contract.functions.deposit(CLIENT_ADDRESS, 1000000000000000000)
        deposit_tx= deposit.build_transaction({ 'from': SIGNER_ADDRESS, 'nonce': web3.eth.get_transaction_count(SIGNER_ADDRESS), 'gas': 200000, 'gasPrice': web3.to_wei('400', 'gwei') })
        return deposit_tx
    

    def deposit(self):
        data = self.deposit_transaction()
        json_data = json.dumps(data)
        return json_data
    

    def send_signed_transaction(self,signed_transaction):
        transaction_hash=self.web3.eth.send_raw_transaction(signed_transaction)
        return transaction_hash



