

def dieciseis():
    import json
    import csv

    archivo = open("Porcentaje mundial de acceso a la electricidad en el año 2016.json","w")

    archivo_csv = open(r'C:/Users/marti/Desktop/actividaduno/share-of-the-population-with-access-to-electricity.csv')

    data={}
    reader=csv.DictReader(archivo_csv)
    for dicc in reader:
        key=dicc['Entity']
        data[key]=dicc
    archivo.write(json.dumps(data, indent=4))


















