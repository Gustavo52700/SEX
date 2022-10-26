par = 0
impar = 0
numero = int(input("Digite um numero:"))
while numero < 1000:
    if numero % 2 == 0 and numero <= 1000:
        par += numero
    elif numero % 2 == 1 and numero <= 1000:
        impar += numero
    numero = int(input("Digite um numero:"))

print(f"A soma dos numeros pares é {par} "
      f"A soma dos numeros impares é {impar}")