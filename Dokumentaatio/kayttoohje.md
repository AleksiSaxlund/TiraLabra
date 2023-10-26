# 

## Pelin säännöt

Pelin tarkoitus on tehdä omista merkeistä katkeamaton 5:n suora pelilaudalle. Nappuloita ei saa laittaa vastustajan- tai omien merkkien päälle. Peli loppuu heti kun toinen pelaaja saa 5:n suoran. X-nappulalla pelaava aloittaa aina ensin.

## Pelin käynnistäminen

Pelin voit käynnistää ajamalla seuraavat komennot projektin juurihakemistossa:

1. ```poetry shell```
2. ```python3 ./src/main.py```

Näin ohjelma aukeaa terminaaliin.

## Pelin pelaaminen

Pelin alussa pelaajalta kysytään kummalla nappulalla hän haluaa pelata. Kirjoita haluamasi nappula "X" tai "O" (ilman lainausmerkkejä) ja paina enter. Peli kysyy uutta syötettä kunnes se saa oikean syötteen.

Nappulan valitsemisen jälkeen terminaaliin tulostuu pelilauta. Jos pelaaja on X niin hän saa tehdä ensimmäisen siirron. Muuten tekoäly tekee ensimmäisen siirron.

Pelaaja voi vuorollaan tehdä siirron kirjoittamalla tahtomansa ruudun koordinaatit, kun niitä kysytään. Peli ei hyväksy väärässä formaatissa syötettyjä koordinaatteja.

Esimerkkejä hyväksytyistä syötteistä (kaikki ilman lainausmerkkejä):
"1 1", "10 1, "4 20","25 25" ja "15 15"

Esimerkkejä hylätyistä syötteistä:
"1 ", "232", "-1 10", "1232 ", "30 4" ja "10 0"

Syötteen ensimmäinen luku on X-koordinaatti ja toinen luku on Y-koordinaatti. Koordinaattien indeksointi alkaa myös 1:stä, eli kumpikin koordinaatti voi olla luku 1-25.
