def linha(tam=65):
    return '\033[36m-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(65))
    print(linha())
