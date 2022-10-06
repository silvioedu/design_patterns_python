from db import _executar


class Produto:

  def __init__(self, nome, preco, id=None) -> None:
    self.id = id
    self.nome = nome
    self.preco = preco
    self.status = 1 # ativo=1; inativo=0

    #se a tabela não existir, crie-a
    query = 'CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco REAL, status NUMERIC)'
    _executar(query)
  
  def salvar(self):
    query = f'INSERT INTO produtos (nome, preco, status) VALUES ("{self.nome}", "{float(self.preco)}", "{self.status}")'
    _executar(query)
  
  def atualizar(self):
    query = f'UPDATE produtos SET status={self.status} where id={int(self.id)}'
    _executar(query)
  
  def deletar(self):
    query = f'DELETE FROM produtos WHERE id={int(self.id)}'
    _executar(query)

  @staticmethod
  def get_produtos():
    query = 'SELECT * FROM produtos'
    return _executar(query)

  @staticmethod
  def get_produto(id):
    query = f'SELECT id, nome, preco FROM produtos where id={int(id)}'
    result = _executar(query)[0]
    produto = Produto(id=result[0], nome=result[1], preco=result[2])
    return produto


