import json
import socket

import requests
from hexbytes import HexBytes
import time

from blockchain_client_service import BlockchainClientService

ENCLAVE_PORT = 5000
ENCLAVE_CID = 16

class EnclaveClient:

    def connect(self, endpoint):
        self.sock = socket.socket(socket.AF_VSOCK, socket.SOCK_STREAM)
        self.sock.connect(endpoint)


    def send_data(self, data):
        # Send data to a remote endpoint
        data = data.encode('utf-8')
        self.sock.sendall(data)


    def recv_data(self):
        # Receive data from a remote endpoint
        data = ''
        while len(data)<=0:
            data = self.sock.recv(2048)
            data = HexBytes(data)
            if not data:
                break
            return data
        

    def disconnect(self):
        # Close the client socket
        self.sock.close()  
        


def get_aws_session_token():
    # Get the AWS credential from EC2 instance metadata

    r = requests.get("http://169.254.169.254/latest/meta-data/iam/security-credentials/")
    instance_profile_name = r.text

    r = requests.get("http://169.254.169.254/latest/meta-data/iam/security-credentials/%s" % instance_profile_name)
    response = r.json()

    return response
   

def client_handler():
    client = EnclaveClient()
    criptech_blockchain = BlockchainClientService()
    endpoint = (ENCLAVE_CID, int(ENCLAVE_PORT))
    time.sleep(3)
    tx = criptech_blockchain.deposit_transaction()
    response = get_aws_session_token()
    data =  json.dumps({"credentials": {
        'access_key_id' : response['AccessKeyId'],
        'secret_access_key' : response['SecretAccessKey'],
        'token' :response['Token'] },
        "transaction": tx
        })

    client.connect(endpoint)
    client.send_data(data)
    signed_transaction_bytes = client.recv_data()

    signed_transaction = HexBytes(signed_transaction_bytes)
    transaction_hash_send = criptech_blockchain.send_signed_transaction(signed_transaction)
    print(f"Transaction sent: {transaction_hash_send.hex()}")

    client.disconnect()


def main():
    client_handler()


if __name__ == "__main__":
    main()
