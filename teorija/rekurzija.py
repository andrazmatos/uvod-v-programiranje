def prva_rekurzija():
    print(42)

def stevila_padajoce(n):
    """funkcija izpiše prvih n števil v padajočem vrstnem redu"""
    if n == 0:
        return
    else:
        print(n)
        stevila_padajoce(n-1)


def fakulteta(n):
    if n<=1 and n>=0:
        return 1
    else:
        return n*fakulteta(n-1)
    

def gcd(m,n):
    if m%n == 0:
        return n
    ostanek = m%n 
    return gcd(n, ostanek)

def fibonacci(n):
    if n==0 or n==1:
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)
    
def posploseni_fibonacci(n,a,b):
    if n==1:
        return b
    if n==0:
        return a
    return posploseni_fibonacci(n-1, b, a+b)

def param(x,y=1,z=2):
    print(x, y, z)
def vks(xyz):
    return x**2+y**2+z**2

def inverse_fakulteta(n):
    return n/(fakulteta(n-1))