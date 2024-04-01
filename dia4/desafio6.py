p1 = int(input("Digite o placar do primeiro time: "))
p2 = int(input("Digite o placar do segundo time: "))

if p1 == p2:
    print("Empate")
elif p1 > p2:
    print("O primeiro time venceu!")
elif p2 > p1:
    print("O segundo time venceu!")