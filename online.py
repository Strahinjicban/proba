radno_vreme=8
ponedeljak=7
utorak=8
sreda=8
cetvrtak=7
petak=6
ukupno=ponedeljak + utorak + sreda + cetvrtak + petak
prosek=ukupno/8

if prosek<10:
    print("bad employre")
elif prosek>10:
    print("good employre")
else:
    print("solid employre")

Ime="Strahinja"
for letter in Ime:
    print(letter)