#Código Servidor

import socket #importando biblioteca do socket
soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soquete.bind(('localhost', 50000))
print("Escutando...")
soquete.listen(10) #aguarda conexão, máximo de conexões simultâneas são 10
conexao, endereco = soquete.accept()
print("Conectado por: ", endereco)



while True:
    data = conexao.recv(1024)
    print(f'Recebido {data} com sucesso!')

    #if data == 1:
    if not data:
       # print("Recebida todas as mensagens, fechando conexão")
        feedback = "Recebida todas as mensagens".encode()
        print(feedback)
        feedback = conexao.recv(1024)
        conexao.sendall(feedback)
        conexao.close()
        break;
    conexao.sendall(data)


    
