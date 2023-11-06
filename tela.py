import PySimpleGUI as sg


class Tela:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
                    [sg.Text('Incluir novo Cliente')],
                    [sg.Text('Nome', size=(20,1)), sg.InputText(key= 'nome', size= (10,1))],
                    [sg.Text('Usuario', size=(20,1)), sg.InputText(key= 'usuario')],
                    [sg.Text('Senha', size=(20,1)), sg.InputText(key = 'senha')],
                    [sg.Submit(), sg.Cancel()]
                ]
        self.__window = sg.Window('Cadastro de Clientes').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)