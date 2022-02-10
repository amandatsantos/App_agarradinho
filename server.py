from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.repositorio.produto import RepositorioProduto

from src.schemas.schemas import Usuario
from src.infra.sqlalchemy.repositorio.user import RepositorioUser

criar_db()
app = FastAPI()

@app.get('/')
def root():
    return {'msg': 'rodando'}

# produtos
@app.post('/criar-produto')
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


#usuarios

@app.post('/criar-usuario')
def criar_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUser(db).criar_user(usuario)
    return usuario_criado

@app.get('/usuarios')
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUser(db).listar_user()
    return usuarios