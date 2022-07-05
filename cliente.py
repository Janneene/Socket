#Código cliente

import socket #importa biblioteca socket para podermos manipular sockets
import queue as queue #importa a biblioteca da fila para podermos usar uma

fila = queue.Queue() #cria um objeto fila que é da biblioteca fila e tem o método fila

x=0 #variável de auxílio para finalizar o while

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#cria objeto soquete da biblioteca soquete com metodo soquete com os parametros
#socket.AF_INET (IPv4) e socket.SOCK_STREAM (TCP)
HOST = input("Informe o IP que gostaria conectar: ")
#variável que recebe o ip do cliente, que no caso do trabalho será localhost
PORT = int(input("Informe a porta que gostaria de conectar: "))
#variável para receber a porta que o usuário vai digitar
qtdMsgs = int (input("Informe quantidade de mensagens que gostaria de mandar ao servidor: "))
#para saber quantas mensagens o usuário vai querer mandar
#abaixo é o while para preencher a fila com as mensagens do usuário
while x < qtdMsgs:
    msg = input(f"Informe a mensagem {x} que quer enviar: ")
    #recebe a mensagem do usuário
    fila.put(msg) #coloca a mensagem na fila
    x = x+1 #para incrementar a variável de auxilio para sair do loop
    
soquete.connect((HOST, PORT))
#tupla com o IP e porta especificado anteriormente para poder se conectar no servidor
print("Conectado ao server")
#abaixo é um laço de repetição para enquanto a fila não for vazia...
while not fila.empty():
    proximoItem = fila.get() #recebe o item da fila
    print("Mensagens que serão enviadas: ", proximoItem)
    #informa a mensagem que sera enviada ao server
    soquete.sendall(str.encode(proximoItem))
    #envia para o servidor através do método sendall a variável próximo item
    #próximo item vai ser encode para poder ser enviada
    data = soquete.recv(1024) #recebe informação do servidor em byte
    print ('Mensagem: ',data) #mostra a mensagem do servidor
    print('Mensagem ecoada e decodificada: ', data.decode()) #mostra ela decodificada

#ja fora do while, recebe do servidor o feedback - pra saber se recebeu tudo ou não  
feedback = soquete.recv(1024)
print(feedback)


soquete.close()
