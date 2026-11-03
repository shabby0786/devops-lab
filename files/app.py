from flask import Flask
import socket
app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from {socket.gethostname()} - deployed by pipeline v2\n"

@app.route("/health")
def health():
    return {"status": "ok"}
