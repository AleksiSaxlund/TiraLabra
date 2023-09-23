# Viikkoraportti 3

## Tällä viikolla

- Tehty alustava minimax algoritmi
- Aloitettu heurestiikkafunktion tekoa
- Korjailtu bugeja pelistä

## Edistyminen

Minimax itsessään alkaa olemaan kutakuinkin valmiina. Tällä hetkellä sitä ei ole vielä integroitu peliin itseensä, mutta sitä voi testailla [minimax.py](/src/tekoaly/minimax.py) tiedostossa muuttelemalla itse muuttujaa "lauta" pelin mukaisesti ja ajamalla tiedosto välissä, että saa tekoälyn siirron. [heurestiikka_temp.py](/src/tekoaly/heurestiikka_temp.py) sisältää netistä löytämäni heurestiikkafunktion, jonka avulla testailen väliaikaisesti algoritmin toimimista. [heurestiikka_dev.py](/src/tekoaly/heurestiikka_dev.py) taas sisältää itse tekemääni keskeneräistä heurestiikkafunktiota, joka valmistuttuaan korvaa väliaikaisen funktion.

## Opin

Paljon minimaxin käytännön ongelmista ja heurestiikkafunktion luomisesta.

## Seuraavaksi

Seuraavaksi olisi tarkoitus saada heurestiikkafunktio kutakuinkin toimivaan kuntoon. Se myös kaipailee vielä muutoksiakin jos valmiina olevaan koodiinkin. Tämän jälkeen voi alkaa sovittelemaan ja optimoimaan minimaxia isommalle pelilaudalle.

## Käytetty aikaa

Aikaa käytetty noin 9 tuntia.
