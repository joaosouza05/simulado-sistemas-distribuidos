import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect(("127.0.0.1", 5005))
    cliente.sendall("PEDIDO-42".encode("utf-8"))

    resposta = cliente.recv(1024).decode("utf-8")
    print("Resposta recebida:", resposta)
