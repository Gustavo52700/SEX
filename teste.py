from random import randint

alunos = ["Gustavo", "Breno"]

for aluno in alunos:
    nota_1 = randint(0, 10)
    nota_2 = randint(0, 10)
    nota_3 = randint(0, 10)

    media = nota_1 * 0.2 + nota_2 * 0.3 + nota_3 * 0.5

    print(f"\t O aluno é {aluno.capitalize()} e sua notas foram:\n"
          f"\t Nota 1 foi {nota_1}\n"
          f"\t Nota 2 foi {nota_2}\n"
          f"\t Nota 3 foi {nota_3}"
          )

    if media > 6:
        print(f"\t Você foi APROVADO com {media} na media!\n")

    elif media == 6:
        print(f"\t Você passou na média com {media}!\n")

    else:
        print(f"\t Você foi REPROVADO com {media} na media!\n")



