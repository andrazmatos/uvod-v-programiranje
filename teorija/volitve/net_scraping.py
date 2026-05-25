import requests
import time

# odgovor = requests.get('https://rtvslo.si', timeout=2)
# odgovor.status_code #(to mi pove, če je vse v redu, npr. error 404, če česa ni našel, vrnit more 200)
# odgovor.text ()
HEADERS = {"User-Agent": "Chrome/148.0.7778.97"}

# DRŽAVNOZBORSKE VOLITVE 2000
for i in range(1,9):
    odgovor = requests.get(f"https://www.dvk-rs.si/arhivi/dz2000/rez_vo{i}.html", headers=HEADERS)

    print(f"2000_{i}", odgovor.status_code)

    vsebina = odgovor.text

    with open(f"teorija\\volitve\\2000\\VO_{i}.html", "w", encoding="UTF-8") as dat:
        dat.write(vsebina)

    time.sleep(2)

# DRŽAVNOZBORSKE VOLITVE 2004
for i in range(1,9):
    odgovor = requests.get(f"https://www.dvk-rs.si/arhivi/dz2004/html/rez_vo{i}.html", headers=HEADERS)
    print(f"2004_{i}", odgovor.status_code)
    vsebina = odgovor.text

    with open(f"teorija\\volitve\\2004\\VO_{i}.html", "w", encoding="UTF-8") as dat:
        dat.write(vsebina)

    time.sleep(2)

# DRŽAVNOZBORSKE VOLITVE 2008
for i in range(1,9):
    odgovor = requests.get(f"https://www.dvk-rs.si/arhivi/dz2008/rezultati/rez_vo{i}.html", headers=HEADERS)

    print(f"2008_{i}", odgovor.status_code)
    vsebina = odgovor.text

    with open(f"teorija\\volitve\\2008\\VO_{i}.html", "w", encoding="UTF-8") as dat:
        dat.write(vsebina)

    time.sleep(2)

# DRŽAVNOZBORSKE VOLITVE 2011
for i in range(1,9):
    odgovor = requests.get(f"https://www.dvk-rs.si/arhivi/dz2011/rezultati/rez_vo{i}.html", headers=HEADERS)
    print(f"2011_{i}", odgovor.status_code)
    vsebina = odgovor.text

    with open(f"teorija\\volitve\\2011\\VO_{i}.html", "w", encoding="UTF-8") as dat:
        dat.write(vsebina)

    time.sleep(2)

# DRŽAVNOZBORSKE VOLITVE 2014
for i in range(1,9):
    odgovor = requests.get(f"https://www.dvk-rs.si/arhivi/dz2014/rezultati/rez_vo{i}.html", headers=HEADERS)
    print(f"2014_{i}", odgovor.status_code)
    vsebina = odgovor.text

    with open(f"teorija\\volitve\\2014\\VO_{i}.html", "w", encoding="UTF-8") as dat:
        dat.write(vsebina)

    time.sleep(2)