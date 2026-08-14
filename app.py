from flask import Flask,render_template ,jsonify

app = Flask(__name__)

VAGAS = [
    {   
        'id': 1,
        "titulo": "Desenvolvedor Python",
        "descricao": "Estamos procurando um desenvolvedor Python para se juntar à nossa equipe.",
        "localizacao": "São Paulo, SP",
        "salario": "R$ 5.000 - R$ 7.000"
    },
    {   
        'id': 2,
        "titulo": "Desenvolvedor Backend",
        "descricao": "Buscamos um desenvolvedor backend com experiência em Python e SQL.",
        "localizacao": "Rio de Janeiro, RJ",
        "salario": "R$ 6.000 - R$ 8.000"
    },
    {
        'id': 3,
        "titulo": "Analista de Machine Learning",
        "descricao": "Procuramos um analista de machine learning para trabalhar em projetos inovadores.",
        "localizacao": "Belo Horizonte, MG",
        "salario": "R$ 7.000 - R$ 9.000"
    },
    {
            'id': 4,
            "titulo": "Desenvolvedor Frontend",
            "descricao": "Procuramos um desenvolvedor frontend para se juntar à nossa equipe.",
            "localizacao": "São Paulo, SP",
            "salario": "R$ 5.000 - R$ 7.000"
        },
        {
                    'id': 5,
                    "titulo": "Cientista de Dados",
                    "descricao": "Procuramos um cientista de dados com experiência em Python e análise de dados.",
                    "localizacao": "São Paulo, SP",
                    "salario": "R$ 6.000 - R$ 8.000"
                }

]

@app.route("/")
def hello():
    return render_template("home.html", vagas=VAGAS)
@app.route("/vagas")
def vagas():
    return jsonify(VAGAS)   

if __name__ == "__main__":
    app.run(debug=True)