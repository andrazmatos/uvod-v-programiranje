import json

dat = open("teorija\\volitve\\2026\\data2026.json", "r", encoding="utf-8")
podatki = json.load(dat)
dat.close()


# legenda, kateri id pripada kateri stranki
legenda = {}
for i in podatki["slovenija"]["rez"]["rez"]:
    stranka = i["knaz"]
    id_stranke = i["st"]
    legenda[stranka] = id_stranke


# podatki za celo Slovenijo
rezultati = {}
for i in podatki["slovenija"]["rez"]["rez"]:
    procenti = i["prc"]
    id_stranke = i["st"]
    rezultati[id_stranke] = procenti

with open(
    "teorija\\volitve\\2026\\data.py", "w", encoding="utf-8"
) as podatkovna_datoteka:

    podatkovna_datoteka.write(f"legenda = {legenda},\n\nrezultati = {rezultati},\n\n")

# podatki o glasovih v posamezni enoti in po okraju:

with open(
    "teorija\\volitve\\2026\\data.py", "a", encoding="utf-8"
) as podatkovna_datoteka:
    podatkovna_datoteka.write("rez = {\n")
    for enota in range(8):
        for okraj in range(11):
            stevilka_okraja = podatki["slovenija"]["enote"][enota]["okraji"][okraj][
                "rpeid"
            ]
            seznam_rezultatov = podatki["slovenija"]["enote"][enota]["okraji"][okraj][
                "rez"
            ]["rez"]
            seznam_rezultatov.insert(0, stevilka_okraja)
            podatkovna_datoteka.write(
                f"'podatki_2026_{stevilka_okraja}' : {seznam_rezultatov},\n"
            )
        podatkovna_datoteka.write("\n\n\n")
    podatkovna_datoteka.write("}")

dat = open("teorija\\volitve\\2026\\rezultati2026.csv", "w", encoding="utf-8")

import data
import csv

tabela = csv.writer(dat)

tabela.writerow(
    ["OKRAJ"] + list(legenda.keys())
)  # pri tej dotični vrsti sem si pomagal z AI

for key in data.rez:
    tabela.writerow(
        [
            data.rez[key][0],
            data.rez[key][1]["prc"],
            data.rez[key][2]["prc"],
            data.rez[key][3]["prc"],
            data.rez[key][4]["prc"],
            data.rez[key][5]["prc"],
            data.rez[key][6]["prc"],
            data.rez[key][7]["prc"],
            data.rez[key][8]["prc"],
            data.rez[key][9]["prc"],
            data.rez[key][10]["prc"],
            data.rez[key][11]["prc"],
            data.rez[key][12]["prc"],
            data.rez[key][13]["prc"],
            data.rez[key][14]["prc"],
            data.rez[key][15]["prc"],
        ]
    )

dat.close()
