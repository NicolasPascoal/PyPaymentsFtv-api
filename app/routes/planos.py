from flask import Blueprint, request, jsonify
from app.controllers.planos import (
    criar_plano,
    listar_planos,
    buscar_plano,
    atualizar_plano,
    deletar_plano
)

planos_bp = Blueprint("planos", __name__)

# CREATE
@planos_bp.route("/add/planos", methods=["POST"])
def criar():
    data = request.json

    plano = criar_plano(
        nome=data["nome"],
        valor=data["valor"]
    )

    return jsonify({
        "id": plano.id,
        "nome": plano.nome,
        "valor": float(plano.valor)
    }), 201


# READ ALL
@planos_bp.route("/planos", methods=["GET"])
def listar():
    planos = listar_planos()

    return jsonify([
        {
            "id": p.id,
            "nome": p.nome,
            "valor": float(p.valor),
        }
        for p in planos
    ]), 200


# READ ONE
@planos_bp.route("/planos/<int:plano_id>", methods=["GET"])
def buscar(plano_id):
    plano = buscar_plano(plano_id)

    if not plano:
        return jsonify({"erro": "Plano não encontrado"}), 404

    return jsonify({
        "id": plano.id,
        "nome": plano.nome,
        "valor": float(plano.valor),
    }), 200


# UPDATE
@planos_bp.route("/planos/<int:plano_id>", methods=["PUT"])
def atualizar(plano_id):
    data = request.json
    plano = atualizar_plano(plano_id, data)

    if not plano:
        return jsonify({"erro": "Plano não encontrado"}), 404

    return jsonify({
        "mensagem": "Plano atualizado com sucesso",
        "id": plano.id
    }), 200


# DELETE
@planos_bp.route("/planos/<int:plano_id>", methods=["DELETE"])
def deletar(plano_id):
    sucesso = deletar_plano(plano_id)

    if not sucesso:
        return jsonify({"erro": "Plano não encontrado"}), 404

    return jsonify({
        "mensagem": "Plano deletado com sucesso"
    }), 200
