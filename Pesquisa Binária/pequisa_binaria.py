def pesquisa_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = int((inicio + fim) / 2)
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            fim = meio - 1
        else:
             inicio = meio + 1
    return None

lista = [1, 3,5,7,9,34,56,78]
print(pesquisa_binaria(lista,56))