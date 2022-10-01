class Singleton:

  __instance = None

  def __init__(self) -> None:
    if not Singleton.__instance:
      print('O método __init__ foi chamado')
    else:
      print(f'A instância já foi criada {self.get_instance()}')
  
  @classmethod
  def get_instance(cls):
    if not cls.__instance:
      cls.__instance = Singleton()
    return cls.__instance


s1 = Singleton()

print(f'Objeto criado agora {Singleton.get_instance()}')

s2 = Singleton()