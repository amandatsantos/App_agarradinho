from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base


class Produto(Base):
    __tablename__ = "Produto"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco= (Float)
    disponivel = Column(Boolean)


class Usuario(Base):
    ...