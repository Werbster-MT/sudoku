from utilizaveis.utils import letras


def linha(simbolo, repeticoes):
    print(f"  +{simbolo * repeticoes}+{simbolo * repeticoes}+{simbolo * repeticoes}++")


def matriz(lin, col, val):
    """Função que retorna uma matriz, com um valor inicial padrão."""
    m = [[val] * col for i in range(lin)]
    return m


def exibir_matriz(matriz):
    """Percorrer a matriz."""
    try:
        if len(matriz) != 9:
            print("Erro ao exibir a matriz")

        else:
            letras(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
            for row in range(len(matriz)):
                if row % 3 == 0 and row != 0:
                    linha("+===", 3)
                else:
                    linha("+---", 3)

                print(row + 1, end=" ")
                for col in range(len(matriz[row])):
                    if col == 0:
                        print("|| %s " % matriz[row][col], end="")

                    elif col == 1 or col == 4 or col == 7:
                        print("| %s |" % matriz[row][col], end="")

                    elif col == 2 or col == 5 or col == 8:
                        print(" %s ||" % matriz[row][col], end="")

                    else:
                        print(" %s " % matriz[row][col], end="")
                print(" %d" % (row + 1))

                if row == len(matriz) - 1:
                    linha("+---", 3)
    except Exception:
        return


def preencher_matriz(valores, matriz):
    for v in range(len(valores)):
        try:
            if matriz[int(valores[v][1]) - 1][int(valores[v][0]) - 1] == " ":
                matriz[int(valores[v][1]) - 1][int(valores[v][0]) - 1] = valores[v][2]

        except Exception:
            return [[]]

    return matriz