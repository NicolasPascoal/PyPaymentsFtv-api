from flask import Blueprint, request, jsonify
from app.controllers.pagamentos import *

pagamentos_bp = Blueprint("pagamentos", __name__)

@pagamentos_bp.route("/add/pagamentos", methods=["POST"])
def criar():
    data = request.json

    pagamento = criar_pagamento(

        plano_id=data["plano_id"],
        data_pagamento=data["data_pagamento"],
        praticante_id=data["praticante_id"]
    )

    return jsonify({
        "mensagem": "Pagamento cadastrado com sucesso",
        "id": pagamento.id
    }), 201

@pagamentos_bp.route("/pagamentos/vencidos", methods=["GET"])
def get_pagamentos_vencidos():
    pagamentos = listar_pagamentos_vencidos()

    return jsonify([
        {
            "id": p.id,
            "valor": float(p.valor),
            "data_vencimento": p.data_vencimento.strftime("%Y-%m-%d"),
            "praticante_id": p.praticante_id
        }
        for p in pagamentos
    ]), 200

@pagamentos_bp.route("/praticantes/<int:praticante_id>/pagamentos", methods=["GET"])
def get_pagamentos_por_praticante(praticante_id):
    pagamentos = listar_pagamentos_por_praticante(praticante_id)

    return jsonify([
        {
            "id": p.id,
            "valor": float(p.valor),
            "pago": p.pago,
            "status": calcular_status_pagamento(p),
            "data_pagamento": p.data_pagamento.strftime("%Y-%m-%d"),
            "data_vencimento": p.data_vencimento.strftime("%Y-%m-%d")
        }
        for p in pagamentos
    ]), 200