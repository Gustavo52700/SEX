ano = input("O ano é bissexto? Digite S para sim ou N para não:")
dia = int(input("Digite o dia:"))
mes = int(input("Digite o mês:"))
V = 0

if ano.upper() == "S":
    if dia <= 30 and mes in [1, 3, 5, 7, 8, 10, 12] or dia <= 29 and mes in [4, 6, 9, 11] or dia <= 28 and mes == 2:
        dia += 1
    elif dia == 31 and mes in [1, 3, 5, 7, 8, 10, 12] or dia == 30 and mes in [4, 6, 9, 11] or dia == 29 and mes == 2:
        mes += 1
        dia = 1
    else:
        if mes == 12:
            mes = 1

    print(f"{dia}/{mes}")

elif ano.upper() == "N":
    if dia <= 30 and mes in [1, 3, 5, 7, 8, 10, 12] or dia <= 29 and mes in [4, 6, 9, 11] or dia <= 27 and mes == 2:
        dia += 1
    elif dia == 31 and mes in [1, 3, 5, 7, 8, 10, 12] or dia == 30 and mes in [4, 6, 9, 11] or dia == 28 and mes == 2:
        mes += 1
        dia = 1
    else:
        if mes == 12:
            mes = 1

    print(f"{dia}/{mes}")
