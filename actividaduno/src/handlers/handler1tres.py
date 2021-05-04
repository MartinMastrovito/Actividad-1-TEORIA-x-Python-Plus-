def setenta():
    import json
    import csv

    archivo = open("Paises con esperanza de vida mayor a 70 años de 2015.json","w")

    archivo_csv = open(r'C:/Users/marti/Desktop/actividaduno/life-expectancy.csv')

    data=[]
    reader=csv.DictReader(archivo_csv)
    for dicc in reader:
        if(dicc['Life expectancy']>'70')&(dicc['Year']=='2015'):
            data.append(list(zip(dicc.keys(),dicc.values())))
    archivo.write(json.dumps(data))

