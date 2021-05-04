import PySimpleGUI as sg 
from src.windows import leyout
from src.handlers import handler2uno
from src.handlers import handler2dos
from src.handlers import handler2tres

def start2():
    """
    Ejecucion del menu data 2
    """
    window = loop_menuData2()
    window.close()


def loop_menuData2():
    """
    Loop del menu configuracion
    """
    window = leyout.data2()

    while True:
        event, _values = window.read()

        if event in ( "Salir", "-exit-"):
            break

        if event == "-accpor-":
            handler2uno.dieciseis()

        if event == "-arg-":
            handler2dos.argen()

        if event == "-treinta-":
            handler2tres.topVeinte()

    return window