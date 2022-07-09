from estruturas.matriz import exibir_matriz, preencher_matriz
from regras.regras_jogo import validar_jogo, validar_jogada
from utilizaveis.utils import gerar_indices, converter_letras_em_numeros


def finalizar_jogo(matriz):
    celula_preenchida = 0
    for row in range(len(matriz)):
        for col in range(len(matriz[row])):
            if matriz[row][col] != " ":
                celula_preenchida += 1

    if celula_preenchida == len(matriz) * len(matriz):
        return True
    else:
        return False

def executar_jogo(grade, dicas):
    dicas_str = converter_letras_em_numeros(dicas)

    grade_preenchida = preencher_matriz(dicas_str, grade)
    exibir_matriz(grade_preenchida)

    indices = gerar_indices(dicas_str)

    if validar_jogo(grade_preenchida, dicas_str):
        while True:
            if finalizar_jogo(grade_preenchida):
                break

            jogada = input()

            if len(jogada) == 4:
                jogada_formatada = jogada.replace(",", " ").split()

                col_str = [[jogada_formatada[0][-1]]]
                col = converter_letras_em_numeros(col_str)[0][0]
                lin = jogada_formatada[1]

                indice = [int(col) - 1, int(lin) - 1]

                if indice not in indices:
                    grade_preenchida[int(lin) - 1][int(col) - 1] = " "
                    exibir_matriz(grade_preenchida)

                else:
                    print("Nao pode deletar um dica, tente novamente!")

            else:
                jogada_formatada = jogada.replace(":", ",").replace(",", " ")
                jogada_validada = validar_jogada(jogada_formatada)
                if jogada_validada:
                    col = jogada_validada[0]
                    lin = jogada_validada[1]
                    num = jogada_validada[2]

                    indice = [int(col) -1, int(lin) -1]

                    if indice not in indices:
                        grade_preenchida[int(lin) - 1][int(col) - 1] = num

                        if validar_jogo(grade_preenchida, dicas_str):
                            exibir_matriz(grade_preenchida)

                        else:
                            print("Nao pode haver repeticao, tente novamente!")
                            continue

                    else:
                        print("Nao pode modificar uma dica, tente novamente!")

                else:
                    print("Formato Invalido!")
                    continue

    else:
        print("Dicas invalidas!")
        return
