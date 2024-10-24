#apertura semplice
#with open("./requirements.txt", "r") as file:
 #   contenuto = file.read()
#print(f"Il contenuto del file è:\n{contenuto}\n\nIl tipo della variabile è : {type(contenuto)}")
# type permette di dirci il tipo 

#apertura con readline
#with open("./requirements.txt", "r") as file:
   # contenuto_file = file.readlines()

#print(f"Il contenuto del file è:\n{contenuto_file}\n\nIl tipo della variabile è : {type(contenuto_file)}")

 #   contenuto_pulito = []
  #  for nome_libreria in contenuto_file:
 #       nome_libreria_pulito = nome_libreria.strip("\n")
   #     contenuto_pulito.append(nome_libreria_pulito)
  #  print(f"Il contenuto del file è:\n{contenuto_pulito}\n\nIl tipo della variabile è : {type(contenuto_pulito)}")

with open("./commedia.txt", "r", encoding="utf-8") as file:
    testo_commedia = file.read()
    
    
testo_commedia = testo_commedia.replace("\n", " ")
testo_commedia = testo_commedia.split()
#print(testo_commedia)

#print(f"Nel testo della divina commedia ci sono: {len(testo_commedia)} parole")
def cleaning_parole(parola):
    parola.replace(" ", "").replace(".", "").replace(",", "").replace(":", "").replace("'", "").strip
print(testo_commedia)