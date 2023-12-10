from flask import Flask, render_template, redirect, url_for, request
from plotly.graph_objs import Figure
from connection import get_mysql_connection

app = Flask(__name__, static_folder="static")



# Rota para a página index e atendimentos
@app.route("/")
def index():
    # Obtém uma conexão com o banco de dados
    conn = get_mysql_connection()

    if conn:
        # Lógica para processar a conexão e renderizar a página
        # ...

        # Fecha a conexão após o uso
        conn.close()

    return render_template("index.html")


# Rota para a página de cadastros
@app.route("/cadastros", methods=["GET", "POST"])
def cadastros():
    if request.method == "POST":
        # Lógica para processar o formulário de cadastros
        name = request.form.get("name")
        email = request.form.get("email")

        # Obtém uma conexão com o banco de dados
        conn = get_mysql_connection()

        if conn:
            cursor = conn.cursor()

            # Execute a instrução SQL INSERT
            sql_insert = "INSERT INTO users (name, email) VALUES (%s, %s)"
            values = (name, email)
            cursor.execute(sql_insert, values)

            # Faça o commit da transação e feche a conexão
            conn.commit()
            conn.close()

        # Redirecione após a inserção
        return redirect(url_for("cadastro"))

    else:
        # Lógica para exibir a página de cadastros
        return render_template("cadastros.html")


@app.route("/dashboard")
def dashboard():
    # Criar um objeto Figure do Plotly
    fig = Figure(data=[{"x": [1, 2, 3], "y": [4, 5, 6]}])

    # Adicionar um log para verificar o conteúdo da variável fig
    print(fig)

    return render_template("dashboard.html", fig=fig)


@app.route("/irmas")
def irmas():
    # Lógica para a página de irmas
    return render_template("irmas.html")


@app.route("/atendimentos")
def atendimentos():
    # Lógica para a página de atendimentos
    return render_template("atendimentos.html")


@app.route("/comuns")
def comuns():
    # Lógica para a página de comuns
    return render_template("comuns.html")


@app.route("/login")
def login():
    # Lógica para a página de login
    return render_template("login.html")


@app.route("/form_atendimento/<int:id>")
def form_atendimento(id):
    # Lógica para a página de form_atendimento
    return render_template("form_atendimento.html", id=id)


@app.route("/excluir_atendimento/<int:id>")
def excluir_atendimento(id):
    # Lógica para a página de excluir_atendimento
    return render_template("excluir_atendimento.html", id=id)




if __name__ == "__main__":
    app.run(port=5000, debug=True)
