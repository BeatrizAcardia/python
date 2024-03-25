frase = str(input("Digite uma frase: "))
a = frase.upper()
print(f"você possui {a.count("A")} no nome. \na posição do primeiro A é: {a.find("A")} \na ultima posição do A é: {a.rfind("A")}")