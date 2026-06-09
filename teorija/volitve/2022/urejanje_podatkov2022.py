import json

dat = open("2022\\data2022.json", "r", encoding="utf-8")
podatki = json.load(dat)
dat.close()


# legenda, kateri id pripada kateri stranki
# Velik problem imamo, ker dve stranki, ZSI in ZOS nista kandidirali v vseh okrajih, ampak samo v določenih, zato dolžina slovarjev ni enaka za vse okraje. Ker sta stranki skupaj prejeli manj kot 0.07% glasov, jih bomo izbrisali iz podatkov.

legenda = {}
for i in podatki["slovenija"]["rez"]["rez"]:
    if i["knaz"] in ["ZSi", "ZOS"]:
        pass
    else:
        stranka = i["knaz"]
        id_stranke = i["st"]
        legenda[stranka] = id_stranke
print(legenda)


# podatki za celo Slovenijo
rezultati_cela_slovenija = {}
for i in podatki["slovenija"]["rez"]["rez"]:
    if i["knaz"] in ["ZSi", "ZOS"]:
        pass
    else:
        procenti = i["prc"]
        id_stranke = i["st"]
        rezultati_cela_slovenija[f"{id_stranke}"] = procenti
print(rezultati_cela_slovenija)


with open("2022\\data.py", "w", encoding="utf-8") as podatkovna_datoteka:

    podatkovna_datoteka.write(
        f"legenda = {legenda}\n\nrezultati_cela_slovenija = {rezultati_cela_slovenija}\n\n"
    )

# podatki o glasovih v posamezni enoti in po okraju

with open("2022\\data.py", "a", encoding="utf-8") as podatkovna_datoteka:
    podatkovna_datoteka.write("rez = {\n")
    for enota in range(8):
        for okraj in range(11):
            stevilka_okraja = (enota + 1) * 1000 + podatki["slovenija"]["enote"][enota][
                "okraji"
            ][okraj]["st"]
            seznam_rezultatov = podatki["slovenija"]["enote"][enota]["okraji"][okraj][
                "rez"
            ]["rez"]
            seznam_rezultatov.insert(0, stevilka_okraja)  # pomagal z AI
            podatkovna_datoteka.write(
                f"'podatki_2022_{stevilka_okraja}' : {seznam_rezultatov},\n"
            )
        podatkovna_datoteka.write("\n\n\n")
    podatkovna_datoteka.write("}")

# Sedaj smo pred velikim izzivom. V datoteki data.py imamo slovar 'rez', v katerem je 88 ključev, kjer mi vsak vrne seznam oblike [stevilka okraja, {'st': id_stranke1, 'prc': procenti, 'gl' : stevilo_glasov},{'st': id_stranke1, 'prc': procenti, 'gl' : stevilo_glasov},...,]. Torej na mestu data.rez[key][i] za nek ključ in nek i živi slovar, ki morda opisuje stranki ZSi (id= 5) in ZOS (id= 21). Moja naloga je, da za vsak key identificiram ta slovar in ga izbrišem. Torej se moram sprehoditi po vsakem ključu slovarja 'rez' in po vsakem mestu v seznamu, pogledati, ali je seznam[i]['st'] mogoče id za katero izmed zgornjih strank. Vrednost vsakega ključa rez[key], ki nam vrne seznam, bomo napisali na novo. Želimo si, da na prvem mestu seznama, ki je vrednost ključa v slovarju 'rez' še vedno piše številka okraja, nato pa se zvrstijo slovarji z rezultati za posamične stranke (v istem vrstnem redu kot prej), če ta stranka ni SLOGA ali REŠITEV. Kodo za ta del sem v veliki meri spisal sam, a je black magic del pomagal spisati AI.
#
import data
import csv

rez = data.rez
for key in rez:
    rez[key] = [rez[key][0]] + [
        slovar for slovar in rez[key][1:] if slovar["st"] not in {5, 21}
    ]

# sedaj imamo v spominu shranjen slovar 'rez', ki je končen, spraviti pa ga moramo še v našo podatkovno datoteko. V ta namen bom povozil vse, kar je bilo prej napisano v datoteki data.py in zraven dopisal še legendo in rezultate za celo Slovenijo, ki so bili definirani zgoraj.

with open("2022\\data.py", "w", encoding="utf-8") as podatkovna_datoteka:

    podatkovna_datoteka.write(
        f"legenda = {legenda}\n\nrezultati_cela_slovenija = {rezultati_cela_slovenija}\n\nrez = {rez}"
    )


dat = open("2022\\rezultati2022.csv", "w", encoding="utf-8", newline="")


tabela = csv.writer(dat)

tabela.writerow(
    ["OKRAJ"] + list(legenda.keys())
)  # pri tej dotični vrsti sem si pomagal z AI

for key in data.rez:
    tabela.writerow(
        [
            data.rez[key][0],
        ]
        + [data.rez[key][i]["prc"] for i in range(1, 20)]
    )
tabela.writerow(
    ["CELOTA"]
    + [data.rezultati_cela_slovenija[key] for key in data.rezultati_cela_slovenija]
)

dat.close()
