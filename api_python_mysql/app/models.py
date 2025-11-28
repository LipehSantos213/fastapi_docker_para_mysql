from pydantic import BaseModel
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from app.banco import BASE


class Usuario(BASE):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    ativo = Column(Boolean, default=True)
    criado_em=Column(DateTime(timezone=True), server_default=func.now())

    posts = relationship("Post", back_populates="autor")

class UsuarioBase(BaseModel):
    nome:str
    email: str


class Post(BASE):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    conteudo = Column(String(300), nullable=False)
    user_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"))

    autor = relationship("Usuario", back_populates="posts")
