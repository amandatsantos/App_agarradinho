from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioUser():

    def __init__(self, db:Session):
        self.db = db


    def criar_user(self, usuario: schemas.Usuario):
        db_user = models.Usuario(nome = usuario.nome,
                                 telefone = usuario.telefone)

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user


    def listar_user(self):
        usuarios = self.db.query(models.Usuario).all()
        return usuarios

    def obter(self):
        ...

    def remover(self):
        ...