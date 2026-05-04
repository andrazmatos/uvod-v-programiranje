sez = ['sda','swwdewfere','fghjkuz']
print(sorted(sez, key=len))
    # key=len, len je funkcija, ki jo lahko podam, na podlagi katerga mi razporedi seznam
    # lahko definiram novo funckijo

def minus_len(niz):
    return -len(niz)
print(sorted(sez, key=minus_len))
print(sorted(sez, key=len))

### SLOVARJI

slovar = {'knjiga':'book', 'hisa':'house'}

# slovar['avto'] = 'car'
# len(slovar)
# del slovar('hisa) -- izbriše ta vnos


def prestej_znake(niz):
    pojavitve = {}
    for znak in niz:
        if znak not in pojavitve:
            pojavitve[znak] = 1
        else:
            pojavitve[znak] += 1
    return pojavitve
 
niz = '''Los 27 países de la Unión Europea (UE) han aprobado una enmienda para prohibir los servicios de inteligencia artificial que generen imágenes sexuales o desnuden fotografías de personas reales. Por el momento, esta es únicamente la posición de los Gobiernos, que deberán consensuarla con el Parlamento Europeo.

Esta medida llega tras la polémica generada por la herramienta Grok, que permitió a sus usuarios generar millones de imágenes de este tipo en apenas unos días. La red social desarrollada por X anunció posteriormente medidas para restringir esta actividad, y la Comisión Europea mantiene abierta una investigación al respecto. Sin embargo, los legisladores podrían ahora ir más allá.'''

def matrika_v_seznam(mat):
    mat_slovar = {}

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                continue
            mat_slovar[(i,j)] = mat[i][j]
    return (mat_slovar, len(mat), len(mat[0]))

def matrika_slovar_v_seznam(mat_slovar, n, m):
    matrika = []
    for _ in range(n):
        matrika.append(m*[0])

    for  kljuc, vrednost in mat_slovar.items():
        i, j = kljuc
        matrika[i][j] = vrednost
    return matrika

# slovar = [i: i**2 for i in range(100)]

