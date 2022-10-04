from abc import ABCMeta, abstractmethod

# Command
class Ordem(metaclass=ABCMeta):

  @abstractmethod
  def executar(self):
    pass

# Concrete Command
class OrdemCompra(Ordem):

  def __init__(self, acao) -> None:
    self.acao = acao

  def executar(self):
    self.acao.comprar()

# Concrete Command
class OrdemVenda(Ordem):

  def __init__(self, acao) -> None:
    self.acao = acao

  def executar(self):
    self.acao.vender()

# Receiver
class Acao:
  
  def comprar(self):
    print(f'Você irá comprar ações')
  
  def vender(self):
    print(f'Você irá vender ações')

# Invoker
class Agente:

  def __init__(self) -> None:
    self.__fila_ordens = []
  
  def adicionar_ordem_na_fila(self, ordem):
    self.__fila_ordens.append(ordem)
    ordem.executar()
  

if __name__ == '__main__':
  acao = Acao()
  ordem_compra = OrdemCompra(acao)
  ordem_venda  = OrdemVenda(acao)

  agente = Agente()
  agente.adicionar_ordem_na_fila(ordem_compra)
  agente.adicionar_ordem_na_fila(ordem_venda)
  