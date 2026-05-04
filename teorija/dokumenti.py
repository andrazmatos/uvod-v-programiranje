# dat = open('krst-pri-savici.txt')
# dat.--------

def prestej_besede(ime_datoteke):
    besede = {}
    dat = open(ime_datoteke)

    for vrstica in dat:
        besede_v_vrstici = vrstica.split(' ')
        for beseda in besede_v_vrstici:
            beseda = beseda.replace(',','')
            beseda = beseda.replace('.','')
            beseda = beseda.replace('!','')
            beseda = beseda.replace('\n','')
            beseda = beseda.replace('?','')
            beseda = beseda.replace(':','')
            beseda = beseda.replace(';','')
            beseda = beseda.replace('-','')

            beseda = beseda.lower()
            if beseda not in besede:
                besede[beseda] = 1
            else: besede[beseda] +=1
    dat.close

    return besede


def prepisi_na_glas(ime_datoteke, nova_datoteka):
    with open(ime_datoteke, 'r', encoding='utf-8') as dat:
        with open(nova_datoteka, 'w', encoding='utf-8') as dat2:
            vsebina = dat.read()
            vsebina = vsebina.upper()

            dat2.write(vsebina)
