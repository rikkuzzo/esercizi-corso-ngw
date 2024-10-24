print("Ciao mondo")

#definizioni variabili
numero = 10
nome = "Alice"
nome_2 = 'Tommaso'
is_active = True 


a = b = c = 0
x, y, z = 1, 2, 3

#tipologia di variabili
#int 
#float
#stringa
#booleani

#tipizzazione dinamica (permessa ma non consigliata)
variabile = 10
variabile = "Pippo"

#operatori

somma = 5 + 3
sottrazione = 5 - 3
moltiplicazione = 5 * 3
divisione = 5 / 3

#operatori logici (confronto)
sono_uguali: bool = ("Mario" == "Giovanni") # = --> assegnazione, == --> confronto
sono_uguali_numeri: bool = (4 == 4)

#operatore diverso
sono_diversi: bool = ("Mario" != "Giovanni") 
sono_deversi_numeri: bool = (4 != 4)

#operatore minore maggiore
confronto_minore: bool = 2 < 3
confronto_minore_uguale: bool = 2 <= 3

#operatori AND, OR, NOT
risultato = True and False 
risultato_esempio_and: bool = (2 == 2) and (3 != 3) #--> false
risultato_esempio_or: bool = (2 == 2) or (3 != 3) #--> true
risultato_esempio_not: bool = not True # --> false

#stringa

saluto: str = 'Ciao'
nome: str = "Mario"
messaggio = saluto + nome 

print(messaggio) 

messaggio = saluto + " " + nome 

print(messaggio)

#f-string 
messaggio_senza_f_string = "oggi è il compleanno di " + nome + "ti faccio tanti" + saluto
messaggio_con_f_string: str = f"oggi è il compleanno di {nome}, ti faccio tanti {saluto}"

#slicing 
testo: str = "Programmazione"
parte_iniziale: str = testo[0:7]
parte_finale: str = testo[7:14]

parte_iniziale: str = testo[:7]
parte_finale: str = testo[7:]

testo = "ciao"
testo.upper() 

testo = "CIAO"
print(testo.lower())


#if
punteggio_test = 82
if punteggio_test < 60:
    print("insufficiente")
elif punteggio_test < 80:
        print("buono")
elif punteggio_test < 90:
    print("distinto") 
else: 
    print("ottimo")
        
        
#clicli for e while 
lista_di_elementi = [1, 2, 3, 4, 5]
for elemento in lista_di_elementi: 
    print(elemento)

somma = 0
while somma <= 100:
    somma = somma + 10
    print(somma)
    
    
#definizione e uso di funzioni

def somma(numero_1, numero_2):
    somma = numero_1 + numero_2
    return somma 

#importazione moduli e pacchetti
import numpy as np
lista_di_numeri = [1, 2, 3]

std = np.std_dev(lista_di_numeri)


from numpy import std_dev
std = std_dev(lista_di_numeri)

#lettura e scrittura di file
file = open('./requirements.txt')
