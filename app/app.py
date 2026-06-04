import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Leemos la URL de la base de datos desde las variables de entorno del sistema
# Si no existe (por ejemplo, local fuera de docker), usa SQLite por defecto para no romper nada
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///fallback.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- MODELO ---
class RegistroNota(db.Model):
    __tablename__ = 'registros_notas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    nota1 = db.Column(db.Float, nullable=False)
    nota2 = db.Column(db.Float, nullable=False)
    nota3 = db.Column(db.Float, nullable=False)
    resultado = db.Column(db.String(50), nullable=False)

def evaluador(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    if promedio >= 6:
        return f"Aprobado (Promedio: {promedio:.2f})"
    else:
        return f"Reprobado (Promedio: {promedio:.2f})"

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = None
    if request.method == "POST":
        try:
            nombre = request.form["nombre"]
            n1 = float(request.form["nota1"])
            n2 = float(request.form["nota2"])
            n3 = float(request.form["nota3"])
            
            resultado = evaluador(n1, n2, n3)

            # Guardado silencioso en la DB externa
            nuevo_registro = RegistroNota(nombre=nombre, nota1=n1, nota2=n2, nota3=n3, resultado=resultado)
            db.session.add(nuevo_registro)
            db.session.commit()
            
        except ValueError:
            resultado = "Por favor, ingresa números válidos."

    # Ya no enviamos el historial al HTML para mantener la privacidad en la página
    return render_template("evaluador.html", resultado=resultado)   

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    # Escuchamos en todas las interfaces (0.0.0.0) para que Docker pueda mapear el puerto
    app.run(host="0.0.0.0", port=5000, debug=True)