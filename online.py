radno_vreme=8
ponedeljak=7
utorak=8
sreda=8
cetvrtak=7
petak=8
ukupno=ponedeljak + utorak + sreda + cetvrtak + petak
prosek=ukupno/5


if prosek<7:
    print("bad employre")
elif prosek>7:
    print("good employre")
else:
    print("solid employre")

Ime="Strahinja"
for letter in Ime:
    print(letter)
