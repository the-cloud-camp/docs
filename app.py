from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello Python Git Action - Nhoona TCC231021"