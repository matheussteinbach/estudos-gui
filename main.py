from tela import Tela
from tela_inicial import Tela_Inicial


tela = Tela()
tela_inicial = Tela_Inicial()
botao, valores = tela_inicial.open()

if botao == 'Incluir':
    tela = Tela()
    tela.open()

elif botao == 'Editar':
    tela_inicial.editar()