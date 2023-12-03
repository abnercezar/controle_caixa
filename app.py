from flask import Flask, render_template, request, redirect, url_for
import plotly.graph_objs as go
from connection import cnx

app = Flask(__name__, static_folder="static")


@app.route("/")
def home():
    return redirect(url_for("index"))


@app.route("/index")
def index():
    # Conexão com o banco de dados
    cursor = cnx.cursor()

    # Cosulta para atendimentos realizados
    cursor.execute(
        """
       SELECT a.irma_id, i.tipo, a.valor, c.nome 
FROM atendimentos a 
INNER JOIN irmas i ON a.irma_id = i.id 
INNER JOIN comum_irma ci ON i.id = ci.irma_id 
INNER JOIN comuns c ON ci.comun_id = c.id 
LIMIT 0, 1000

       """
    )
    atendimentos = cursor.fetchall()

    # Feche a conexão com o banco de dados
    cursor.close()

    return render_template("index.html", atendimentos=atendimentos)


if __name__ == "__main__":
    app.run()

if __name__ == "__main__":
    app.run(port=8080)
