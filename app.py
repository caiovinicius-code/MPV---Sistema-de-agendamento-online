import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)

# Configurações de Segurança e Banco de Dados
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave-secreta-padrao')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///agendamento.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o Banco de Dados
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "<h1>Sistema de Agendamento Online</h1><p>O servidor está rodando!</p>"

if __name__ == '__main__':
    app.run(debug=True)