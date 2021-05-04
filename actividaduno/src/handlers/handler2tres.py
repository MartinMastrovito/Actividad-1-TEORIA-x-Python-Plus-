 
def topVeinte():
    import json
    import csv
    archivo = open("Top 20 paises con menor acceso, año 1999.json","w")
    with open(r'C:/Users/marti/Desktop/actividaduno/share-of-the-population-with-access-to-electricity.csv', newline='') as f:
        reader = csv.reader(f)
        dataL = list(reader)  #proceso el csv en una lista

    dataOr=[]
    topTen=[]
    a=len(dataL)

    for i in range(a):
        if (dataL[i][2]=='1999')&(dataL[i][3]!='100'):
            dataOr.append(dataL[i])     #selecciono en la lista solo el año 1999

    dataOr=sorted(dataOr, key=lambda dataOr : dataOr[3]) #ordeno la lista por menor % en el año 1999



    for i in range(10):
        topTen.append(dataOr[i])

    archivo.write(json.dumps(topTen))

