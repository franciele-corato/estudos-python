contador = 0
soma = 0
while True:
    numerador = int(input("Digite um numerador e (0) para encerrar: "))
    if numerador == 0:
        break
    else :
        contador +=1
        soma += numerador
if contador == 0:
    print("Não foram inseridos numeros a calcular")
else:
    media = soma /contador
    print("Resultado da media dos numeros: ", media)