# Entrada

idade = input("Digite a sua idade:")
sexo = input("Digite M para masculino e F para feminino:")
anostrab = input("Digite quantos anos voce trabalhou:")

if sexo.upper() == "M":
    if int(idade) >= 65 or int(anostrab) >= 30:
        print("Aposentadoria aceita!")
    else:
        print(f"Aposentadoria negada! Espere mais {65 - int(idade)} anos, ou trabalhe por mais {30 - int(anostrab)} anos.")

elif sexo.upper() == "F":
    if int(idade) >= 60:
        print("Aposentadoria aceita!")
    else:
        print(f"Aposentadoria negada! Espere mais {60 - int(idade)} anos.")

else:
    print("Aposentadoria negada, digite F ou M!")
