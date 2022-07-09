import sys

from estruturas.matriz import matriz, exibir_matriz, preencher_matriz
from regras.regras_jogo import validar_jogo, validar_jogada
from utilizaveis.utils import ler_dicas, converter_letras_em_numeros, converter_string_para_int


if __name__ == "__main__":
    """1.1) Mostrar a Matriz."""

    grade = matriz(9, 9, " ")

    dicas = ler_dicas(sys.argv[1])
    dicas_str = converter_letras_em_numeros(dicas)

    grade_preenchida = preencher_matriz(dicas_str, grade)
    exibir_matriz(grade_preenchida)

    if validar_jogo(grade_preenchida, dicas_str):
        while True:
            validar_jogada()