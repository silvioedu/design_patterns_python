class Instalador:

  def __init__(self, fonte, destino):
    self.opcoes = []
    self.destino = destino
    self.fonte = fonte
  
  def preferencias(self, escolha):
    self.opcoes.append(escolha)
  
  def executar(self):
    for opcao in self.opcoes:
      print(opcao)
      if list(opcao.values())[0]:
        print(f'Copiando o binários de {self.fonte} para {self.destino}')
      else:
        print('Operação finalizada')


if __name__ == '__main__':
  instalador = Instalador('python3.9.1.gzip', '/usr/bin/')

  instalador.preferencias({'python': True})
  instalador.preferencias({'java': False})

  instalador.executar()