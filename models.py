# models.py
# Aqui definimos a estrutura dos dados usando Classes (POO)

class Usuario:
    def __init__(self, id, nome, whatsapp, senha_hash):
        self.id = id
        self.nome = nome
        self.whatsapp = whatsapp
        self.senha_hash = senha_hash

class Profissional:
    def __init__(self, id, nome, especialidade):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade

class Agendamento:
    def __init__(self, id, usuario_id, profissional_id, data_hora, status='pendente'):
        self.id = id
        self.usuario_id = usuario_id
        self.profissional_id = profissional_id
        self.data_hora = data_hora
        self.status = status