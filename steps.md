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

install docker on ec2
sudo yum install docker
sudo service docker start
sudo systemctl enable docker.service

Install the Nitro CLI.

$ sudo amazon-linux-extras install aws-nitro-enclaves-cli -y
Install the Nitro Enclaves development tools needed to build enclave images. The development tools also includes some sample applications.

$ sudo yum install aws-nitro-enclaves-cli-devel -y
Add your user to the ne user group.

$ sudo usermod -aG ne ec2-user
Add your user to the docker user group.

$ sudo usermod -aG docker ec2-user
For the changes to take effect, log out of the instance and then reconnect to it.

Verify that the Nitro CLI installed correctly.

$ nitro-cli --version

sudo docker build -t nitro-enclave-sample-server -f Dockerfile.server .
touch nitro-enclave-sample-server.eif
sudo nitro-cli build-enclave --docker-uri nitro-enclave-sample-server:latest --output-file nitro-enclave-sample-server.eif

sudo nano /etc/nitro_enclaves/allocator.yaml
sudo systemctl enable --now nitro-enclaves-allocator.service

sudo nitro-cli run-enclave --cpu-count 2 --memory 4320 --enclave-cid 16 --eif-path nitro-enclave-sample-server.eif --debug-mode

nitro-cli console --enclave-id {enclave-id}

------ kms --------
create a rule for kms
create a IAM
attach IAM to instance

----- km service --------

docker build -t kms-server -f Dockerfile.kms.server .
docker create -p 6000:80 --name kms-server
docker run -dp 127.0.0.1:6000:6000 kms-server

---

systemctl enable nitro-enclaves-vsock-proxy.service

sudo nitro-cli run-enclave --config enclave-manifest.json

---
