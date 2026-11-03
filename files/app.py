from flask import Flask
import socket
app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from {socket.gethostname()} - deployed by Ansible\n"

@app.route("/health")
def health():
    return {"status": "ok"}
