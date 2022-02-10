from sqlalchemy import Column, Integer, String, Float, Boolean, true
from src.infra.sqlalchemy.config.database import Base


class Produto(Base):
    __tablename__ = "Produto"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco= Column(Float)
    disponivel = Column(Boolean)


class Usuario(Base):
    __tablename__ = "Usuario"

    id = Column(Integer, primary_key= True, index= True)
    nome= Column(String)
    telefone = Column(Integer)