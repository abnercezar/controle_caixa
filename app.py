from flask import Flask, render_template, redirect, url_for, request
from connection import cnx

app = Flask(__name__, static_folder="static")

# Função fictícia para obter dados de atendimentos
def obter_dados_atendimentos():
    # Substitua esta lógica com a lógica real para obter seus dados de atendimentos
    dados_atendimentos = [
        ("Irmã(o) 1", "Comum 1", 100, "2023-12-04"),
        ("Irmã(o) 2", "Comum 2", 150, "2023-12-03"),
        # ... outros dados
    ]
    return dados_atendimentos

# Rota para a página index e atendimentos
@app.route('/')
def index():
    # Criar um gráfico Plotly simples
    trace = go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13], mode='markers')
    data = [trace]
    layout = go.Layout(title='Gráfico de Exemplo', showlegend=False)
    fig = go.Figure(data=data, layout=layout)

    # Passar o objeto 'fig' para o template ao renderizar
    return render_template('seu_template.html', fig=fig)

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        # Lógica para processar o formulário de cadastro
        # ...
        return redirect(url_for('alguma_pagina_apos_cadastro'))  # ajuste conforme necessário
    else:
        # Lógica para exibir a página de cadastro
        return render_template("cadastro.html")


@app.route("/dashboard")
def dashboard():
    # Lógica para a página de dashboard
    return render_template("dashboard.html")

@app.route("/funcionarios")
def funcionarios():
    # Lógica para a página de funcionários
    return render_template("funcionarios.html")

@app.route("/pagamentos")
def pagamentos():
    # Lógica para a página de pagamentos
    return render_template("pagamentos.html")

@app.route("/empresas_terc")
def empresas_terc():
    # Lógica para a página de empresas_terc
    return render_template("empresas_terc.html")

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
    app.run(debug=True)
    
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)
