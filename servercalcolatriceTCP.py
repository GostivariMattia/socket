import socket,json

SERVER_IP="127.0.0.1"
SERVER_PORT=5005
BUFFER_SIZE=1024

#creazione della socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_IP,SERVER_PORT))
    sock_server.listen()
    print(f"server in ascolto su {SERVER_IP}:{SERVER_PORT}")
    while True:
        sock_service, address_client = sock_server.accept()
        with sock_service as sock_client:
            while True:
                dati = sock_client.recv(BUFFER_SIZE).decode()
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
