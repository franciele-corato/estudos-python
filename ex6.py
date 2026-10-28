frase = input("Digite uma frase: ")
consoantes = ""
for letra in frase:
    if letra.lower() not in "aeiou":
        consoantes += letra
print(consoantes)
