# Criar uma Instância EC2 na AWS

## Passo 1: Escolher uma Imagem de Máquina Virtual

- Abra o Console da AWS.
- Clique em "EC2" no painel de serviços.
- Na guia "Launch Instance", clique em "Launch Instance".

### Subpasso 1.1: Selecionar uma Imagem de Máquina Virtual

- Na página "Choose an Amazon Machine Image (AMI)", escolha "Amazon Linux 2" na lista de AMIs disponíveis.

## Passo 2: Escolher o Tipo de Instância

### Subpasso 2.1: Selecionar o Tipo de Instância

- Na página "Choose an Instance Type", selecione "m5.xlarge" como o tipo de instância.

## Passo 3: Configurar Detalhes Avançados

### Subpasso 3.1: Habilitar Nitro Enclave

- Na página "Configure Instance Details", role para baixo até a seção "Advanced Details".
- Marque a opção "Nitro Enclave" para habilitá-la.

## Passo 4: Revisar e Iniciar

- Clique em "Review and Launch" para revisar todas as configurações.

## Passo 5: Lançar a Instância

- Na página de revisão, clique em "Launch" para iniciar a instância EC2.

## Passo 6: Criar ou Selecionar um Par de Chaves

- Se você ainda não tiver um par de chaves, escolha "Create a new key pair" e siga as instruções para criar um novo par de chaves.
- Se já tiver um par de chaves, selecione-o na lista.

## Passo 7: Lançar a Instância

- Clique em "Launch Instances" novamente.

## Passo 8: Acessar sua Instância EC2

- Aguarde até que o status da instância seja "running".
- Anote o endereço IP público da instância para acessá-la remotamente.

Lembre-se de que as taxas de uso da instância podem ser aplicadas, portanto, certifique-se de encerrar a instância quando não estiver em uso para evitar custos adicionais.
