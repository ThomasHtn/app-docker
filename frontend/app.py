import os

import requests
import streamlit as st
from loguru import logger

API_URL = os.getenv("API_URL", "http://backend:9500")

st.title("Calcul du carré d’un entier")

number = st.number_input("Entrez un entier", step=1)

if st.button("Calculer le carré"):
    try:
        url = f"{API_URL}/square"
        logger.info(f"Calling API URL: {url}")
        response = requests.post(url, json={"number": int(number)})
        if response.status_code == 200:
            result = response.json()["result"]
            st.success(f"Le carré de {number} est {result}")
        else:
            st.error(f"Erreur côté serveur: {response.status_code}")
            logger.error(f"Erreur API: {response.text}")
    except Exception as e:
        st.error("Connexion à l'API impossible")
        logger.exception(e)
