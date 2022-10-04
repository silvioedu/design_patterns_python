from abc import ABCMeta, abstractmethod


class Comando(metaclass=ABCMeta):

  def __init__(self, receiver) -> None:
    self.receiver = receiver
  
  @abstractmethod
  def executar(self):
    pass


class ComandoConcreto(Comando):

  def __init__(self, receiver) -> None:
    self.receiver = receiver
  
  def executar(self):
    self.receiver.acao()
  

class Receiver:

  def acao(self):
    print('Ação do Receiver')


class Invoker:

  def comando(self, cmd):
    self.cmd = cmd
  
  def executar(self):
    self.cmd.executar()


if __name__ == '__main__':
  receiver = Receiver()
  cmd = ComandoConcreto(receiver)
  invoker = Invoker()
  
  invoker.comando(cmd)
  invoker.executar()