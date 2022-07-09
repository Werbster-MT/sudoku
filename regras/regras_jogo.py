from utilizaveis.utils import verificar_elemento

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
            # print(f"{matriz[cont_lin][cont_col]}", end=" ")
            regiao.append(matriz[cont_lin][cont_col])
            cont_col += 1
        # print()
        cont_lin += 1
    # print(regiao)
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


def validar_jogo(matriz, dicas_int):
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

    if len(dicas_int) >= 1 and len(dicas_int) <= 80:
        if validar_linhas(matriz) and validar_colunas(matriz) and validar_quadrantes(quadrantes):
            return True

    else:
        return False
