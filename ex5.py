maior = 0
menor = 1000000
for i in range(5):
    num=int(input("Digite um numero: "))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print("O maior numero foi", maior)
print("O menor numero foi", menor)