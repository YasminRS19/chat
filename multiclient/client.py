import threading
import socket

def recebendo(cliente):
    while True:
        try:
            mensagem = cliente.recv(2048).decode('utf-8')
            print(mensagem)
        except:
            print('Você está desconectado')
            print('Pressione a tecla "Enter" para sair')
            cliente.close()
            break

def enviando(cliente,nomedeusuario):
    while True:
        try:
            mensagem = input('\n')
            cliente.send(f'<{nomedeusuario}> {mensagem}'.encode('utf-8'))
        except:
            return
def main():
    
    cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    try:
        cliente.connect(('localhost', 7777))
    except:
        return print('Conexão não estabelecida')
    
    nomedeusuario = input('Usuario ')
    print('Você está conectado')
    
    recebe = threading.Thread(target=recebendo, args=[cliente])
    envia = threading.Thread(target=enviando, args=[cliente])
    
    recebe.start()
    envia.start()
    