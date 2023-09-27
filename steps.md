### Etapas

1. Instale o Docker.

sudo yum install docker
sudo service docker start
sudo systemctl enable docker.service
​

2. Instale o Nitro CLI.

sudo amazon-linux-extras install aws-nitro-enclaves-cli -y
​

3. Instale as ferramentas de desenvolvimento do Nitro Enclaves.

sudo yum install aws-nitro-enclaves-cli-devel -y
​

4. Adicione seu usuário ao grupo `ne`.

sudo usermod -aG ne ec2-user
​

5. Adicione seu usuário ao grupo `docker`.

sudo usermod -aG docker ec2-user
​

6. Para que as alterações tenham efeito, saia da instância e reconecte-se a ela.
7. Verifique se o Nitro CLI foi instalado corretamente.

nitro-cli --version
​

8. Crie uma imagem do Docker para o servidor de amostra do Nitro Enclave.

sudo docker build -t nitro-enclave-sample-server -f Dockerfile.server .
​

9. Crie um arquivo de enclave (EIF) para o servidor de amostra do Nitro Enclave.

touch nitro-enclave-sample-server.eif
​

10. Construa o enclave usando o Nitro CLI.

sudo nitro-cli build-enclave --docker-uri nitro-enclave-sample-server:latest --output-file nitro-enclave-sample-server.eif
​

11. Alter o arquivo de configuração para o Nitro Enclaves Allocator.

sudo nano /etc/nitro_enclaves/allocator.yaml
​

12. Habilite o serviço Nitro Enclaves Allocator.

sudo systemctl enable --now nitro-enclaves-allocator.service
​

13. Execute o enclave usando o Nitro CLI.

sudo nitro-cli run-enclave --cpu-count 2 --memory 4320 --enclave-cid 16 --eif-path nitro-enclave-sample-server.eif --debug-mode

14. Conecte nos logs do Nitro Enclave.

nitro-cli console --enclave-id {enclave-id}
