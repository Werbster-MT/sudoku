import sys

from nucleo.jogo import executar_jogo
from estruturas.matriz import matriz
from utilizaveis.utils import ler_dicas

"""Sudoku desenvolvido puramnete em python, por: 
    Werbster Marques Teixeira - Matricula: 537205
    Pedro Henrique Santos Rodrigues - Matricula: 537759
"""

if __name__ == "__main__":
    grade = matriz(9, 9, " ")
    dicas = ler_dicas(sys.argv[1])
    executar_jogo(grade, dicas)
