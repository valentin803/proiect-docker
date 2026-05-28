import os
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurăm baza de date (va crea un fișier 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definim tabelul pentru explicații
class Explanatie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nume_pagina = db.Column(db.String(50), unique=True, nullable=False)
    text = db.Column(db.String(200), nullable=False)

# Creăm baza de date la pornirea aplicației (doar o dată)
with app.app_context():
    db.create_all()
    # Adăugăm datele inițiale dacă nu există
    if not Explanatie.query.first():
        db.session.add(Explanatie(nume_pagina='health', text="Sistemul funcționează perfect!"))
        db.session.add(Explanatie(nume_pagina='about', text="Aceasta este pagina About a proiectului Docker, adusă din baza de date!"))
        db.session.commit()

# --- RUTELE TALE MODIFICATE ---

@app.route('/health')
def health():
    # Căutăm explicația în baza de date
    record = Explanatie.query.filter_by(nume_pagina='health').first()
    return jsonify(status="healthy", message=record.text if record else "Nicio explicație găsită")

@app.route('/about')
def about():
    record = Explanatie.query.filter_by(nume_pagina='about').first()
    text = record.text if record else "Pagina nu are conținut."
    return render_template('about.html', text_din_db=text)

# (Ruta ta de home rămâne la fel, dar acum ai baza de date conectată)
@app.route('/', methods=['GET', 'POST'])
def home():
    # ... restul codului tău de la home ...
    return "Pagina principală (Formular)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)