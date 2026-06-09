# Python Reference Manual (FMF – Uvod v programiranje)

## Table of Contents

1. Basic Types
2. Strings (`str`)
3. Lists (`list`)
4. Tuples (`tuple`)
5. Sets (`set`)
6. Dictionaries (`dict`)
7. Functions
8. Loops
9. Comprehensions
10. Classes
11. Files
12. Exceptions
13. Regular Expressions
14. Common Exam Traps

---

# Slovenian ↔ English Terminology

| Slovenian | English | Python Type |
|------------|------------|------------|
| niz | string | str |
| seznam | list | list |
| nabor | tuple | tuple |
| množica | set | set |
| slovar | dictionary | dict |
| razred | class | class |
| objekt | object / instance | object |
| atribut | attribute | attribute |
| metoda | method | method |
| funkcija | function | function |
| zanka | loop | loop |
| datoteka | file | file |
| izjema | exception | exception |

# 1. Basic Types

```python
type(5)
# int

type(3.14)
# float

type(True)
# bool

type("abc")
# str

type([1,2,3])
# list

type((1,2,3))
# tuple

type({1,2,3})
# set

type({"a":1})
# dict
```

---

# 2. Niz | Strings (`str`)

Strings are immutable.

```python
s = "Programiranje"
```

## Length

```python
len(s)
# 12
```

## Indexing

```python
s[0]
# 'P'

s[-1]
# 'e'
```

## Slicing

```python
s[2:6]
# 'ogra'

s[:4]
# 'Prog'

s[4:]
# 'ramiranje'

s[::-1]
# 'ejnarimargorP'
```

## Membership

```python
"mir" in s
# True

"x" in s
# False
```

## Methods

### upper

```python
s.upper()
# 'PROGRAMIRANJE'
```

### lower

```python
s.lower()
# 'programiranje'
```

### replace

```python
s.replace("a","X")
# 'ProgrXmirXnje'
```

### count

```python
s.count("r")
# 3
```

### find

```python
s.find("mir")
# 6

s.find("xyz")
# -1
```

### split

```python
"a,b,c".split(",")
# ['a','b','c']

"ana bor cilka".split()
# ['ana','bor','cilka']
```

### join

```python
"-".join(["a","b","c"])
# 'a-b-c'
```

---

# 3. Seznami | Lists (`list`)

Lists are mutable.

```python
L = [10,20,30]
```

## Indexing

```python
L[0]
# 10

L[-1]
# 30
```

## Slicing

```python
L[1:]
# [20,30]
```

## append

```python
L.append(40)

L
# [10,20,30,40]
```

Important:

```python
x = L.append(50)

print(x)
# None
```

## insert

```python
L.insert(1,99)

L
# [10,99,20,30]
```

## remove

```python
L.remove(20)

L
# [10,30]
```

## pop

```python
L = [10,20,30]

L.pop()
# 30

L
# [10,20]
```

## sort

```python
L = [3,1,4,2]

L.sort()

L
# [1,2,3,4]
```

## sorted

```python
L = [3,1,4,2]

sorted(L)
# [1,2,3,4]

L
# [3,1,4,2]
```

## reverse

```python
L.reverse()
```

## count

```python
[1,1,2,3].count(1)
# 2
```

## index

```python
[10,20,30].index(20)
# 1
```

---

# 4. Nabori | Tuples (`tuple`)

Immutable sequence.

```python
T = (1,2,3)
```

## Access

```python
T[0]
# 1
```

## count

```python
(1,1,2).count(1)
# 2
```

## index

```python
(5,7,9).index(7)
# 1
```

## Unpacking

```python
a,b,c = (1,2,3)

a
# 1
```

### Single-element tuple

```python
(5,)
# tuple

(5)
# int
```

---

# 5. Množice | Sets (`set`)

Unique elements only.

```python
A = {1,2,3}
```

## add

```python
A.add(4)
```

## remove

```python
A.remove(2)
```

## discard

```python
A.discard(100)
```

## Union

```python
{1,2} | {2,3}
# {1,2,3}
```

## Intersection

```python
{1,2} & {2,3}
# {2}
```

## Difference

```python
{1,2,3} - {2}
# {1,3}
```

---

# 6. Slovarji | Dictionaries (`dict`)

Key-value pairs.

```python
D = {
    "ime":"Ana",
    "starost":20
}
```

## Access

```python
D["ime"]
# 'Ana'
```

## get

```python
D.get("ime")
# 'Ana'

D.get("naslov")
# None
```

## Add

```python
D["smer"] = "FMF"
```

## Delete

```python
del D["starost"]
```

## keys

```python
list(D.keys())
# ['ime','starost']
```

## values

```python
list(D.values())
# ['Ana',20]
```

## items

```python
list(D.items())
# [('ime','Ana'),('starost',20)]
```

---

# 7. Useful Functions

## len

```python
len("abc")
# 3

len([1,2,3])
# 3
```

## sum

```python
sum([1,2,3])
# 6
```

## min

```python
min([5,1,8])
# 1
```

## max

```python
max([5,1,8])
# 8
```

## sorted

```python
sorted([3,1,2])
# [1,2,3]
```

---

# 8. Loops

## range

```python
list(range(5))
# [0,1,2,3,4]
```

```python
list(range(2,10,3))
# [2,5,8]
```

## enumerate

```python
list(enumerate("abc"))
# [(0,'a'),(1,'b'),(2,'c')]
```

Important:

```python
for i, x in enumerate("abc"):
    print(i, x)
```

Output:

```text
0 a
1 b
2 c
```

## zip

```python
list(zip(["Ana","Bor"], [10,9]))
# [('Ana',10),('Bor',9)]
```

## break

Stops loop immediately.

## continue

Skips current iteration.

---

# 9. Comprehensions

## List comprehension

```python
[x*x for x in range(5)]
# [0,1,4,9,16]
```

```python
[x for x in range(10) if x % 2 == 0]
# [0,2,4,6,8]
```

## Dictionary comprehension

```python
{x:x*x for x in range(4)}
# {0:0,1:1,2:4,3:9}
```

## Set comprehension

```python
{x*x for x in range(5)}
# {0,1,4,9,16}
```

---

# 10. Classes (Razredi)

A class is a blueprint for creating objects.

A class describes:
- what data an object stores (attributes)
- what an object can do (methods)

Example:

```python
class Student:
    pass
```

This creates a class but no students yet.

---

## Creating Objects

```python
class Student:
    pass

s = Student()
```

Here:

```python
type(s)
# __main__.Student
```

`Student` is the class.

`s` is an object (instance).

---

## Attributes

Attributes store data inside an object.

```python
class Student:
    pass

s = Student()

s.ime = "Ana"
s.starost = 20
```

Access:

```python
s.ime
# 'Ana'

s.starost
# 20
```

---

## Constructor (__init__)

The constructor runs automatically when creating an object.

```python
class Student:

    def __init__(self, ime):
        self.ime = ime
```

Create object:

```python
s = Student("Ana")
```

Result:

```python
s.ime
# 'Ana'
```

---

## Understanding self

Most important class concept.

```python
class Student:

    def __init__(self, ime):
        self.ime = ime
```

When Python executes:

```python
s = Student("Ana")
```

it effectively does:

```python
Student.__init__(s, "Ana")
```

Therefore:

```python
self
```

is the current object.

---

## Multiple Attributes

```python
class Student:

    def __init__(self, ime, letnik):
        self.ime = ime
        self.letnik = letnik
```

Create:

```python
s = Student("Ana", 1)
```

Result:

```python
s.ime
# 'Ana'

s.letnik
# 1
```

---

## Methods

Methods are functions belonging to an object.

```python
class Student:

    def __init__(self, ime):
        self.ime = ime

    def pozdravi(self):
        print("Pozdravljen,", self.ime)
```

Usage:

```python
s = Student("Ana")

s.pozdravi()
```

Output:

```text
Pozdravljen, Ana
```

---

## Methods Returning Values

```python
class Student:

    def __init__(self, ime):
        self.ime = ime

    def pozdrav(self):
        return f"Pozdravljen, {self.ime}"
```

Usage:

```python
s.pozdrav()
# 'Pozdravljen, Ana'
```

---

## Modifying Attributes

```python
class Student:

    def __init__(self, ime):
        self.ime = ime
```

```python
s = Student("Ana")

s.ime = "Bor"
```

Result:

```python
s.ime
# 'Bor'
```

---

## Counter Example

```python
class Stevec:

    def __init__(self):
        self.vrednost = 0

    def povecaj(self):
        self.vrednost += 1
```

Usage:

```python
s = Stevec()

s.vrednost
# 0

s.povecaj()

s.vrednost
# 1
```

Again:

```python
s.povecaj()

s.vrednost
# 2
```

---

## Bank Account Example

```python
class Racun:

    def __init__(self):
        self.stanje = 0

    def polog(self, znesek):
        self.stanje += znesek
```

Usage:

```python
r = Racun()

r.stanje
# 0

r.polog(100)

r.stanje
# 100
```

---

## __str__()

Controls what print() displays.

Without:

```python
class Student:

    def __init__(self, ime):
        self.ime = ime

s = Student("Ana")

print(s)
```

Output:

```text
<__main__.Student object at 0x...>
```

With:

```python
class Student:

    def __init__(self, ime):
        self.ime = ime

    def __str__(self):
        return self.ime
```

Usage:

```python
s = Student("Ana")

print(s)
```

Output:

```text
Ana
```

---

## Lists of Objects

```python
class Student:

    def __init__(self, ime):
        self.ime = ime
```

```python
studenti = [
    Student("Ana"),
    Student("Bor"),
    Student("Cilka")
]
```

Loop:

```python
for s in studenti:
    print(s.ime)
```

Output:

```text
Ana
Bor
Cilka
```

---

## Typical Exam Example

```python
class Pravokotnik:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ploscina(self):
        return self.a * self.b

    def obseg(self):
        return 2*self.a + 2*self.b
```

Usage:

```python
p = Pravokotnik(3, 4)

p.ploscina()
# 12

p.obseg()
# 14
```

---

## Common Mistakes

### Forgetting self

Wrong:

```python
class Student:

    def __init__(ime):
        self.ime = ime
```

Correct:

```python
class Student:

    def __init__(self, ime):
        self.ime = ime
```

---

### Forgetting self.

Wrong:

```python
class Student:

    def __init__(self, ime):
        ime = ime
```

Correct:

```python
class Student:

    def __init__(self, ime):
        self.ime = ime
```

---

### Forgetting ()

Wrong:

```python
s.pozdrav
```

Output:

```text
<bound method ...>
```

Correct:

```python
s.pozdrav()
# 'Živjo'
```

---

## Minimal Template To Memorize

```python
class ImeRazreda:

    def __init__(self, x):
        self.x = x

    def metoda(self):
        return self.x
```

Usage:

```python
obj = ImeRazreda(5)

obj.x
# 5

obj.metoda()
# 5
```
---

# 11. Files

Suppose file contains:

```text
Ana
Bor
Cilka
```

## Read all

```python
with open("imena.txt") as f:
    vse = f.read()
```

## Read lines

```python
with open("imena.txt") as f:
    vrstice = f.readlines()

vrstice
# ['Ana\n','Bor\n','Cilka\n']
```

## Iterate line by line

```python
with open("imena.txt") as f:
    for vrstica in f:
        print(vrstica)
```

---

# 12. Exceptions

```python
try:
    x = 1/0
except ZeroDivisionError:
    print("Napaka")
```

Output:

```text
Napaka
```

---

# 13. Regular Expressions

```python
import re
```

## search

```python
re.search(r"\d+", "abc123")
```

Matches:

```text
123
```

## findall

```python
re.findall(r"\d+", "a12b34")
# ['12','34']
```

## groups

```python
m = re.search(r"(\d+)-(\d+)", "12-34")

m.group(1)
# '12'

m.group(2)
# '34'
```

---

# 14. Common Exam Traps

```python
[1,2,3] * 3
# [1,2,3,1,2,3,1,2,3]
```

```python
"abc" * 3
# 'abcabcabc'
```

```python
[1,2] + [3,4]
# [1,2,3,4]
```

```python
"abc" + "def"
# 'abcdef'
```

```python
list("abc")
# ['a','b','c']
```

```python
''.join(['a','b','c'])
# 'abc'
```

```python
len({1,1,1,2,2})
# 2
```

```python
dict(a=1,b=2)
# {'a':1,'b':2}
```

```python
bool([])
# False

bool("")
# False

bool({})
# False

bool([1])
# True
```

```python
None == False
# False
```

```python
None is None
# True
```
