# Sistema de Agendamento Online - Projeto Integrador

## 1. Proposta do Sistema
O projeto consiste em uma plataforma web desenvolvida para otimizar o processo de agendamento de serviços. O sistema visa substituir controles manuais por uma interface digital onde clientes podem visualizar horários disponíveis, realizar agendamentos via identificação por WhatsApp e gestores podem administrar o fluxo de faturamento e profissionais.

## 2. Equipe Responsável
*   **Caio Vinícius Lima Soares** 

## 3. Roadmap de Desenvolvimento
- [x] Definição da arquitetura e estrutura de pastas.
- [x] Configuração do ambiente virtual (venv) e dependências.
- [x] Modelagem inicial do banco de dados (SQLAlchemy).
- [x] Implementação da rota de login e integração com Bootstrap.
- [ ] Desenvolvimento do módulo de autenticação.
- [ ] Criação do CRUD de agendamentos.
- [ ] Integração com banco de dados MariaDB.

## 4. Configuração e Execução
Siga os passos abaixo para rodar a aplicação em seu ambiente local (Linux/Windows):

1. **Clonar o repositório:**
   ```bash
   git clone <link-do-repositorio>
   cd "Projeto Integrador - Sistema Agendamento"
   
2. Configurar o ambiente virtual:
  python3 -m venv venv
source venv/bin/activate

3. Instalar dependências:
   pip install flask flask-sqlalchemy flask-login mysql-connector-python python-dotenv
   
5. Configurar variáveis de ambiente:
   Crie um arquivo `.env` na raiz com:
   ```text
   DATABASE_URL=sqlite:///agendamento.db
   SECRET_KEY=sua_chave_secreta

6. Executar aplicação
   python app.py
   
## 5. Integração de Paradigmas de Programação

O sistema foi estruturado utilizando a convergência de múltiplos paradigmas para garantir eficiência e manutenibilidade:

### A. Programação Orientada a Objetos (POO)
Utilizada no arquivo `models.py` para representar as entidades do mundo real (Usuário, Profissional, Agendamento) através de **Classes**. Isso permite o uso de herança e encapsulamento no gerenciamento dos dados.

### B. Programação Imperativa
Aplicada na lógica de inicialização e configuração do servidor no `app.py`, onde as instruções são seguidas em uma sequência lógica definida para preparar o ambiente.

### C. Programação Funcional/Declarativa
Manifesta-se no uso de **Decoradores** do Flask (ex: `@app.route`), onde declaramos "o que" o código deve fazer (mapear uma URL) sem necessariamente detalhar "como" o servidor web trata a requisição internamente. Além disso, o uso de ORM (SQLAlchemy) permite consultas declarativas ao banco de dados.
