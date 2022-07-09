def letras(list):
    for letter in range(len(list)):
        if letter == 0:
            print("{:>6}  ".format(list[letter]), end="")

        elif letter == 1 or letter == 4 or letter == 7:
            print("{:^4}".format(list[letter]), end="")

        elif letter == 2 or letter == 5 or letter == 8:
            print("{:^4}".format(list[letter]), end="")

        else:
            print("{:^5}".format(list[letter]), end="")
    print()

def converter_letras_em_numeros(letras):
    for letra in range(len(letras)):
        if letras[letra][0].lower() == "a":
            letras[letra][0] = 1
        elif letras[letra][0].lower() == "b":
            letras[letra][0] = 2
        elif letras[letra][0].lower() == "c":
            letras[letra][0] = 3
        elif letras[letra][0].lower() == "d":
            letras[letra][0] = 4
        elif letras[letra][0].lower() == "e":
            letras[letra][0] = 5
        elif letras[letra][0].lower() == "f":
            letras[letra][0] = 6
        elif letras[letra][0].lower() == "g":
            letras[letra][0] = 7
        elif letras[letra][0].lower() == "h":
            letras[letra][0] = 8
        elif letras[letra][0].lower() == "i":
            letras[letra][0] = 9
    return letras

def converter_string_para_int(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(matriz[i][j])
    return matriz

def ler_dicas(arquivo):
    with open(arquivo, "r") as arq_config:
        linhas = arq_config.readlines()

        dicas = [] * len(linhas)

        dados = ""

        for l in range(len(linhas)):
            if len(linhas[l]) > 5:
                dados = linhas[l][0:5].replace(":", ",")

            else:
                dados = linhas[l].replace(":", ",")

            dicas.insert(l, list(dados.replace(",", "")))

    arq_config.close()
    return dicas

def verificar_elemento(lista):
    for elemento in range(len(lista)):
        lista_temp = lista.copy()
        del lista_temp[elemento]
        demais_valores = lista_temp

        if lista[elemento] != " " and lista[elemento] in demais_valores:
            return False

        else:
            if elemento + 1 == len(lista):
                return True
