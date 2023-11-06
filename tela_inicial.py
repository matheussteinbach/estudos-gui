import PySimpleGUI as sg
import emoji


class Tela_Inicial():
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
                    [sg.Button('Incluir', size=(10,1))],
                    [sg.Button('Excluir', size=(10,1))],
                    [sg.Button('Editar', size=(10,1))],
                    [sg.Button('theus', size=(10,1))]

                ]
        self.__window = sg.Window('Tela Inicial').Layout(layout)

    def editar(self):
        layout = [
                    [sg.Text('Editar Cliente')],
                    [sg.Text('Nome', size=(20,1)), sg.InputText(key= 'nome', size= (10,1))],
                    [sg.Text('Usuario', size=(20,1)), sg.InputText(key= 'usuario')],
                    [sg.Text('Senha', size=(20,1)), sg.InputText(key = 'senha')],
                    [sg.Submit(), sg.Cancel()]
                ]
        self.__window = sg.Window('Edição de Clientes').Layout(layout)
        self.open()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
