from flask import Blueprint, request, jsonify
from app.controllers.praticantes import (criar_praticante, listar_praticantes, buscar_praticante, deletar_praticante)
praticante_bp = Blueprint("praticantes", __name__)

@praticante_bp.route("/add/praticantes", methods=["POST"])
def criar():
    data = request.json

    praticante = criar_praticante(
        nome=data["nome"],
        telefone=data["telefone"],
        personal=data.get("personal", False)
    )

    return jsonify({"usuario cadastrado com sucesso! id:": praticante.id}), 201



@praticante_bp.route("/praticantes", methods=["GET"])
def get_praticantes():
    praticantes = listar_praticantes()

    return jsonify([
        {
            "id": p.id,
            "nome": p.nome,
            "telefone": p.telefone,
            "personal": p.personal,
            "ativo": p.ativo
        }
        for p in praticantes
    ]), 200

@praticante_bp.route("/praticantes/<int:praticante_id>", methods=["GET"])
def get_praticante(praticante_id):
    praticante = buscar_praticante(praticante_id)

    if not praticante:
        return jsonify({"erro": "Praticante n�o encontrado"}), 404

    return jsonify({
        "id": praticante.id,
        "nome": praticante.nome,
        "telefone": praticante.telefone,
        "personal": praticante.personal,
        "ativo": praticante.ativo
    }), 200

from app.controllers.praticantes import deletar_praticante

@praticante_bp.route("/praticantes/<int:praticante_id>", methods=["DELETE"])
def delete_praticante(praticante_id):
    sucesso = deletar_praticante(praticante_id)

    if not sucesso:
        return jsonify({"erro": "Praticante não encontrado"}), 404

    return jsonify({"msg": "Praticante deletado com sucesso"}), 200

