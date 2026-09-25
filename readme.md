# Prova 1 de Sistemas Distribuídos

## Problema da empresa

O cliente deve enviar um pedido ao servidor por meio de uma conexão TCP. O servidor recebe o pedido e devolve uma confirmação.

## Arquivos

- servidor.py: aguarda a conexão, recebe o pedido e envia uma confirmação.
- cliente.py: conecta-se ao servidor, envia o pedido e apresenta a resposta recebida.

## Resultado do cliente

Resposta recebida: Recebido pelo servidor: PEDIDO-42

## Resultado do servidor

Servidor aguardando conexao na porta 5005
Pedido recebido: PEDIDO-42

## Explicação

### 1. Qual programa iniciou a conexão?

O cliente iniciou a conexão.

### 2. Qual programa recebeu PEDIDO-42 e produziu a confirmação?

O servidor recebeu PEDIDO-42 e produziu a confirmação.

### 3. O que aconteceria com o cliente se o servidor estivesse desligado?

O cliente não conseguiria se conectar ao servidor e apresentaria um erro de conexão.
