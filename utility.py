import json
from typing import Union


class DatabaseHandler:
    
    def __init__(self, filename: str = "database.json"):
        self.filename = filename
        self.db = self.read_database()
        
    def get_database(self):
        return self.db
        
    def save_database(self) -> None:
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.db, file)  # Corretto: salva self.db invece di self.database

    def add_user_to_database(
        self,
        nome_utente: str
    ) -> dict:
        self.db[nome_utente] = {}  # Corretto: usa self.db invece di self.database
        return self.db  # Corretto: restituisce self.db

    def delete_user_from_database(
        self,
        nome_utente: str
    ) -> Union[dict, str]:  # Corretto: aggiunto self come primo parametro
        
        messaggio = f"L'utente {nome_utente} non esiste"
        
        if nome_utente in self.db.keys():  # Corretto: usa self.db invece di database
            del self.db[nome_utente]
            messaggio = f"L'utente {nome_utente} è stato rimosso"
            
        return self.db, messaggio  # Corretto: restituisce self.db

    def read_database(self) -> dict:
        with open(self.filename, "r", encoding="utf-8") as file:
            database: dict = json.load(file)
        return database
