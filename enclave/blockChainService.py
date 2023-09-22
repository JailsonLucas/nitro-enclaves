from web3 import Web3
import json
import boto3

INFURA_URL_KEY = 'https://sepolia.infura.io/v3/YOUR_KEY'
ENCRYPTED_KEY = b""
KEY_NAME = ''

class BlockChainService:
    def __init__(self):
        web3 = Web3(Web3.HTTPProvider(INFURA_URL_KEY))
        self.web3 = web3

    def getWeb3(self, web3):
        return web3
    
    def signTransaction(self, dataCredentialsAndTransaction):
        data = json.loads(dataCredentialsAndTransaction)
        credentials = data['credentials']
        transaction = data['transaction']
        decrypted = self.decryptKey(credentials)
        privateKey = (decrypted['Plaintext']).decode('utf-8')

        return self.web3.eth.account.sign_transaction(transaction, privateKey)

    def decryptKey(self,credentials):
        client = boto3.client(
            'kms',
            region_name = 'us-east-1',
            aws_access_key_id = credentials['access_key_id'],
            aws_secret_access_key = credentials['secret_access_key'],
            aws_session_token = credentials['token']
        )
        decrypted_data = client.decrypt(
            CiphertextBlob=ENCRYPTED_KEY,
            EncryptionContext={'KeyName': KEY_NAME}
        )
        return decrypted_data

