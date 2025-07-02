from fastapi import FastAPI, HTTPException
from loguru import logger
from modules.calcul import compute_square
from pydantic import BaseModel

app = FastAPI()


class NumberInput(BaseModel):
    number: int


@app.get("/")
def read_root():
    return {"message": "API is running"}


@app.post("/square")
def square_number(input: NumberInput):
    try:
        result = compute_square(input.number)
        return {"result": result}
    except Exception as e:
        logger.error(f"Error in compute_square: {e}")
        raise HTTPException(status_code=400, detail="Invalid input")


@app.get("/health")
def health_check():
    return {"status": "ok"}
