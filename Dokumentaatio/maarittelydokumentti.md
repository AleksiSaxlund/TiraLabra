# Projekti

Jatkan projektia periodi 1 toteutuksesta.

## Projektin määritelmä

Projektin tarkoituksena olisi luoda tekoäly 25x25 ristinollalle, jossa voittoehtona on 5:n rivi. Peliä voisi pelata tekoälyä vastaan ja jos aika sallii niin voisi lisätä myös AI vs AI pelitilan.

## Projektin kielet

Käytän projektissa Pythonia ja se on ainut kieli, jota osaan kunnolla ja dokumentaatiot tulee olemaan Suomen kielellä. 

## Käyttöliittymä ja syötteet

Käyttöliittymän olisi tarkoitus olla terminaalissa, johon tulostetaan jokaisen vuoron alussa pelilaudan tilanne. Jokaisella pelaajan vuorolla kysytään seuraava peliliike, jonka pelaaja syöttää koordinaatteina tyyliin: "11 2".

## Algoritmit ja tietorakenteet

Toteutan tekoälyn minimax-algoritmilla, jota tehostan alpha-beta-karsinnalla. Minimax-algoritmi hyödyntää puurakennetta ja pelilautaa esitän 25x25 matriisia, joka muodostuu listoista.

Minimax-algoritmin aikavaativuus on O(b^m) ja alpha-beta-karsinnalla O(b^d).

Minimax-algoritmi alpha-beta-karsinnalla on kohtalaisen yksinkertainen, mutta silti tehokas tapa toteuttaa tekoäly ristinollan kaltaiselle pelille, sekä kyseisestä tavasta löytyy reilusti dokumentaatiota netistä.

## Opinto-ohjelma

Tietojenkäsittelytieteen kandidaatti

## Lähteet

- https://cis.temple.edu/~vasilis/Courses/CIS603/Lectures/l7.html
- https://en.wikipedia.org/wiki/Minimax
- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
