def topTenmas():
    import json
    import csv
    archivo = open("Top 10 paises con mayor esperanza de vida en 2019.json","w")
    with open(r'C:/Users/marti/Desktop/actividaduno/life-expectancy.csv', newline='') as f:
        reader = csv.reader(f)
        dataL = list(reader)  #proceso el csv en una lista

    dataOr=[]
    topTen=[]
    a=len(dataL)

    for i in range(a):
        if (dataL[i][2]=='2019'):
            dataOr.append(dataL[i])     #selecciono en la lista solo el año 2019

    dataOr=sorted(dataOr, key=lambda dataOr : dataOr[3],reverse=True) #ordeno la lista por mayor % 



    for i in range(10):
        topTen.append(dataOr[i])

    archivo.write(json.dumps(topTen))
