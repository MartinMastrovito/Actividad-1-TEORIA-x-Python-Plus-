import PySimpleGUI as sg
from src.windows import leyout
from src.component import menudata1
from src.component import menudata2

def start():
    """
    Ejecucion del menu principal
    """
    window = loop_menu()
    window.close()


def loop_menu():
    """
    Loop del menu principal
    """
    window = leyout.menu()

    while True:
        event, _values = window.read()

        if event in ( "Exit", "-exit-"):
            break

        if event == "-data1-":
            window.hide()
            menudata1.start1()
            window.un_hide()


        if event == "-data2-":
            window.hide()
            menudata2.start2()
            window.un_hide()
    return window

