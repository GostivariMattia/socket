import socket,json

SERVER_IP="127.0.0.1"
SERVER_PORT=5005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((SERVER_IP, SERVER_PORT))
    while True:
        print("list\n")
        print("get\n")
        print("set\n")
        print("put\n")
        print("close\n")
        comando=input("inserisci l'operazione che vuoi effettuare")
        if(comando=='list' or comando=='close'):
            parametri=''
        elif(comando=='get' or comando=='set'):
            nomestudente=input("inserisci il nome dello studente")
            parametri={'nomestudente':nomestudente}
        elif(comando=='put'):
            nomestudente=input("inserisci il nome dello studente")
            materia=input("inserisci la materia")
            voto=input(int("inserisci il voto"))
            ore=input(int("inserisci il numero di ore"))
            parametri={'nomestudente':nomestudente,
                       'materia':materia,
                       'voto':voto,
                       'ore':ore}
        else:
            print("comando non esistente")
        
            








            dati={'comando':comando,
                  'parametri':parametri}
            dati = json.dumps(dati)
            sock_service.sendall(dati.encode("UTF-8"))