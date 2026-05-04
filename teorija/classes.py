class AritmeticnoZaporedje:
    def __init__(self, zacetni_clen, razlika):
        self.zacetni_clen = zacetni_clen
        self.razlika = razlika

    def n_ti_clen(self, n):
        return self.zacetni_clen + n*self.razlika
    
    def vsota(self, n):
        return (n+1)*self.zacetni_clen + (n*(n+1)/2)*self.razlika
    
    def __add__(self, drugo_zap):
        return AritmeticnoZaporedje(self.zacetni_clen + drugo_zap, self.razlika + drugo_zap.razlika)
    
    def __repr__(self):
        return f'Zaporedje: {self.zacetni_clen}, {self.zacetni_clen + self.razlika} ...'
    
    def __contains__(self, clen):
        ostanek = (clen - self.zacetni_clen)%self.razlika
        delitelj = (clen - self.zacetni_clen) // self.razlika

####### ULOMKI
def gcd(n, m):
        i = 1
        if m>n:
         n, m = m, n 
        for l in range(m+1):
            if l == 0:
                l += 1
            if n % (l) == 0 and m%l == 0:
                i = l
        return i

class Ulomek:
    def __init__(self, stevec, imenovalec):
        self.im = imenovalec
        self.st = stevec
    
    def __mul__(self, other):
        return Ulomek(self.st * other.st, self.im * other.im)
    
    def __add__(self, other):
        
        st = self.st*other.im + self.im*other.st
        im = self.im * other.im
        return Ulomek(st, im)
    
    def __iter__(self):
        i = 0
        while True:
            yield self[i]
            i += 1

    def prastevila():
        sez = []
        i = 2
        while True:
            je_prastevilo = True
            for j in sez:
                if i % j == 0:
                    je_prastevilo = False
                    break
            if je_prastevilo:
                yield i
                sez.append(i)
            i += 1

                
            
   