massa = float(input("Digite a quantidade de gramas:"))
tempo = 0
print(f"A massa inicial foi {massa}")
while massa >= 0.50:
    massa /= 2
    tempo += 50
print(f"A massa final foi {massa}")

horas = tempo // 3600
segundosrestantes = tempo % 3600
minutos = segundosrestantes // 60
segundosrestantesfinal = segundosrestantes % 60
print(f"O tempo foi de {horas} horas, {minutos} minutos e {segundosrestantesfinal} segundos!")
