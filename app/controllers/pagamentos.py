from datetime import datetime
from dateutil.relativedelta import relativedelta
from app.extensions import db
from app.models.pagamentos import Pagamentos
from app.models.planos import Plano

def criar_pagamento( data_pagamento, praticante_id, plano_id):
    if isinstance(data_pagamento, str):
        data_pagamento = datetime.strptime(data_pagamento, "%Y-%m-%d")
    plano = Plano.query.get(plano_id)
    data_vencimento = data_pagamento + relativedelta(months=1)

    pagamento = Pagamentos(
        valor=plano.valor,
        pago=False,
        data_pagamento=data_pagamento,
        data_vencimento=data_vencimento,
        praticante_id=praticante_id,
        plano_id = plano_id
    )

    db.session.add(pagamento)
    db.session.commit()
    return pagamento


def listar_pagamentos_vencidos():
    hoje = datetime.now()

    return Pagamentos.query.filter(
        Pagamentos.pago == False,
        Pagamentos.data_vencimento < hoje
    ).all()

def calcular_status_pagamento(pagamento):
    if pagamento.pago:
        return "PAGO"

    hoje = datetime.now()

    if pagamento.data_vencimento < hoje:
        return "VENCIDO"

    return "EM_DIA"

def listar_pagamentos_por_praticante(praticante_id):
    return Pagamentos.query.filter_by(praticante_id=praticante_id).all()
