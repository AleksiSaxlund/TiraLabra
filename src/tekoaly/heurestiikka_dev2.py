
def arvioi(lauta, arvioitava):
    n = len(lauta)
    laudan_arvo = 0
    nappulat = ["X", "O"]
    nappulat.remove(arvioitava)
    vastustaja = nappulat[0]

    for i in range(n):
        for j in range(n):
            valiarvo = 0
            if lauta[i][j] == arvioitava:
                for x in range(5):
                    if j + x < n:

                        if lauta[i][j + x] == arvioitava:
                            valiarvo += 1
                            if valiarvo >= 5:
                                return 9999
                        elif lauta[i][j + x] == vastustaja:
                            break
            if valiarvo == 1:
                valiarvo = 0
            laudan_arvo += valiarvo
    return laudan_arvo


#[print(i) for i in range(-5, 5)]

lauta = [["", "", "", "", "X", "X", "X", "X", "O", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""]]

print(arvioi(lauta, "X"))