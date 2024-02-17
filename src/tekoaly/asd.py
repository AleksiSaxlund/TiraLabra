import minimax

a = [
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_']]

minimax = minimax.MiniMax(a, "X")

minimax.lauta[10][10] = "X"
minimax.lisaa_varattu_paikka(10, 10)
minimax.lauta[9][9] = "O"
minimax.lisaa_varattu_paikka(9, 9)

minimax.tulosta_lauta()
input()

minimax.lauta[10][11] = "X"
minimax.lisaa_varattu_paikka(10, 11)
asd = minimax.valitse_paras_siirto()
print(asd)
minimax.lauta[asd[0][0]][asd[0][1]] = "O"

minimax.tulosta_lauta()
input()

minimax.lauta[10][9] = "X"
minimax.lisaa_varattu_paikka(10, 9)
asd = minimax.valitse_paras_siirto()
print(asd)

minimax.lauta[asd[0][0]][asd[0][1]] = "O"

minimax.tulosta_lauta()