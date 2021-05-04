 
def argen():
    import json
    import csv

    archivo = open("Porcentaje de acceso a la energia Argentina 2000-2015.json","w")

    archivo_csv = open(r'C:/Users/marti/Desktop/share-of-the-population-with-access-to-electricity.csv')

    data=[]
    reader=csv.DictReader(archivo_csv)
    for dicc in reader:
        if(dicc['Entity']=='Argentina')&(dicc['Year']>='2000')&(dicc['Year']<='2015'):
            data.append(list(zip(dicc.keys(),dicc.values())))
    archivo.write(json.dumps(data))


