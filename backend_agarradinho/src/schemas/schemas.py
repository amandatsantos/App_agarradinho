from pydantic import BaseModel
from typing import Optional, List

class Usuario(BaseModel):
    id : Optional[str]  = None
    nome: str
    telefone: str
    

class Produto(BaseModel):
    id: Optional[str] = None
    usuario:Usuario
    nome:str
    preco: float
    disponivel: bool = False
    descricao: str

    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quatidade: int
    entrega:bool = True
    endereco: str
    observacao: Optional[str] = 'Sem observações'

class UsuarioMovi(BaseModel):
    usuario: Usuario
    vendas: List[Pedido]
    produtos: List[Produto]
    pedidos: List[Pedido]