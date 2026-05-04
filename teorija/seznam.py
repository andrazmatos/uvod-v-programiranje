matrika = [[1, 0, 1], [2, 7, 9], [2, 4, 5]]

def najvecji_element_matrike(mat):
    maksimum = none
    for vrstica in mat:
        for el in vrstica:
            if maksimum== none or el > maksimum:
                maksimum = el
    return maksimum
list = [1,23, 54, 654, 876,42,323,5,9]
def index_najvecjega(sez):
    maksimum = None
    index = None
    for i in range(len(sez)):
        if maksimum == None or sez[i] > maksimum:
            maksimum = sez[i]
            index = i
    return index

def tr(mat):
    sled = 0
    for i in range(len(mat[0])):
        sled += mat[i][i]
    return sled

def sodi_el(sez):
    nov_sez = []
    for el in sez:
        if el % 2 == 0:
            nov_sez.append(el)
    return nov_sez