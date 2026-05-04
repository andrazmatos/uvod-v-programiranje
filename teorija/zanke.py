def druga_zanka(n):
    stevec = n
    while stevec >0:
        print (stevec*'*')
        stevec = stevec - 1

def tretja(n):
    stevec = 0
    while True:
        while stevec < n:
            print(stevec*'°')
            stevec += 1
        while stevec >=0:
            print(stevec*'°')
            stevec -= 1

def schv(x):
    vsota = 0
    i=1
    while vsota <= x:
        vsota += 1/i
        i += 1
        print(i)
    return i - 1

def for_zanka(niz):
    for crka in niz:
        print(f'{crka}')

def fakulteta1(n):
    i=1
    produkt =1
    while i<=n:
        produkt = produkt*i
        i+=1
    return produkt

def fakulteta2(n):
    produkt =1
    for i in range(1, n+1):
        produkt *= i
        i+=1
    return produkt

def zamenjava(niz):
    nov_niz=''
    for crka in niz:
        if crka in 'aeiouAEIOU':
            nov_niz = nov_niz +'?'
        if crka in 'l':
            nov_niz = nov_niz + '!'
        else:
            nov_niz += crka
    return nov_niz

import math
def sinzero(a, b, epsilon=1e-10):
    while b - a > epsilon:
        sredina = (a+b)/2
        if math.sin(a) ==0:
            return a
        if math.sin(b) ==0:
            return b
        if math.sin(sredina) ==0:
            return sredina
        if math.sin(a)*math.sin(sredina) > 0:
            a, b = sredina, b
        else:
            a, b = a, sredina
    return sredina