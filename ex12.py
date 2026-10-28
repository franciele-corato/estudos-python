print("sistema de compras")
total = 0
continuar = True
while continuar:
    while True:
        produto = input("Digite o nome do produto: ")
        if produto != "":
            break
        else:
            print("Nome do produto inválido")
    while True:
        try:
            valor = float(input("Digite o valor unitario do produto: "))
            if valor <= 0:
                print("O valor deve ser maior que 0")
            else :
                break
        except ValueError:
            print("Valor invalido")
    while True:
        try:
            quantidade = int(input("Digite a quantidade de produtos a ser comprada: "))
            if valor <=0:
                print("O valor deve ser maior que 0")
            else :
                break
        except ValueError:
            print("Valor invalido")

    total += quantidade * valor

    resp= input("Produto adicionado ao carrinho com sucesso, deseja adicionar mais algum produto? [S/N]").upper()
    if resp == "N":
        continuar = False
print(f"O valor total do carrinho deu R${total:.2f}")