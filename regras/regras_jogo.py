from utilizaveis.utils import verificar_elemento, converter_letras_em_numeros


def validar_linhas(matriz):
    linhas_aprovadas = 0
    for r in range(len(matriz)):
        if verificar_elemento(matriz[r]):
            linhas_aprovadas += 1

    if linhas_aprovadas == len(matriz):
        return True
    else:
        return False


def validar_colunas(matriz):
    colunas_validadas = 0
    contador = 0

    while contador < len(matriz):
        coluna_temp = []

        for r in range(len(matriz)):
            coluna_temp.append(matriz[r][contador])

        if verificar_elemento(coluna_temp):
            colunas_validadas += 1
        contador += 1

    if colunas_validadas == len(matriz):
        return True
    else:
        return False


def quadrante(lin_ini, lin_fin, col_ini, col_fin, matriz):
    cont_lin = lin_ini - 1
    regiao = []

    while cont_lin < lin_fin:
        cont_col = col_ini - 1
        while cont_col < col_fin:
            regiao.append(matriz[cont_lin][cont_col])
            cont_col += 1
        cont_lin += 1
    return regiao


def validar_quadrantes(quadrantes):
    quadrante_validado = 0

    for quadrante in range(len(quadrantes)):
        if verificar_elemento(quadrantes[quadrante]):
            quadrante_validado += 1

    if quadrante_validado == len(quadrantes):
        return True
    else:
        return False


def validar_jogo(matriz, dicas):
    try:
        quad01 = quadrante(1, 3, 1, 3, matriz)
        quad02 = quadrante(1, 3, 4, 6, matriz)
        quad03 = quadrante(1, 3, 7, 9, matriz)

        quad04 = quadrante(4, 6, 1, 3, matriz)
        quad05 = quadrante(4, 6, 4, 6, matriz)
        quad06 = quadrante(4, 6, 7, 9, matriz)

        quad07 = quadrante(7, 9, 1, 3, matriz)
        quad08 = quadrante(7, 9, 4, 6, matriz)
        quad09 = quadrante(7, 9, 7, 9, matriz)

        quadrantes = []
        quadrantes.append(quad01)
        quadrantes.append(quad02)
        quadrantes.append(quad03)

        quadrantes.append(quad04)
        quadrantes.append(quad05)
        quadrantes.append(quad06)

        quadrantes.append(quad07)
        quadrantes.append(quad08)
        quadrantes.append(quad09)

    except Exception:
        quadrantes = []

    if len(dicas) >= 1 and len(dicas) <= 80:
        if validar_linhas(matriz) and validar_colunas(matriz) and validar_quadrantes(quadrantes):
            return True
        else:
            return False
    else:
        return False


def validar_formato(lista):
    try:
        col_str, lin, num = lista.split()
        col_str = [[col_str]]
        col = converter_letras_em_numeros(col_str)[0][0]

        return [col, lin, num]

    except Exception:
        return False


def validar_jogada(jogada):
    resultado = validar_formato(jogada)

    intervalo = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if resultado:
        if resultado[0] not in intervalo or resultado[1] not in intervalo or resultado[2] not in intervalo:
            # print("Tente novamente!")
            return False

        else:
            return resultado
    else:
        return False
