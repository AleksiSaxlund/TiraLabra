
def arvioi(lauta: list, arvioitava: str):
    """Arvioi annetun laudan arvon. Kutsuu apufunkitoita, jotka arvioivat yksitellen
        Kaikki mahdolliset suunnat, joissa voi olla suoria.

    Args:
        lauta (list): Arvioitavan pelilaudan nykyinen tilanne
        arvioitava (str): Arvioitava nappula

    Returns:
        int: Palauttaa pelilaudalle arvioidun arvon.
    """
    n = len(lauta)
    laudan_arvo = 0
    nappulat = ["X", "O"]
    nappulat.remove(arvioitava)
    vastustaja = nappulat[0]

    vaaka = arvioi_vaakasuorat(lauta, n, arvioitava, vastustaja)
    pysty = arvioi_pystysuorat(lauta, n, arvioitava, vastustaja)
    diagonaali_vasemmalta_alas = arvioi_diagonaalit_vasemmalta_alas(
        lauta, n, arvioitava, vastustaja)
    diagonaali_vasemmalta_ylos = arvioi_diagonaalit_vasemmalta_ylos(
        lauta, n, arvioitava, vastustaja)

    if 10**5 in [vaaka, pysty, diagonaali_vasemmalta_alas, diagonaali_vasemmalta_ylos]:
        return 10**5

    laudan_arvo = vaaka + pysty + diagonaali_vasemmalta_alas + diagonaali_vasemmalta_ylos
    return laudan_arvo


def arvioi_vaakasuorat(lauta: list, n: int, arvioitava: str, vastustaja: str):
    """Arvioi annetun pelilaudan vaakasuorat rivit. Jos löydetty rivi on auki molemmista päistä, 
        niin sen arvo kerrotaan kahdella. Toisesta päästä auki olevan rivin arvo palautetaan sellaisenaan.
        Molemmista päistä suljettu rivi, jonka pituus on pienempi kuin viisi ei anna yhtään arvoa.

    Args:
        lauta (list): Arvioitava pelilauta
        n (int): Laudan koko
        arvioitava (str): Arvioitava nappula
        vastustaja (str): Vastustajan nappula

    Returns:
        int: Palauttaa vaakasuorille riveille lasketun arvon
    """
    laudan_arvo = 0

    for x in range(n):
        auki_alussa = True
        valiarvo = 0
        for y in range(n):
            if lauta[x][y] == arvioitava:
                if y - 1 <= 0 or lauta[x][y-1] == vastustaja:
                    auki_alussa = False
                valiarvo += 1

            elif lauta[x][y] == vastustaja:
                if auki_alussa:
                    laudan_arvo += valiarvo
                auki_alussa = True
                valiarvo = 0

            if (lauta[x][y] == "_" or y == n - 1) and valiarvo != 0:
                if auki_alussa and valiarvo != 1 and y != n - 1:
                    if valiarvo >= 3:
                        laudan_arvo += valiarvo * 100
                    else:
                        laudan_arvo += valiarvo * valiarvo * 1.5
                else:
                    laudan_arvo += valiarvo * valiarvo
                auki_alussa = True
                valiarvo = 0

            if valiarvo >= 5:
                return 10**5

    return laudan_arvo


def arvioi_pystysuorat(lauta: list, n: int, arvioitava: str, vastustaja: str):
    """Arvioi annetun pelilaudan pystysuorat rivit. Jos löydetty rivi on auki molemmista päistä, 
        niin sen arvo kerrotaan kahdella. Toisesta päästä auki olevan rivin arvo palautetaan sellaisenaan.
        Molemmista päistä suljettu rivi, jonka pituus on pienempi kuin viisi ei anna yhtään arvoa.

    Args:
        lauta (list): Arvioitava pelilauta
        n (int): Laudan koko
        arvioitava (str): Arvioitava nappula
        vastustaja (str): Vastustajan nappula

    Returns:
        int: Palauttaa vaakasuorille riveille lasketun arvon
    """
    laudan_arvo = 0
    for x in range(n):
        auki_alussa = True
        valiarvo = 0
        for y in range(n):
            if lauta[y][x] == arvioitava:
                if y - 1 < 0 or lauta[y-1][x] == vastustaja:
                    auki_alussa = False
                valiarvo += 1

            elif lauta[y][x] == vastustaja:
                if auki_alussa:
                    laudan_arvo += valiarvo * valiarvo
                auki_alussa = True
                valiarvo = 0

            if (lauta[y][x] == "_" or y == n - 1) and valiarvo != 0:
                if auki_alussa and valiarvo != 1 and y != n - 1:
                    if valiarvo >= 3:
                        laudan_arvo += valiarvo * 100
                    else:
                        laudan_arvo += valiarvo * valiarvo * 1.5
                else:
                    laudan_arvo += valiarvo * valiarvo
                auki_alussa = True
                valiarvo = 0

            if valiarvo >= 5:
                return 10**5

    return laudan_arvo


def arvioi_diagonaalit_vasemmalta_alas(lauta: list, n: int, arvioitava: str, vastustaja: str):
    """Arvioi kaikki diagonaalirivit, jotka alkaa vasemmalta ja menee alaspäin, joissa voi kumminkin olla voittorivi.
        Iteraattorit käy läpi kaikki vasemman reunan, sekä ylimmän rivin alkiot, joista voi lähteä sopivia diagonaalirivejä.
        Tämän jälkeen se kutsuu apufunktion, joka käy läpi diagonaalirivin.
        Apufunktioista saadut arvon summataan ja lisätään koko laudan arvoon.

    Args:
        lauta (list): Pelilauta
        n (int): Laudan koko
        arvioitava (str): Arvioitavan pelaajan nappula
        vastustaja (str): Vastustajan nappula

    Returns:
        int: Palauttaa laudan arvon.
    """
    laudan_arvo = 0
    for i in range(n-5, -1, -1):
        diagonaalin_arvo = arvioi_yksi_diagonaali_vasemmalta_alas(
            lauta, n, i, 0, arvioitava, vastustaja)
        if diagonaalin_arvo >= 10**5:
            return diagonaalin_arvo
        laudan_arvo += diagonaalin_arvo

    for i in range(1, n-5):
        diagonaalin_arvo = arvioi_yksi_diagonaali_vasemmalta_alas(
            lauta, n, 0, i, arvioitava, vastustaja)
        if diagonaalin_arvo >= 10**5:
            return diagonaalin_arvo
        laudan_arvo += diagonaalin_arvo
    return laudan_arvo


def arvioi_yksi_diagonaali_vasemmalta_alas(lauta: list, n: int, aloitus_x: int, aloitus_y: int, arvioitava: str, vastustaja: str):
    """Apufunktio, joka arvioi yksittäisen diagonaalirivin arvon. Jos löydetty rivi on auki molemmista päistä, 
        niin sen arvo kerrotaan kahdella. Toisesta päästä auki olevan rivin arvo palautetaan sellaisenaan.
        Molemmista päistä suljettu rivi, jonka pituus on pienempi kuin viisi ei anna yhtään arvoa.

    Args:
        lauta (list): Pelilauta
        n (int): Laudan koko
        aloitus_x (int): Määrittää X-koordinaatin, josta lähdetään liikkeelle.
        aloitus_y (int): Määrittää Y -koordinaatin, josta lähdetään liikkeelle.
        arvioitava (str): Arvioitava nappula
        vastustaja (str): Vastustajan nappula

    Returns:
        int: Palauttaa yksittäisen diagonaalirivin arvon.
    """
    rivin_arvo = 0
    auki_alussa = True
    valiarvo = 0
    for j in range(n + 1):
        if j + aloitus_x + aloitus_y < n:
            if lauta[j + aloitus_x][j + aloitus_y] == arvioitava:
                if j - 1 < 0 or lauta[j + aloitus_x - 1][j + aloitus_y - 1] == vastustaja:
                    auki_alussa = False
                valiarvo += 1

            elif lauta[j + aloitus_x][j + aloitus_y] == vastustaja:
                if auki_alussa:
                    rivin_arvo += valiarvo * valiarvo
                auki_alussa = True
                valiarvo = 0

            if lauta[j + aloitus_x][j + aloitus_y] == "_" and valiarvo != 0:
                if auki_alussa and valiarvo != 1 and j + aloitus_x < n:
                    if valiarvo >= 3:
                        rivin_arvo += valiarvo * 100
                    else:
                        rivin_arvo += valiarvo * valiarvo * 1.5
                else:
                    rivin_arvo += valiarvo * valiarvo
                auki_alussa = True
                valiarvo = 0

            if valiarvo >= 5:
                return 10**5

        else:
            if auki_alussa:
                rivin_arvo += valiarvo * valiarvo
            valiarvo = 0
            break

    return rivin_arvo


def arvioi_diagonaalit_vasemmalta_ylos(lauta: list, n: int, arvioitava: str, vastustaja: str):
    """Arvioi kaikki diagonaalirivit, jotka alkaa vasemmalta ja menee ylös päin, joissa voi kumminkin olla voittorivi.
        Iteraattorit käy läpi kaikki vasemman reunan, sekä alimman rivin alkiot, joista voi lähteä sopivia diagonaalirivejä.
        Tämän jälkeen se kutsuu apufunktion, joka käy läpi diagonaalirivin.
        Apufunktioista saadut arvon summataan ja lisätään koko laudan arvoon.

    Args:
        lauta (list): Pelilauta
        n (int): Laudan koko
        arvioitava (str): Arvioitavan pelaajan nappula
        vastustaja (str): Vastustajan nappula

    Returns:
        int: Palauttaa laudan arvon.
    """
    laudan_arvo = 0
    for i in range(n-5, 0, -1):
        diagonaalin_arvo = arvioi_yksi_diagonaali_vasemmalta_ylos(
            lauta, n, i, 0, arvioitava, vastustaja)
        if diagonaalin_arvo >= 10**5:
            return diagonaalin_arvo
        laudan_arvo += diagonaalin_arvo

    for i in range(0, n - 4):
        diagonaalin_arvo = arvioi_yksi_diagonaali_vasemmalta_ylos(
            lauta, n, 0, i, arvioitava, vastustaja)
        if diagonaalin_arvo >= 10**5:
            return diagonaalin_arvo
        laudan_arvo += diagonaalin_arvo
    return laudan_arvo


def arvioi_yksi_diagonaali_vasemmalta_ylos(lauta: list, n: int, aloitus_x: int, aloitus_y: int, arvioitava: str, vastustaja: str):
    """Apufunktio, joka arvioi yksittäisen diagonaalirivin arvon. Jos löydetty rivi on auki molemmista päistä, 
        niin sen arvo kerrotaan kahdella. Toisesta päästä auki olevan rivin arvo palautetaan sellaisenaan.
        Molemmista päistä suljettu rivi, jonka pituus on pienempi kuin viisi ei anna yhtään arvoa.

    Args:
        lauta (list): Pelilauta
        n (int): Laudan koko
        aloitus_x (int): Määrittää X-koordinaatin, josta lähdetään liikkeelle.
        aloitus_y (int): Määrittää Y -koordinaatin, josta lähdetään liikkeelle.
        arvioitava (str): Arvioitava nappula
        vastustaja (str): Vastustajan nappula

    Returns:
        int: Palauttaa yksittäisen diagonaalirivin arvon.
    """
    rivin_arvo = 0
    auki_alussa = True
    valiarvo = 0
    for j in range(n + 1):
        if n - 1 - j - aloitus_x >= 0 and j + aloitus_y < n:
            if lauta[n - 1 - j - aloitus_x][j + aloitus_y] == arvioitava:
                if j - 1 < 0 or lauta[n - j - aloitus_x][j + aloitus_y] == vastustaja:
                    auki_alussa = False
                valiarvo += 1

            elif lauta[n - 1 - j - aloitus_x][j + aloitus_y] == vastustaja:
                if auki_alussa:
                    rivin_arvo += valiarvo * valiarvo
                auki_alussa = True
                valiarvo = 0

            if lauta[n - 1 - j - aloitus_x][j + aloitus_y] == "_" and valiarvo != 0:
                if auki_alussa and valiarvo != 1 and j + aloitus_y < n:
                    if valiarvo >= 3:
                        rivin_arvo += valiarvo * 100
                    else:
                        rivin_arvo += valiarvo * valiarvo * 1.5
                else:
                    rivin_arvo += valiarvo * valiarvo
                auki_alussa = True
                valiarvo = 0

            if valiarvo >= 5:
                return 10**5

        else:
            if auki_alussa:
                rivin_arvo += valiarvo * valiarvo
            valiarvo = 0
            break

    return rivin_arvo
