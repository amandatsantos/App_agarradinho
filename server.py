from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.repositorio.produto import RepositorioProduto

criar_db()
app = FastAPI()

@app.get('/')
def root():
    return {'msg': 'rodando'}

@app.post('/criar-produto')
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos