# seed.py
from app import app, db
from models import Usuario

print("Iniciando a criação do usuário...")

with app.app_context():
    # 1. Verifica se o usuário já existe para não duplicar
    usuario_existe = Usuario.query.filter_by(whatsapp="99999999999").first()
    
    if not usuario_existe:
        # 2. Se não existir, cria o seu usuário de teste
        novo_usuario = Usuario(
            nome="Caio Vinicius", 
            whatsapp="99999999999", 
            senha_hash="123456"
        )
        db.session.add(novo_usuario)
        db.session.commit()
        print("🎉 Usuário 'Caio Vinicius' criado com sucesso!")
    else:
        print("💡 O usuário com este WhatsApp já está cadastrado no banco.")