from utilizaveis.utils import converter_letras_em_numeros, converter_string_para_int


def validar_jogada():
    jogada = input().replace(":", ",").replace(",", " ")
    col_str, lin, num = jogada.split()
    col_str = [[col_str]]
    col = converter_letras_em_numeros(col_str)[0][0]

    print(f"{type(col)}, {type(lin)}, {type(num)}")
    print(f"{col}, {lin}, {num}")

    dicas = [[col, lin, num]]
    dicas_int = converter_string_para_int(dicas)[0]

    dica_validada = 0
    for dica in dicas_int:
        if dica < 1 or dica > 9:
            print("Formato invalido!")
        else:
            dica_validada += 1

    if dica_validada == len(dicas_int):
        return True

    else:
        return False
