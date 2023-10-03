from flask import Flask

# Iniciar aplicacion
app = Flask(__name__)

# Configuracion de la sesion
app.secret_key = "mysecretkey"
