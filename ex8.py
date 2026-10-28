numerador = int(input("digite um numero: "))
expoente = int(input("digite o expoente: "))
resultado = 1
for i in range (expoente):
    resultado *= numerador
print("numerador, elevado a ", expoente, "resultado = " , resultado)
