# Socket

1) Implemente um servidor e um cliente em sua máquina, utilizando protocolo TCP na porta acima de 50000.
2) No exemplo dado as informações de IP e porta estão fixos: ‘localhost’ e porta 50007. Mudar para deixar essas informações fiquem parametrizadas solicitando
ao usuário que informe IP e porta.
3) Do lado do servidor parametrize a quantidade máxima de conexões simultâneas que vai aceitar.
4) Do lado do cliente solicite ao usuário informar que insira várias mensagens ( ex. de 3 a 5 palavras ou frases), ir adicionando em uma fila. Pode optar por alguma
das duas bibliotecas estudadas.
OU
Depois que terminar a fila de mensagens, conectar ao servidor e enviar essas mensagens ao servidor, seguindo a ordem da fila.
5) Do lado do servidor receber todas as mensagens do cliente e só retorna “Confirmado”, para confirmar que recebeu.
6) Do lado do cliente exibir essa última mensagem enviada pelo servidor e encerrar a conexão com o servidor.
