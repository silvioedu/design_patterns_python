from re import S


class GerenciamentoEventos:

  def __init__(self) -> None:
    print('Gerenciamento de eventos :: vou organizar tudo\n')

  def organizar(self):
    self.salao = SalaoFestas()
    self.salao.agendar()
    
    self.florista = Florista()
    self.florista.arranjar_flores()

    self.comida = Restaurante()
    self.comida.preparar()

    self.musica = Banda()
    self.musica.montar_palco()


class SalaoFestas:

  def __init__(self) -> None:
    print('Salão de Festas :: Agendando')
  
  def _esta_disponivel(self):
    print('Salão de Festas :: Está disponível')
    return True
  
  def agendar(self):
    if self._esta_disponivel():
      print('Salão de Festas :: Agendado com sucesso\n')


class Florista:

  def __init__(self) -> None:
    print('Florista :: Flores para o evento?')

  def arranjar_flores(self):
    print('Florista ::  Rosas, Margaridas e Lírios serão usados\n')


class Restaurante:

  def __init__(self) -> None:
    print('Restaurante :: Comida para o evento?')

  def preparar(self):
    print('Restaurante :: Comida chinesa e brasileira serão servidas\n')


class Banda:

  def __init__(self) -> None:
    print('Banda :: Arranjos musicais para o evento')
  
  def montar_palco(self):
    print('Banda :: Palco preparado para tocar jazz\n')


class Cliente:

  def __init__(self) -> None:
    print('Cliente :: Preparação para o casamento')

  def contrata_gerente_eventos(self):
    print('Cliente :: Vou contratar uma empresa pra gerenciar eventos\n')

    ge = GerenciamentoEventos()
    ge.organizar()
  
  def __del__(self):
    print('Cliente :: Foi muito simples organizar este evento com o Facade')


if __name__ == '__main__':
  cliente = Cliente()
  cliente.contrata_gerente_eventos()


