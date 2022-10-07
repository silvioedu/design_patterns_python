from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

  @abstractmethod
  def manipular(self):
    pass


class StateConcretaA(State):

  def manipular(self):
    print(f'State concreta A')


class StateConcretaB(State):

  def manipular(self):
    print(f'State concreta B')


class Context(State):

  def __init__(self) -> None:
    self.state = None
  
  def get_state(self):
    return self.state
  
  def set_state(self, state):
    self.state = state
  
  def manipular(self):
    self.state.manipular()


contexto = Context()
state_A = StateConcretaA()
state_B = StateConcretaB()

contexto.set_state(state_A)
contexto.manipular()

contexto.set_state(state_B)
contexto.manipular()