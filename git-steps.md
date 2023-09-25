# Configuração da Máquina AWS e Instalação do Git

## Acessar a Máquina AWS

Para acessar a máquina AWS, siga os seguintes passos:

## Passo 1: Abra seu terminal.

1. Execute o seguinte comando para garantir que as permissões da chave de acesso estejam corretas (substitua "your-key.pem" pelo nome do seu arquivo de chave):

chmod 400 your-key.pem
​

2. Conecte-se à instância EC2 usando SSH (substitua "your-key.pem" pelo nome do seu arquivo de chave e "ec2-32-4342-94-3424.compute-1.amazonaws.com" pelo endereço IP ou nome de host da sua instância):

ssh -i "your-key.pem" ec2-user@ec2-32-4342-94-3424.compute-1.amazonaws.com
​

## Instalar o Git no Amazon Linux 2

Para instalar o Git no Amazon Linux 2, siga os seguintes passos:

1. Após se conectar com sucesso à instância EC2, execute o seguinte comando para instalar o Git usando o gerenciador de pacotes Yum:

sudo yum install git
​

## Clonar o Repositório

Agora que o Git está instalado, você pode clonar um repositório de seu interesse. Siga os seguintes passos:

1. Execute os seguintes comandos para clonar um repositório do GitHub (substitua o URL do repositório pelo que você deseja clonar):

git clone https://github.com/JailsonLucas/nitro-enclaves.git
cd nitro-enclaves
​

Lembre-se de personalizar as informações, como o nome do arquivo de chave e o URL do repositório do GitHub, conforme necessário.
