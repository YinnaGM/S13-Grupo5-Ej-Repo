from flask import Flask
app = Flask (__name__)

@app.route("/")
def primera_ruta():
    return "Hola mundo"