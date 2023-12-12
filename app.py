from dotenv import load_dotenv
import os
from flask import Flask, render_template, redirect, url_for, request, flash, session

print(flash)
from plotly.graph_objs import Figure
from connection import get_mysql_connection

app = Flask(__name__, static_folder="static")
app.secret_key = os.getenv("SECRET_KEY")
print(app.secret_key)
app.env = "development"
app.debug = True


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
        email = request.form.get("email").strip()

        # Verifica se o e-mail já existe no banco de dados
        if not email_exists(email):
            # Obtém uma conexão com o banco de dados
            conn = get_mysql_connection()

            if conn:
                cursor = conn.cursor()

                # Execute a instrução SQL INSERT
                sql_insert = "INSERT INTO users (name, email) VALUES (%s, %s)"
                values = (name, email)
                try:
                    cursor.execute(sql_insert, values)
                    conn.commit()

                    # Redefine a variável de sessão para False após a operação de cadastro bem-sucedida
                    session["mostrar_mensagem"] = True
                except mysql.connector.errors.IntegrityError:
                    flash(
                        "E-mail já cadastrado. Por favor, escolha outro e-mail.",
                        "error",
                    )

                # Feche a conexão
                conn.close()

                # Redirecione após a inserção
                return redirect(url_for("cadastros"))

        else:
            flash("E-mail já cadastrado. Por favor, escolha outro e-mail.", "error")
            

    # Lógica para exibir a página de cadastros
    return render_template("cadastros.html", mostrar_mensagem=session.pop("cadastro_sucesso", False))


# Função para verificar se o e-mail já existe no banco de dados
def email_exists(email):
    conn = get_mysql_connection()

    if conn:
        cursor = conn.cursor(dictionary=True)

        # Execute a instrução SQL SELECT para verificar se o e-mail já existe
        sql_select = "SELECT * FROM users WHERE email = %s"
        cursor.execute(sql_select, (email,))
        result = cursor.fetchone()

        # Feche a conexão
        conn.close()

        return result is not None
    else:
        flash("Erro ao conectar ao banco de dados", "error")
        return False


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
