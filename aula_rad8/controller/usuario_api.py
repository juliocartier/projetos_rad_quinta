from flask import Blueprint, jsonify, request
from models.usuarios import salvar_usuarios, listas_usuarios

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/", methods=['GET'])
def inicio():
    return jsonify({"mensagem": "Ola pessoal! Bem vindo ao mundo 42..."})

@usuarios_bp.route("/usuarios", methods=['GET'])
def listar():
    retorno = listas_usuarios()
    return jsonify(retorno)

@usuarios_bp.route("/usuarios", methods=['POST'])
def criar():
    dados = request.json
    novo = salvar_usuarios(dados)
    return jsonify(novo), 201