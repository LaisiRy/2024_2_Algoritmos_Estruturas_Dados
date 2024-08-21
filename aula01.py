produtos = ['borracha', 'papel', 'caneta', 'lapis']
precos = [3, 8, 2, 9]
quantidade = [2, 5, 4, 8]

def imprimir_produto(index):
    if 0 <= index < len(produtos):
        print(f"Produto: {produtos[index]}, Preço: {precos[index]}, Quantidade: {quantidade[index]}")
    else:
        print("Índice fora do intervalo.")

def retirar_produto(index, quantidade_retirada):
    if 0 <= index < len(produtos):
        if quantidade[index] >= quantidade_retirada:
            quantidade[index] -= quantidade_retirada
            print(f"{quantidade_retirada} unidades de {produtos[index]} retiradas. Restante: {quantidade[index]}")
        else:
            print("Quantidade insuficiente para retirada.")
    else:
        print("Índice fora do intervalo.")
