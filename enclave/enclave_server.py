import argparse
import socket
import sys
import os

from blockchain_service import BlockchainService

ENCLAVE_PORT = 5000

class EnclaveServer:
    def __init__(self, conn_backlog=128):
        self.block_chain_service = BlockchainService()
        self.conn_backlog = conn_backlog

    def bind(self):
        # Bind and listen for connections on the specified port
        self.sock = socket.socket(socket.AF_VSOCK, socket.SOCK_STREAM)
        address = (socket.VMADDR_CID_ANY, ENCLAVE_PORT)

        try:
            self.sock.bind(address)
            self.sock.listen()
        except socket.error as e:
            print(f'Failed to bind: {e}')
            sys.exit(1)

    def recv_data(self):
        while True:
            try:
                (from_client, (remote_cid, remote_port)) = self.sock.accept()
                print(f'Connection from: {remote_cid} - {remote_port}')

                data = from_client.recv(4096).decode()

                signed_transaction = self.block_chain_service.sign_transaction(data)
                byte_data = bytes(signed_transaction.rawTransaction)

                self.send_data(from_client, byte_data)
                from_client.close()
            except socket.error as e:
                print(f'Socket error: {e}')
                break

    def send_data(self, client_socket, data):
        # Send data to a remote endpoint
        try:
            print(f'Sending data')
            client_socket.sendall(data)
        except socket.error as e:
            print(f'Error sending data: {e}')
        finally:
            client_socket.close()

def server_handler():
    server = EnclaveServer()
    server.bind()
    server.recv_data()

def main():
    server_handler()

if __name__ == '__main__':
    main()