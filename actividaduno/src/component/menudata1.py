import PySimpleGUI as sg 
from src.windows import leyout
from src.handlers import handler1uno
from src.handlers import handler1dos
from src.handlers import handler1tres
def start1():
    """
    Ejecucion del menu configuracion
    """
    window = loop_menuData1()
    window.close()


def loop_menuData1():
    """
    Loop del menu configuracion
    """
    window = leyout.data1()

    while True:
        event, _values = window.read()

        if event in ( "Salir", "-exit-"):
            break

        if event == "-maev-":
            handler1uno.topTenmas()

        if event == "-meev":
            handler1dos.topTenmenos()

        if event == "-ma70-":
            handler1tres.setenta()
    return window
