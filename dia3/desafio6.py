nome = str(input("Digite um nome: "))

p = nome.find(" ")
u = nome.rfind(" ")

prinome = nome[:p]
ultnome = nome[u:]

print(f"O primeiro nome é: {prinome} \nO ultimo nome é: {ultnome}")