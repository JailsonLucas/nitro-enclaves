## Passo 1: Instale as ferramentas de desenvolvimento

sudo yum groupinstall "Development Tools"
​

## Passo 2: Instale as dependências do Python

sudo yum install libffi-devel bzip2-devel
​

## Passo 3: Baixe e extraia o Python 3.11.1

sudo wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz
sudo tar xzf Python-3.11.1.tgz
cd Python-3.11.1
​

## Passo 4: Configure e instale o Python 3.11.1

sudo ./configure --enable-optimizations
sudo make install
​

## Passo 5: Instale as dependências do cliente

cd client
pip3.11 install -r requirements.txt

sudo yum groupinstall "Development Tools"

sudo yum install libffi-devel bzip2-devel

sudo wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz
sudo tar xzf Python-3.11.1.tgz
cd Python-3.11.1

sudo ./configure --enable-optimizations
sudo make install

cd client
pip3.11 install -r requirements.txt
