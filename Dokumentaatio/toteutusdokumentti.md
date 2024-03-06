# Toteutusdokumentti

## Rakenne

Korkealla tasolla ohjelma on jaettu kahteen osaan. [Peli](/src/peli/) ja [tekoäly](/src/tekoaly/). Peli-osa vastaa käyttöliittymästä sekä pelin pyörittämisestä itsestään. Tekoäly-osa taas vastaa ohjelman algoritmillisesta puolesta.

### Luokkarakenne

```mermaid

classDiagram
    class kayttoliittyma
    class pelilauta
    class pelimoottori
    class minimax
    class heurestiikka

    pelimoottori "1" -- "1" kayttoliittyma
    pelimoottori "1" -- "1" pelilauta
    pelimoottori "1" -- "1" minimax
    minimax -- heurestiikka

```

### Toiminnallisuutta

Peli on alkanut ja siirtoja on tehty X määrää. On pelaajan vuoro tehdä siirto.

```mermaid

sequenceDiagram
    actor käyttäjä
    participant kayttoliittyma
    participant pelimoottori
    participant pelilauta
    participant minimax
    participant heurestiikka

    käyttäjä ->> kayttoliittyma: Syöte
    activate kayttoliittyma
    kayttoliittyma ->> pelimoottori: return syöte
    activate pelimoottori
    pelimoottori ->> pelilauta: pelilauta.siirto(syöte, nappula)
    activate pelilauta
    pelilauta ->> pelimoottori: return True
    deactivate pelilauta
    pelimoottori ->> minimax: minimax.lisaa_varattu_paikka(x, y)
    activate minimax
    minimax ->> pelimoottori: ""
    deactivate minimax
    pelimoottori ->> pelimoottori: tekoalyn_vuoro()
    pelimoottori ->> minimax: minimax.valitse_paras_siirto()
    activate minimax
    minimax ->> minimax: self.lisaa_tutkittavat_paikat()
    minimax ->> minimax: self.minimax("KAIKKI APUMUUTTUJAT") Kutsuu itseään kunnes lopetusehdot täyttyy
    minimax ->> minimax: self.voiton_tarkistin()
    minimax ->> minimax: self.minimax("KAIKKI APUMUUTTUJAT") Kutsuu itseään kunnes lopetusehdot täyttyy
    minimax ->> heurestiikka: arvioi(lauta, nappula), kun saavutettu tavoitesyvyys
    activate heurestiikka
    heurestiikka ->> minimax: return laudan_arvo
    deactivate heurestiikka
    minimax ->> pelimoottori: return paras_siirto
    deactivate minimax
    pelimoottori ->> minimax: minimax.lisaa_varattu_paikka(x, y)
    activate minimax
    minimax ->> pelimoottori: ""
    deactivate minimax
    pelimoottori ->> pelilauta: pelilauta[x][y] = tekoälyn nappula
    activate pelilauta
    pelilauta ->> pelimoottori: ""
    deactivate pelilauta
    pelimoottori ->> pelimoottori: self.voiton_tarkistin()
    pelimoottori ->> kayttoliittyma: kayttoliittyma.tulosta_pelilauta()
    deactivate pelimoottori
    kayttoliittyma ->> käyttäjä: Tulostaa pelitilanteen
    deactivate kayttoliittyma

```

## Puutteet ja parannusehdotukset

1. Tekoälyn pelitaidoissa on parantamisen varaa ja se on myös hitaampi kuin toivoisin. Tilanteesta riippuen jopa liian hidas.
2. Vaikeusasteen voisi tehdä muutettavaksi syvyyttä kasvattamalla ja pienentämällä. Nyt kuitenkin syvyyden kasvatus tekee tekoälystä hitaan.
3. Graafinen käyttäliittymä olisi kiva.

## Aika- ja tilavaativuudet

Minimaxin aikavaativuus on O(mahdollisten siirtojen määrä^syvyys)ja alphabeetta karsinnalla se on O(mahdollisten siirtojen määrä^(syvyys/2)).

Suorituskykytestauksen löytää [testausdokumentin](./testausdokumentti.md) *Suorituskykytestaus* osiosta.

## Kielimallien käyttö

Kielimalleja käytettiin työn alussa asiaan perehtymiseen ja projektin hahmotteluun korkealla tasolla. Kaikki koodi sekä dokumentaatio on kuitenkin tehty täysin ilman kielimalleja.

## Lähteet

- [Minimax, Wikipedia](https://en.wikipedia.org/wiki/Minimax)
- [Minimax set 1, geeks for geeks](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/)
- [Minimax set 4, geeks for geeks](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/)
