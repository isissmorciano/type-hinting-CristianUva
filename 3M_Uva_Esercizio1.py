#Cristian Uva 3M
#Creare una funzione descrizione() con due parametri nome ed eta. La funzione restituisce una stringa formattata nel seguente modo: "nome ha eta anni." descrizione("Pippo",23)
import random
def descrizione(nome, eta):
    return "{} ha {} anni.".format(nome, eta)
print(descrizione("Pippo", 23))    
#Creare una funzione(?) numero_casuale() che restituisce un numero casuale tra 0 e 99. La funzione restituisce il numero generato numero_casuale()
def numero_casuale():
    return random.randint(0, 99)
print(numero_casuale())
#Creare una funzione descrizione_eta_casuale() con un parametro nome. L'eta e' calcolata in modo casuale La funzione restituisce una stringa formattata nel seguente modo: "nome ha eta anni." descrizione_eta_casuale("Pippo")
def descrizione_eta_casuale(nome):
    eta = random.randint(0, 99)
    return "{} ha {} anni.".format(nome, eta)
print(descrizione_eta_casuale("Pippo"))
#Creare una funzione(?) descrizione_casuale(). Il nome e' scelto in modo casuale da una lista di nomi interna alla fuzione. L'eta e' calcolata in modo casuale La funzione restituisce una stringa formattata nel seguente modo: "nome ha eta anni." descrizione_casuale()
def descrizione_casuale():
    nomi = ["Luca", "Simone", "Andrea", "Paolo", "Chiara"]
    nome = random.choice(nomi)
    eta = random.randint(0, 99)
    return "{} ha {} anni.".format(nome, eta)
print(descrizione_casuale())










