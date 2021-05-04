import PySimpleGUI as sg



def menu():
    """
    Construye la ventana del menu
    """
    layout = [
             [sg.Text('Que Datos Analizamos?',text_color='Dark Blue',background_color=('Light Grey'))],    
        [sg.Button('Esperanza de vida ',size=(25, 2),key="-data1-",button_color=('Grey'))],
        [sg.Button('Acceso a la tecnologia', size=(25, 2), key="-data2-",button_color=('Grey'))],

        [sg.Button('SALIR', size=(25, 2), key="-exit-",button_color=('Grey'))],
    ]

    board = sg.Window('Actividad 1 x Python Plus -TEORIA-',margins=(100,100),no_titlebar = True,background_color=('Light Grey')).Layout(layout)

    return board


def data1():
    layout = [
             [sg.Text('Elige que opcion analizar',text_color='Dark Blue',background_color=('Light Grey'))],
        [sg.Button('Top 10 paises con mayor esperanza de vida en 2019',size=(25, 2),key="-maev-",button_color=('Grey'))],
        [sg.Button('Top 10 paises con menor esperanza de vida en 2019', size=(25, 2), key="-meev",button_color=('Grey'))],
        [sg.Button('Paises con esperanza de vida mayor a 70 años de 2015', size=(25, 2), key="-ma70-",button_color=('Grey'))],
        [sg.Button('SALIR', size=(25, 2), key="-exit-")],
    ]

    boardata1 = sg.Window('Esperanza de vida',margins=(100,100),no_titlebar = True,background_color=('Light Grey')).Layout(layout)

    return boardata1



def data2():
    layout = [
             [sg.Text('Elige que opcion analizar',text_color='Dark Blue',background_color=('Light Grey'))],
        [sg.Button('Porcentaje mundial de acceso en el año 2016',size=(25, 2),key="-accpor-",button_color=('Grey'))],
        [sg.Button('Porcentaje de acceso en Argentina  2000-2015', size=(25, 2), key="-arg-",button_color=('Grey'))],
        [sg.Button('Top 10 paises con mayor acceso, año 1975',size=(25, 2),key="-treinta-",button_color=('Grey'))],
        [sg.Button('SALIR', size=(25, 2), key="-exit-")],
    ]

    boardata2 = sg.Window('Acceso a la electricidad',margins=(100,100),no_titlebar = True,background_color=('Light Grey')).Layout(layout)
    return boardata2

