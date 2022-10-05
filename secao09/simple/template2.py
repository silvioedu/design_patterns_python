from abc import ABCMeta, abstractmethod


class ClasseAbstrata(metaclass=ABCMeta):

  def __init__(self) -> None:
    pass

  @abstractmethod
  def operacao1(self):
    pass

  @abstractmethod
  def operacao2(self):
    pass

  def template_method(self):
    self.operacao1()
    self.operacao2()


class ClasseConcreta(ClasseAbstrata):

  def operacao1(self):
    print('Minha operação concreta 1')
  
  def operacao2(self):
    print('Minha operação concreta 2')


concreta = ClasseConcreta()
concreta.template_method()