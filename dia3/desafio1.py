nome1 = str(input("Digite seu nome: "))
n = nome1.find(" ")
primeironome = nome1[:n]

print(f"O nome em maiusculo é: {nome1.upper} \nSeu nome em minusculo é: {nome1.lower()} \nQuantas letras tem seu nome todo: {len(nome1.strip())} \nQuantas letras tem o primeiro nome: {primeironome}")



