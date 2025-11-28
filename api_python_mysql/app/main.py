from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from app.banco import get_db, BASE, ENGINE
from app.crud import criar_usuario, buscar_usuario_pelo_id, remover_usuario, atualizar_nome_usuario
from app.models import Usuario, Post, UsuarioBase


app = FastAPI()

BASE.metadata.create_all(bind=ENGINE)

@app.get("/")
def rota_raiz():
    return {"menssagem":"Api rodando !!!"}


@app.get("/users/{id}")
def rota_pegar_usuario(id:int, db:Session = Depends(get_db)):
    return buscar_usuario_pelo_id(id, db=db)

@app.post("/users")
def rota_create_user(user: UsuarioBase, db:Session = Depends(get_db)):
    return criar_usuario(user, db)

@app.delete("/users/{id}")
def rota_deletar_usuario(id:int, db:Session = Depends(get_db)):
    return remover_usuario(id=id, db=db)

@app.put("/users/{id}")
def rota_atualizar_usuario(id:int, nome_novo:str, db:Session = Depends(get_db)):
    return atualizar_nome_usuario(id=id, nome_novo=nome_novo, db=db)


