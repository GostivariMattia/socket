import json,socket

SERVER_IP= "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE =1024

#creazione del socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    #dati da inviare al server
    primoNumero=float(input("inserisci il primo numero"))
    operazione=input("inserisci l'operazione (+,-,*,/,%)")
    secondoNumero=float(input("inserisci il secondo numero"))
    messaggio={'primoNumero': primoNumero,
            'operazione':operazione,
            'secondoNumero':secondoNumero}
    messaggio=json.dumps(messaggio) #trasforma l'oggetto in una stringa
    s.sendto(messaggio.encode("UTF-8"),(SERVER_IP,SERVER_PORT))
    #ricezione dei dati
    data=s.recv(BUFFER_SIZE)
    print("Risultato: ",data.decode())
