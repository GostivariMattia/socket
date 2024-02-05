import socket,json
from threading import Thread

SERVER_IP="127.0.0.1"
SERVER_PORT=5005
BUFFER_SIZE=1024

diz={   'Antonio Barbera': [   ['Matematica', 8, 1],
                           ['Italiano', 6, 1],
                           ['Inglese', 9.5, 0],
                           ['Storia', 8, 2],
                           ['Geografia', 8, 1]],
    'Giuseppe Gullo': [   ['Matematica', 9, 0],
                          ['Italiano', 7, 3],
                          ['Inglese', 7.5, 4],
                          ['Storia', 7.5, 4],
                          ['Geografia', 5, 7]],
    'Nicola Spina': [   ['Matematica', 7.5, 2],
                        ['Italiano', 6, 2],
                        ['Inglese', 4, 3],
                        ['Storia', 8.5, 2],
                        ['Geografia', 8, 2]]}

def trova_stud(diz,nomestudente):
    if nomestudente in diz:
        return True
    else:
        return False

def comm_list(diz):
    risposta='OK'
    valori=diz
    dati={'risposta':risposta,
          'valori':valori}
    return dati

def comm_get(diz,parametri):
    nomestudente=parametri['nomestudente']
    if(trova_stud(diz,nomestudente)):
        risposta='OK'
        valori=diz[nomestudente]
    else:
        risposta='KO'
        valori="studente inesistente"
    dati={'risposta':risposta,
          'valori':valori}
    return dati

def comm_set(diz):
    nomestudente=input("inserisci il nome dello studente")
    if(trova_stud(diz,nomestudente)):
        risposta='KO'
        valori='studente già inserito'
    else:
        diz[nomestudente]=[]
        risposta='OK'
        valori='studente inserito correttamente'
    dati={'risposta':risposta,
          'valori':valori}
    return dati


    







#creazione della socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_IP,SERVER_PORT))
    sock_server.listen()
    print(f"server in ascolto su {SERVER_IP}:{SERVER_PORT}")

    while True:
        sock_service, address_client = sock_server.accept()
        print(f"connessione ricevuta da {address_client}")

        with sock_service as sock_client:
            while True:
                dati = sock_client.recv(BUFFER_SIZE).decode()
                if not dati:
                    break
                dati=json.loads(dati)
                comando=dati['comando']
                parametri=dati['parametri']

                if(comando=='list'):
                    comm_list(diz)
                elif(comando=='get'):
                    comm_get(diz,parametri)
                elif(comando=='set'):
                    comm_set(parametri)
                elif(comando=='put'):
                    comm_put(parametri)
                else:
                    #chiusura del server
