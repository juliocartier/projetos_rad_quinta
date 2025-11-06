from flask import Blueprint
from controllers import usuarios_controller

usuarios_bp = Blueprint("usuarios_bp", __name__)

usuarios_bp.route("/", methods=["GET"])(usuarios_controller.index)
usuarios_bp.route("/listar_usuarios", methods=["GET"])(usuarios_controller.listar_usuarios)
usuarios_bp.route("/criar_usuarios", methods=["POST"])(usuarios_controller.criar_usuarios)
usuarios_bp.route("/deleta_usuarios/<int:user_id>", methods=["DELETE"])(usuarios_controller.deletar_usuarios)
usuarios_bp.route("/atualizar_usuarios/<int:user_id>", methods=["PUT"])(usuarios_controller.atualizar_usuarios)