import threading
import socket

clientes= []

def tratamento(cliente):
    while True:
        try:
            mensagem = cliente.recv(2048)
            broadcast(mensagem, cliente)
        except:
            removerCliente(cliente)
            break
        
def broadcast(mensagem,cliente):
    for x in clientes:
        if x != cliente:
            try:
                x.send(mensagem)
            except:
                removerCliente(x)
                
def removerCliente(cliente):
    clientes.remove(cliente)
    
def main():
    servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    try:
        servidor.bind(('localhost', 7777))
        servidor.listen()
    except:
        return print('O servidor não pode ser iniciado')
    
    while True:
        cliente, adrr = servidor.accept()
        clientes.append(cliente)
        
        thread = threading.Thread(target= tratamento, args=[cliente])
        thread.start()
        