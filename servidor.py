import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind(("127.0.0.1", 5005))
    servidor.listen(1)
    print("Servidor aguardando conexao na porta 5005", flush=True)

    conexao, endereco = servidor.accept()
    with conexao:
        pedido = conexao.recv(1024).decode("utf-8")
        print("Pedido recebido:", pedido, flush=True)

        resposta = "Recebido pelo servidor: " + pedido
        conexao.sendall(resposta.encode("utf-8"))
