import requests
import time

# odgovor = requests.get('https://rtvslo.si', timeout=2)
# odgovor.status_code #(to mi pove, če je vse v redu, npr. error 404, če česa ni našel, vrnit more 200)
# odgovor.text ()
HEADERS = {"User-Agent": "Mozilla/5.0"}


odgovor = requests.get(f"https://volitve.dvk-rs.si/dz2026/#/rezultati", headers=HEADERS)

print(odgovor.status_code)

vsebina = odgovor.text

with open(f"teorija\\volitve\\DZ2026.html", "w", encoding="UTF-8") as dat:
    dat.write(vsebina)

time.sleep(2)
