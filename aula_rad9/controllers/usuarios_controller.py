from flask import request, jsonify
from werkzeug.security import generate_password_hash
from flask_restful import reqparse
from db.conexao import conexao_banco
import re

argumentos = reqparse.RequestParser()
argumentos.add_argument('email', type=str)
argumentos.add_argument('password', type=str)

def index():
    retorno = [{"id": 1, "nome": "Julio"}, {"id": 2, "nome": "Luiz"}]
    return jsonify(retorno)

def listar_usuarios():
    conexao = None
    cursor = None
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT ID, EMAIL FROM USERS")
        usuarios = cursor.fetchall()
        colunas = [desc[0] for desc in cursor.description]
        for desc2 in cursor.description:
            print(desc2[0])
        resultado = [dict(zip(colunas, linha)) for linha in usuarios]
        return jsonify(resultado)
    except Exception as e:
        if conexao:
            conexao.rollback()
        return jsonify({"Erro": f"Erro ao buscar o usuarios: {e}"}), 500
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def criar_usuarios():
    conexao = None
    cursor = None

    try:
        dados = argumentos.parse_args()
        email = dados['email']
        senha = dados['password']

        if not email or not senha:
            return jsonify({"mensagem": "Por favor, verifique todos os campos"}), 400
        
        if len(senha) < 8:
            return jsonify({"mensagem": "Sua senha esta muita curta, digite uma nova senha"}), 400
        
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return jsonify({"mensagem": "Email invalido"}), 400

        conexao = conexao_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM USERS WHERE email = %s", (email,))
        conta = cursor.fetchall()
        if conta:
            return jsonify({"mensagem": "Essa conta ja existe"}), 409
        
        senha_hash = generate_password_hash(senha)
        cursor.execute("INSERT INTO USERS (EMAIL, PASSWORD) VALUES (%s, %s)", (email, senha_hash))
        conexao.commit()
        return jsonify({"mensagem":"Usuario criado com sucesso"}), 201
    except Exception as e:
        if conexao:
            conexao.rollback()
        return jsonify({"erro": f"Erro ao criar o usuario {e}"}), 500
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def deletar_usuarios(user_id):
    conexao = None
    cursor = None
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM USERS WHERE ID = %s", (user_id,))
        conexao.commit()
        return jsonify({"mensagem": "Usuario deletado com sucesso"}), 200
    except Exception as e:
        if conexao:
            conexao.rollback()
        return jsonify({"erro": f"Erro ao deletar o usuario {e}"}), 500
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def atualizar_usuarios(user_id):
    conexao = None
    cursor = None
    try:
        data = request.get_json()
        email = data.get("email")

        conexao = conexao_banco()
        cursor = conexao.cursor()
        cursor.execute("UPDATE USERS SET email = %s WHERE id = %s", (email, user_id))
        conexao.commit()
        return jsonify({"mensagem": "Usuario atualizado com sucesso"}), 200
    except Exception as e:
        if conexao:
            conexao.rollback()
        return jsonify({"erro": f"Erro ao atualizar o usuario {e}"}), 500
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
