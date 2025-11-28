

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.banco import get_db
from app.models import Usuario, UsuarioBase


def criar_usuario(user:UsuarioBase, db: Session = Depends(get_db())):
    novo_user = Usuario(
        nome=user.nome.strip(),
        email = user.email.strip(),
    )
    emailCadastrado = db.query(Usuario).filter(Usuario.email == user.email).all()
    if emailCadastrado:
        raise HTTPException(404, detail="Email ja cadastrado, tente outro")
    if user.email.count("@gmail.com") != 1:
        return {"mensagem":"Email invalido, digite novamente !!!"}
    db.add(novo_user) #adiciona o novo usuario na sesão
    db.commit() # salva as alterações
    db.refresh(novo_user)  # atualiza no banco
    return {
        "menssagem":"Usuario Cadastrado Com Sucesso !!!", 
        "dados":{
            "nome":novo_user.nome
            }
    }

def buscar_usuario_pelo_id(id:int, db:Session):
    user = db.query(Usuario).filter(Usuario.id == id).all()
    if not user:
        raise HTTPException(404, detail="Usuario não Encontrado !!!")
    return {
        "mensagem":"Usuario Encontrado !!!",
        "dados":user
        }


def remover_usuario(id:int, db:Session):
    user = db.query(Usuario).filter(Usuario.id == id).all()
    if not user:
        raise HTTPException(404, detail="Usuario não Encontrado !!!")
    db.delete(user[0])
    db.commit()
    return {"menssagem":f"Usuario {user[0].nome}, removido !!!"}

def atualizar_nome_usuario(id:int,nome_novo:str, db:Session):
    user = db.query(Usuario).filter(Usuario.id == id).all()
    if not user:
        raise HTTPException(404, detail="Usuario não Encontrado !!!")
    user[0].nome = nome_novo
    db.add(user[0])
    db.commit()
    db.refresh(user[0])
    return {
        "menssagem": "Nome atualizado !!!",
        "dados":{
            "nome":user[0].nome,
            "email":user[0].email,
        }
    }

    