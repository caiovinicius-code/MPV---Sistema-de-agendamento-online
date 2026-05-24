# models.py
from app import db
from flask_login import UserMixin

# Herdar de db.Model transforma a classe em uma tabela de banco de dados
class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    whatsapp = db.Column(db.String(20), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    
    # Relacionamento para conseguir buscar os agendamentos do usuário facilmente
    agendamentos = db.relationship('Agendamento', backref='cliente', lazy=True)

class Profissional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)
    
    agendamentos = db.relationship('Agendamento', backref='profissional', lazy=True)

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_hora = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='pendente')
    
    # Chaves estrangeiras ligando as tabelas (Integridade Referencial)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissional.id'), nullable=False)