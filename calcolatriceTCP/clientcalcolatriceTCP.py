import socket,json

SERVER_IP="127.0.0.1"
SERVER_PORT=20009


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((SERVER_IP, SERVER_PORT))
    print(f"connesso a {SERVER_IP} {SERVER_PORT}")
    while True:
        primoNumero=float(input("inserisci il primo numero"))
        operazione=input("inserisci l'operazione (+,-,*,/,%)")
        secondoNumero=float(input("inserisci il secondo numero"))
        messaggio={'primoNumero': primoNumero,
                'operazione':operazione,
                'secondoNumero':secondoNumero}
        messaggio=json.dumps(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))
        data=sock_service.recv(1024)
        print('Received', data.decode())
        risp=input("fare un altra operazione? s=si n=no")
        if (risp=='n'):
            break

print("socket chiusa")
