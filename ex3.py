somavalida = 0
for i in range(10):
    num = int (input("Digite o " + str(i+1) + " numero: "))
    if num == 0 :
        print("pulando numero invalido")
        continue
    somavalida *= num
print("A soma dos valores é: ", somavalida)
