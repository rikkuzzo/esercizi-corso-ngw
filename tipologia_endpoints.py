import json
from fastapi import FastAPI
from utility import DatabaseHandler

app = FastAPI()
db = DatabaseHandler(filename="database.json")

@app.get("/")
async def homepage() -> dict:
    return {"message": "Benvenuto"}

@app.get("/database")
async def get_database_info() -> dict:
    # Utilizza il metodo della classe DatabaseHandler per leggere il database
    return db.get_database()

@app.post("/database")
async def create_new_user(nome: str):
    # Aggiunge un nuovo utente utilizzando il metodo di DatabaseHandler
    database = db.add_user_to_database(nome)
    return {"message": "Utente creato!"}

@app.delete("/database")
async def delete_user(nome: str):
    # Rimuove un utente utilizzando il metodo di DatabaseHandler
    database, messaggio = db.delete_user_from_database(nome)
    return {"message": messaggio}
