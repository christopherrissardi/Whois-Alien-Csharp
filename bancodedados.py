import sqlite3
import hashlib

def criar_tabela():
    conexao = sqlite3.connect('C:/Users/ALIEN/Desktop/Projetos/Painel de consultas/Painel Whois Alien Python/whoisalien_users.db')
    cursor = conexao.cursor()

    # Criação da tabela
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()

def cadastrar_usuario(username, password):
    conexao = sqlite3.connect('C:/Users/ALIEN/Desktop/Projetos/Painel de consultas/Painel Whois Alien Python/whoisalien_users.db')
    cursor = conexao.cursor()

    # Hash da senha usando SHA-256
    hash_senha = hashlib.sha256(password.encode()).hexdigest()

    # Inserção do usuário e senha criptografada na tabela
    cursor.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, hash_senha))

    conexao.commit()
    conexao.close()


def verificar_credenciais(username, password):
    conexao = sqlite3.connect('C:/Users/ALIEN/Desktop/Projetos/Painel de consultas/Painel Whois Alien Python/whoisalien_users.db')
    cursor = conexao.cursor()

    # Hash da senha para comparar com o valor armazenado no banco de dados
    hash_senha = hashlib.sha256(password.encode()).hexdigest()

    # Consulta para verificar se as credenciais estão corretas
    cursor.execute('SELECT * FROM usuarios WHERE username=? AND password=?', (username, hash_senha))
    usuario = cursor.fetchone()

    conexao.close()

    return usuario is not None

# Exemplo de uso
criar_tabela()
cadastrar_usuario('1', '1')

# Verificar credenciais
username_input = input("Digite o nome de usuário: ")
senha_input = input("Digite a senha: ")

if verificar_credenciais(username_input, senha_input):
    print("Credenciais corretas. Acesso permitido.")
else:
    print("Credenciais incorretas. Acesso negado.")
