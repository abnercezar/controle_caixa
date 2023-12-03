from flask import Flask, render_template, redirect, url_for
from connection import cnx

app = Flask(__name__, static_folder="static")

# ... (Other route definitions)

@app.route("/index")
def index():
    # Your route logic goes here
    return render_template("index.html", atendimentos=atendimentos)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
