
def heurestiikka(lauta, maksivoitava, minivoitava):
    # Checking for Rows for X or O victory.
    for row in range(3):
        if (lauta[row][0] == lauta[row][1] and lauta[row][1] == lauta[row][2]):
            if (lauta[row][0] == maksivoitava):
                return 10
            elif (lauta[row][0] == minivoitava):
                return -10

    # Checking for Columns for X or O victory.
    for col in range(3):

        if (lauta[0][col] == lauta[1][col] and lauta[1][col] == lauta[2][col]):

            if (lauta[0][col] == maksivoitava):
                return 10
            elif (lauta[0][col] == minivoitava):
                return -10

    # Checking for Diagonals for X or O victory.
    if (lauta[0][0] == lauta[1][1] and lauta[1][1] == lauta[2][2]):

        if (lauta[0][0] == maksivoitava):
            return 10
        elif (lauta[0][0] == minivoitava):
            return -10

    if (lauta[0][2] == lauta[1][1] and lauta[1][1] == lauta[2][0]):

        if (lauta[0][2] == maksivoitava):
            return 10
        elif (lauta[0][2] == minivoitava):
            return -10

    # Else if none of them have won then return 0
    return 0
