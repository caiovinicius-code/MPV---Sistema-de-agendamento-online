import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# 1. Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# 2. Configurações de Segurança e Banco de Dados
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave-secreta-padrao-de-seguranca')
# Se não encontrar o DATABASE_URL no .env, ele usa o SQLite local como padrão seguro
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///agendamento.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Inicializa o Banco de Dados (ORM)
db = SQLAlchemy(app)

# 4. Importa os modelos APÓS a inicialização do 'db' para evitar importação circular
from models import Usuario

# 5. Rota Principal (Página de Login) - Aceita GET (carregar a página) e POST (enviar o formulário)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Captura o que o usuário preencheu nos campos 'name' do HTML
        whatsapp_digitado = request.form.get('whatsapp')
        senha_digitada = request.form.get('senha')
        
        # Faz uma consulta no banco de dados buscando o primeiro usuário com esse WhatsApp
        usuario = Usuario.query.filter_by(whatsapp=whatsapp_digitado).first()
        
        # Validação de Login (Checando o usuário e a senha informada)
        if usuario and usuario.senha_hash == senha_digitada:
            print(f"Sucesso: O usuário {usuario.nome} entrou no sistema!")
            return f"<h1>Bem-vindo, {usuario.nome}! Login realizado com sucesso.</h1>"
        else:
            print(f"Tentativa falhou para o WhatsApp: {whatsapp_digitado}")
            # Recarrega a página passando uma mensagem de erro para o usuário
            return render_template('auth/login.html', erro="WhatsApp ou senha incorretos.")
            
    # Se for uma requisição GET comum, apenas exibe a tela de login vazia
    return render_template('auth/login.html')

# 6. Inicialização do Servidor (Modo de Desenvolvimento)
if __name__ == '__main__':
    app.run(debug=True)