git clone https://github.com/aws/aws-nitro-enclaves-cli.git
cd aws-nitro-enclaves-cli
make vsock-proxy

cd vsock_proxy/service
sudo systemctl enable nitro-enclaves-vsock-proxy.service
