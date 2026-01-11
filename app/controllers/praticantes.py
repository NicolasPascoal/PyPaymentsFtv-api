from app.extensions import db
from app.models.praticante import Praticante

def criar_praticante(nome, telefone, personal):
    praticante = Praticante(
        nome=nome,
        telefone=telefone,
        personal=personal
    )
    db.session.add(praticante)
    db.session.commit()
    return praticante

def listar_praticantes():
    return Praticante.query.all()

def buscar_praticante(praticante_id):
    return Praticante.query.get(praticante_id)

def atualizar_praticante(praticante_id, dados):
    praticante = buscar_praticante(praticante_id)
    if not praticante:
        return None

    praticante.nome = dados.get("nome", praticante.nome)
    praticante.telefone = dados.get("telefone", praticante.telefone)
    praticante.personal = dados.get("personal", praticante.personal)
    praticante.ativo = dados.get("ativo", praticante.ativo)

    db.session.commit()
    return praticante

def deletar_praticante(praticante_id):
    praticante = buscar_praticante(praticante_id)
    if not praticante:
        return False

    db.session.delete(praticante)
    db.session.commit()
    return True
