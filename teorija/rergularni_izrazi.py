dat = open("filmi.html", encoding="utf8")
vsebina = dat.read()
dat.close()

import re  # regularni izrazi

#

# REGULARNI IZRAZI
# . - katerikoli znak
# .a - karkoli + a
# \d - decimal, številka, v pythonu \\d, ker je prvi \ anchor, ki pythinu reče, da pride za njim dejasnki znak. Alternativno r'\d', ker r pomeni 'raw'
# \w - alfanumerični znak
# \W - vse, razen alfanumerični znaki
# \s - bel znak tipa space,tab, new line ...

# \d+ - iščem eno ali več števk (torej eno ali več iteracij isteg družine, v tem primeru števil) - išče požrešno
# * - lahko da je, lahko pa da ga ni, npr. .*d - vsi d-ji ki imajo nekaj pred seboj, lahko pa da tudi nimajo
# *? -išči čim krajšo iteracijo
# d?   d+   d* - 0 ali 1 pojavitev d-ja,  1 ali več ponovitev d-ja    0 ali več ponovitev d-ja
# [ñññ] - list , iz katerega nekaj mora imeti tisto, kar iščemo TO JE ENA ENOTA
# [^a] - brez a-ja
# [a-z] - pojdi od a do z
# [a-z]{4}: štiri črke
# \b - rob besede
# $ - konec
# () - skupina
# \1 - prejšnjo skupino (prvo odprto od leve proti desni) mi še enkrat naprintaj
# (?P<id>\d) -


def izlusci_naslove(vsebina):
    filmi = []
    for najdba in re.finditer(
        r"<a\s*https://www\.imdb\.com/tile/tt(?P<id>\d)+", vsebina, flags=re.DOTALL
    ):
        filmi.append(najdba)
    print(len(filmi))


izlusci_naslove(vsebina)
