from flask import Flask, render_template
from productos import productos_bp
from compras import compras_bp  # Importa el blueprint desde el archivo correcto

app = Flask(__name__)

app.register_blueprint(productos_bp)
app.register_blueprint(compras_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
