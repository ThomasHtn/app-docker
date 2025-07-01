import requests
import streamlit as st
from loguru import logger

st.title("Carré d'un entier")

num = st.number_input("Entrez un entier:", step=1, format="%d")
if st.button("Calculer le carré"):
    try:
        logger.info(f"Envoi de l'entier {num} à l'API")
        res = requests.post("http://localhost:9500/square", json={"number": int(num)})
        res.raise_for_status()
        result = res.json()["result"]
        st.success(f"Le carré de {int(num)} est {result}")
    except Exception as e:
        logger.error(f"Erreur lors de l'appel à l'API: {e}")
        st.error("Une erreur s'est produite")
