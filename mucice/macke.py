import csv
import os
import requests
import re

###############################################################################
# Najprej definirajmo nekaj pomožnih orodij za pridobivanje podatkov s spleta.
###############################################################################

# definirajte URL glavne strani bolhe za oglase z mačkami
cats_frontpage_url = "http://www.bolha.com/zivali/male-zivali/macke/"
# mapa, v katero bomo shranili podatke
cat_directory = "mucice"
# ime datoteke v katero bomo shranili glavno stran
frontpage_filename = "macke.html"
# ime CSV datoteke v katero bomo shranili podatke
csv_filename = "macke.csv"


def download_url_to_string(url):
    """Funkcija kot argument sprejme niz in poskusi vrniti vsebino te spletne
    strani kot niz. V primeru, da med izvajanje pride do napake vrne None.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text

    except Exception as e:
        print(f"Nekaj je šlo nekaj narobe: {e}")

        # koda, ki se izvede pri napaki
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije


def save_string_to_file(text, directory, filename):
    """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
    locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
    niz "directory" prazen datoteko ustvari v trenutni mapi.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, "w", encoding="utf-8") as file_out:
        file_out.write(text)


# Definirajte funkcijo, ki prenese glavno stran in jo shrani v datoteko.


def save_frontpage(page, directory, filename):
    """Funkcija shrani vsebino spletne strani na naslovu "page" v datoteko
    "directory"/"filename"."""
    save_string_to_file(download_url_to_string(page), directory, filename)


###############################################################################
# Po pridobitvi podatkov jih želimo obdelati.
###############################################################################


def read_file_to_string(directory, filename):
    """Funkcija vrne celotno vsebino datoteke "directory"/"filename" kot niz."""
    path = os.path.join(directory, filename)
    with open(path, "r", encoding="utf-8") as file_in:
        return file_in.read()


# Definirajte funkcijo, ki sprejme niz, ki predstavlja vsebino spletne strani,
# in ga razdeli na dele, kjer vsak del predstavlja en oglas. To storite s
# pomočjo regularnih izrazov, ki označujejo začetek in konec posameznega
# oglasa. Funkcija naj vrne seznam nizov.


def page_to_ads(page_content):
    """Funkcija poišče posamezne oglase, ki se nahajajo v spletni strani in
    vrne seznam oglasov."""
    oglasi = re.findall(
        r'<article.*?href="/macke.*?</article>', page_content, flags=re.DOTALL
    )
    return oglasi


# Definirajte funkcijo, ki sprejme niz, ki predstavlja oglas, in izlušči
# podatke o imenu, lokaciji, datumu objave in ceni v oglasu.


def get_dict_from_ad_block(block):
    """Funkcija iz niza za posamezen oglasni blok izlušči podatke o imenu, ceni
    in opisu ter vrne slovar, ki vsebuje ustrezne podatke."""
    ime_zadetek = re.search(r"<span>(.*?)</span>", block, flags=re.DOTALL)
    # return ime[1] #ali ime.group(1) ali v oklepajih (?P<ime>.*?)
    datum_zadetek = re.search(
        r'<time.*?pubdate="pubdate">(.*?)</time>', block, flags=re.DOTALL
    )
    cena_zadetek = re.search(
        r'<strong class="price price--hrk">(.*?)>/strong>', block, flags=re.DOTALL
    )

    if ime_zadetek and datum_zadetek and cena_zadetek:
        return {
            "ime": ime_zadetek.group(1),
            "datum": datum_zadetek.group(1),
            "cena": cena_zadetek.group(1),
        }


# Definirajte funkcijo, ki sprejme ime in lokacijo datoteke, ki vsebuje
# besedilo spletne strani, in vrne seznam slovarjev, ki vsebujejo podatke o
# vseh oglasih strani.


def ads_from_file(filename, directory):
    """Funkcija prebere podatke v datoteki "directory"/"filename" in jih
    pretvori (razčleni) v pripadajoč seznam slovarjev za vsak oglas posebej."""
    stran = read_file_to_string(directory, filename)
    bloki = page_to_ads(stran)
    oglasi = []
    for blok in bloki:
        oglas = get_dict_from_ad_block(blok)
        if oglas:
            oglasi.append(oglas)
    return oglasi


###############################################################################
# Obdelane podatke želimo sedaj shraniti.
###############################################################################


def write_csv(fieldnames, rows, directory, filename):
    """
    Funkcija v csv datoteko podano s parametroma "directory"/"filename" zapiše
    vrednosti v parametru "rows" pripadajoče ključem podanim v "fieldnames"
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, "w", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


# Definirajte funkcijo, ki sprejme neprazen seznam slovarjev, ki predstavljajo
# podatke iz oglasa mačke, in zapiše vse podatke v csv datoteko. Imena za
# stolpce [fieldnames] pridobite iz slovarjev.


def write_cat_ads_to_csv(ads, directory, filename):
    """Funkcija vse podatke iz parametra "ads" zapiše v csv datoteko podano s
    parametroma "directory"/"filename". Funkcija predpostavi, da so ključi vseh
    slovarjev parametra ads enaki in je seznam ads neprazen."""
    # Stavek assert preveri da zahteva velja

    # Če drži se program normalno izvaja, drugače pa sproži napako
    # Prednost je v tem, da ga lahko pod določenimi pogoji izklopimo v
    # produkcijskem okolju

    # assert ads and (all(j.keys() == ads[0].keys() for j in ads))

    write_csv(ads[0].keys(), ads, directory, filename)


# Celoten program poženemo v glavni funkciji


def main(redownload=True, reparse=True):
    """Funkcija izvede celoten del pridobivanja podatkov:
    1. Oglase prenese iz bolhe
    2. Lokalno html datoteko pretvori v lepšo predstavitev podatkov
    3. Podatke shrani v csv datoteko
    """
    # Najprej v lokalno datoteko shranimo glavno stran
    if redownload:
        save_frontpage(cats_frontpage_url, cat_directory, frontpage_filename)
    # Iz lokalne (html) datoteke preberemo podatke
    # stran = read_file_to_string(cat_directory, frontpage_filename)
    # oglasi = page_to_ads(stran)
    # print(len(oglasi))
    # #print(stran)
    # Podatke preberemo v lepšo obliko (seznam slovarjev)
    if reparse:
        oglasi = ads_from_file(frontpage_filename, cat_directory)
    # Podatke shranimo v csv datoteko
    write_cat_ads_to_csv(oglasi, cat_directory, csv_filename)
    # Dodatno: S pomočjo parametrov funkcije main omogoči nadzor, ali se
    # celotna spletna stran ob vsakem zagon prenese (četudi že obstaja)
    # in enako za pretvorbo


if __name__ == "__main__":
    main()
