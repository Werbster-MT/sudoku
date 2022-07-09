from estruturas.matriz import matriz, exibir_matriz, preencher_matriz
from regras.regras_jogo import validar_jogo
from utilizaveis.utils import ler_dicas, converter_letras_em_numeros, converter_string_para_int
import sys

def validar_jogadas():
    jogada = input("Informe uma jogada: ").replace(":", ",").split()
    if jogada[0] is not None:
        jogada[0].replace(",", " ")
        print(jogada[0])


if __name__ == "__main__":
    """1.1) Mostrar a Matriz."""

    grade = matriz(9, 9, " ")

    dicas = ler_dicas(sys.argv[1])
    dicas_str = converter_letras_em_numeros(dicas)
    dicas_int = converter_string_para_int(dicas)

    grade_preenchida = preencher_matriz(dicas_int, grade)
    exibir_matriz(grade_preenchida)

    if validar_jogo(grade_preenchida, dicas_int):
        validar_jogadas()

    else:
        print("Jogo Invalido !")