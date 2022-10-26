A = 5000000
B = 7000000
crescimentoA = 0.03
crescimentoB = 0.02
anos = 0

while A < B:
    anos += 1
    A = A + (A * crescimentoA)
    B = B + (B * crescimentoB)
    if A > B:
        print(f"'Em {anos} anos a populacao A ira ultrapassar a populacao B")
        print(f"Quantidade da população A: {A:.2f}")
        print(f"Quantidade da população B: {B:.2f}")

