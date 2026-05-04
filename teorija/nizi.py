def srednja_crka(niz):
    sredina = len(niz)//2
    if len(niz) % 2 == 1:
        return niz[sredina]
    else:
        return niz[sredina-1:sredina+1]


def je_samoglasnik(crka):
    if crka in "aeiouAEIOU":
        return True
    else:
        return False
    
def stevilo_samoglasnikov(niz):
    stevilo = 0
    if niz == "":
        return 0
    if je_samoglasnik(niz[0]):
        stevilo = stevilo + 1
    
    stevilo += stevilo_samoglasnikov(niz[1:])
    return stevilo

def narisi_crtice(n):
    if n==0:
        return
    else:
        print(n*"|")
        narisi_crtice(n-1)
    
