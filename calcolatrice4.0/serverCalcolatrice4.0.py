import socket,json
from threading import Thread

SERVER_IP="127.0.0.1"
SERVER_PORT=5005
BUFFER_SIZE=1024


def ricevi_comandi(sock_service,addr_client):
    with sock_service as sock_client:
        while True:
            dati = sock_client.recv(BUFFER_SIZE).decode()
            if not dati:
                print("termine elaborazioni")
                break
            dati=json.loads(dati)
            primoNumero=dati['primoNumero']
            operazione=dati['operazione']
            secondoNumero=dati['secondoNumero']
            if operazione=='+':
                risultato=primoNumero+secondoNumero
            elif operazione=='-':
                risultato=primoNumero-secondoNumero
            elif operazione=='*':
                risultato=primoNumero*secondoNumero
            elif operazione=='/':
                if secondoNumero!=0:
                    risultato=primoNumero/secondoNumero
                else:
                    risultato="impossibile"
            elif operazione=='%':
                risultato=primoNumero%secondoNumero

            sock_client.sendall(str(risultato).encode())


def ricevi_connessioni(sock_listen):
    while True:
        sock_service,addr_client=sock_listen.accept()
        print("\nConnessione ricevuta da %s" % str(addr_client))
        print("creo un thread per servire le richieste")
        try:
            Thread(target=ricevi_comandi, args=(sock_service,addr_client)).start()
        except:
            print("il thread non si avvia")
            sock_listen.close()


def avvia_server(indirizzo,porta):
    try:
        sock_listen=socket.socket()
        sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        sock_listen.bind((indirizzo,porta))
        sock_listen.listen(5)
        print("server in attesa di connessioni")
        ricevi_connessioni(sock_listen)
    except socket.error as errore:
        print(f"errore: {errore}")

    ricevi_connessioni(sock_listen)


if __name__=='__main__':
    avvia_server(SERVER_IP,SERVER_PORT)