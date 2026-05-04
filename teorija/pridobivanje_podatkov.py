# pip install requests (v GITu)
import requests
import time

# odgovor = requests.get('https://rtvslo.si', timeout=2)
# odgovor.status_code #(to mi pove, če je vse v redu, npr. error 404, če česa ni našel, vrnit more 200)
# odgovor.text ()
HEADERS = {'User-Agent': 'Mozilla/5.0'}



for i in range(1, 6): #prvih 5 strani na GoodReads seznamu, ker drugače vzame samo 1 
    odgovor = requests.get(f'https://www.goodreads.com/list/show/1.Best_Books_Ever?page={i}', headers=HEADERS)

    print(odgovor.status_code)

    vsebina = odgovor.text

    with open(f'teorija\\htmlji\\stran{i}.html', 'w', encoding='UTF-8') as dat:
        dat.write(vsebina)

    time.sleep(2) #spi 2 sekundi, preden spet narediš zanko

# vzorec = 'nek regularni izraz brez '' '
# knjige = []

# for i in range(1, 6):
#     with open(f'htmlji/stran{i}.html') as dat:
#         vsebina = dat.read()

#         for najdba in vzorec.finditer(vsebina):
#             knjige.append(
#                 {
#                     'naslov': najdba['naslov'],
#                     'povezava': najdba['link'],
#                     'id': najdba ['id_knjige'],
#                 }
#             )

# print (knjige)

# 'kako pa to shranim nekam'

# import json

# dat = open('knjige.json', 'w')
# json.dump(knjige, dat) #kaj je razlika med json.dump in json.load
# dat.close()

# ' kaj pa kot CSV'

# dat = open('knjige.csv', 'w')
# import csv
# pisatelj = csv.writer(dat)
# pisatelj.writerow(
#     [
#         'jezik',
#         'avtor',
#         'ocena'
#     ]
# )
# for knjiga in knjige:
#     pisatelj.writerow([knjiga['jezik'], knjiga['avtor'], knjiga['ocena']])

# dat.close()