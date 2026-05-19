# Importăm modulele necesare din librăria Flask și sistemul de operare (os)
# Flask - clasa principală pentru aplicația web
# jsonify - funcție care transformă dicționarele Python în format JSON
import os
from flask import Flask, jsonify

# Inițializăm aplicația Flask
app = Flask(__name__)

# RUTA 1: Pagina principală (Root endpoint)
@app.route('/')
def home():
    # CHALLENGE 2: Citim variabila de mediu APP_ENV setată în docker-compose.yml
    # Dacă nu este configurată în sistem, va folosi valoarea implicită 'unknown'
    mediu = os.getenv('APP_ENV', 'unknown')
    return f"Salut! Aplicatia ruleaza in mediul de: {mediu}!"

# RUTA 2: Endpoint-ul de Health Check (Verificare tehnică)
@app.route('/health')
def health():
    # Returnează un răspuns structurat JSON citit automat de unelte DevOps
    return jsonify(status="healthy")

# RUTA 3: Pagina Despre (Adăugată în Part 7)
@app.route('/about')
def about():
    return "Aceasta este pagina About a proiectului Docker!"

# Blocul principal care asigură pornirea serverului
if __name__ == '__main__':
    # host='0.0.0.0' - Obligatoriu în Docker! Permite aplicației să accepte conexiuni din afara ei (de la Nginx)
    # port=5000      - Portul intern pe care ascultă această aplicație în rețeaua Docker
    app.run(host='0.0.0.0', port=5000)