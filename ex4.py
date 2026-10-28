pares=0
impares=0
for i in range(10):
    Dados = int (input("digite um numero: "))
    if Dados%2==0:
        pares +=1
    else:
        impares +=1
print("Dos 10 numeros ", pares, " são par e ", impares ,"são impar")