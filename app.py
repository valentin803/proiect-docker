# Importăm request pe lângă Flask și jsonify pentru a putea citi datele trimise din formular
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# RUTA 1: Pagina principală modificată să accepte și afișeze un formular text
# methods=['GET', 'POST'] înseamnă: 
# GET - când omul doar intră pe pagină (îi arătăm formularul)
# POST - când omul apasă pe butonul "Trimite" (citim ce a scris)
@app.route('/', methods=['GET', 'POST'])
def home():
    mediu = os.getenv('APP_ENV', 'unknown')
    mesaj_primit = ""

    # Dacă utilizatorul a completat textul și a apăsat butonul:
    if request.method == 'POST':
        # Citim textul din căsuța care are numele (name) "text_utilizator"
        text_transmis = request.form.get('text_utilizator', '')
        mesaj_primit = f"<div style='color: green; margin-top: 10px;'><b>Serverul a primit textul:</b> {text_transmis}</div>"

    # Formularul HTML scris direct în cod (ușor de citit și testat)
    html_formular = f"""
    <html>
        <head><title>Formular Flask</title></head>
        <body style="font-family: Arial, sans-serif; margin: 40px;">
            <h2>Salut! Aplicatia ruleaza in mediul de: {mediu}!</h2>
            
            <fieldset style="padding: 20px; border-radius: 8px; border: 1px solid #ccc; max-width: 400px;">
                <legend><b>Adauga un text mai jos:</b></legend>
                <form method="POST" action="/">
                    <input type="text" name="text_utilizator" placeholder="Scrie ceva aici..." required style="padding: 8px; width: 250px;">
                    <button type="submit" style="padding: 8px 15px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;">Trimite</button>
                </form>
                {mesaj_primit}
            </fieldset>
            
            <p><a href="/about">Mergi la pagina About</a></p>
        </body>
    </html>
    """
    return html_formular

# RUTA 2: Endpoint-ul de Health Check
@app.route('/health')
def health():
    return jsonify(status="healthy")

# RUTA 3: Pagina Despre
@app.route('/about')
def about():
    return "Aceasta este pagina About a proiectului Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)