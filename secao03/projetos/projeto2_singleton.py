class SanidadeCheck:

  __instance = None

  def __new__(cls, *args, **kwargs):
    if not SanidadeCheck.__instance:
      SanidadeCheck.__instance = super(SanidadeCheck, cls).__new__(cls, *args, **kwargs)
    return SanidadeCheck.__instance
  
  def __init__(self):
    self.__servidores = []
  
  def checar_servidor(self, srv):
    print(f'Checando servidor {self.__servidores[srv]}')
  
  def add_servidor(self):
    self.__servidores = [f'Servidor {i}' for i in range(1, 5)]
  
  def mudar_servidor(self):
    self.__servidores.pop()
    self.__servidores.append('Servidor 5')


sc1 = SanidadeCheck()
sc2 = SanidadeCheck()

sc1.add_servidor()
print(f'Cronograma de checagem de sanidade de servidores A...')
[sc1.checar_servidor(srv) for srv in range(4)] 

sc2.mudar_servidor()
print(f'Cronograma de checagem de sanidade de servidores B...')
[sc2.checar_servidor(srv) for srv in range(4)] 
