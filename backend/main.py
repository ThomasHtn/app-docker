from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from loguru import logger
from modules.calcul import compute_square

app = FastAPI()

class NumberInput(BaseModel):
    number: int

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API de carré"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/square")
def square_number(data: NumberInput):
    logger.info(f"Reçu: {data.number}")
    try:
        result = compute_square(data.number)
        return {"result": result}
    except Exception as e:
        logger.error(f"Erreur: {e}")
        raise HTTPException(status_code=400, detail=str(e))
