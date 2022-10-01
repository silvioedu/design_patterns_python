from abc import ABCMeta, abstractmethod

# Abstract Factory
class PizzaFactory(metaclass=ABCMeta):
  @abstractmethod
  def criar_pizza_veg(self):
    pass

  @abstractmethod
  def criar_pizza(self):
    pass

# Concrect Factory A
class PizzaBrasileira(PizzaFactory):

  def criar_pizza_veg(self):
    return PizzaMandioca()
  
  def criar_pizza(self):
    return PizzaCamarao()

# Concrect Factory B
class PizzaItaliana(PizzaFactory):

  def criar_pizza_veg(self):
    return PizzaBrocoli()
  
  def criar_pizza(self):
    return PizzaBolonha()

# Abstract Product A
class PizzaVeg(metaclass=ABCMeta):
  @abstractmethod
  def preparar(self, PizzaVeg):
    pass

# Abstract Product B
class Pizza(metaclass=ABCMeta):
  @abstractmethod
  def servir(self, PizzaVeg):
    pass

# Abstract Product A
class PizzaMandioca(PizzaVeg):
  def preparar(self):
    print(f'Preparando {type(self).__name__}')

# Concrect Product B
class PizzaBrocoli(PizzaVeg):
  def preparar(self):
    print(f'Preparando {type(self).__name__}')

# Concrect Product C
class PizzaCamarao(Pizza):
  def servir(self, PizzaVeg):
    print(f'{type(self).__name__} é servida com camarão na {type(PizzaVeg).__name__}')

# Concrect Product D
class PizzaBolonha(Pizza):
  def servir(self, PizzaVeg):
    print(f'{type(self).__name__} é servida com bolonha na {type(PizzaVeg).__name__}')


class Pizzaria:

  def fazer_pizzas(self):
    for factory in [PizzaBrasileira(), PizzaItaliana()]:
      self.factory = factory
      self.pizza = self.factory.criar_pizza()
      self.pizza_veg = self.factory.criar_pizza_veg()
      self.pizza_veg.preparar()
      self.pizza.servir(self.pizza_veg)


pizzaria = Pizzaria()
pizzaria.fazer_pizzas() 