frase = str(input("Digite uma sequencia: "))
quartoCareacter = frase[3:7:2] #3 - pega o numero 3 da sequencia, 7 - adiciona uma sequencia da posição 3 ao 7, 2 - faz essa sequencia pulando de 2 em 2 números
print(f"O quarto caractere é: {quartoCareacter}")


frase2 = str(input("Digite uma sequencia de novo: "))
caractere = frase2[:7] #vai de 0 até até a posição 7 ex: (12345678910 > 1234567)
print(f"A sequencia com :7 é: {caractere}")


frase3 = str(input("Digite uma sequencia (len): "))
tamanhofrase = len(frase3) #le quantos caracteres tem na sequencia
print(f"tamanho da frase é: {tamanhofrase}")


frase4 = str(input("digite uma sequencia: "))
tamanhostring = frase4.count("3")
print(f"Quantas vezes repete a string 3: {tamanhostring}")


frase5 = str(input("Digite uma sequencia: "))
tamanhofrase2 = frase.find("Pynthon")
print(f"Tamanho da frase é: {tamanhofrase2}")


frase6 = str(input("Digite uma sequencia: "))
tamanhofrase3 = "Python" in frase6
print(f"Tamanho da frase é: {tamanhofrase3}")


frase7 = str(input("Digite uma sequencia: "))
tamanhostring2 = frase7.upper()
print(f"sua string maiuscula é: {tamanhostring2}")


frase8 = str(input("Digite uma sequencia: "))
tamanhostring3 = frase8.lower()
print(f"sua string minuscula é: {tamanhostring3}")

frase9 = str(input("Digite uma sequencia: "))
tamanhostring = frase8.capitalize()
print(f"SOMENTE a primeira letra em maiusculo: {tamanhostring}")


frase10 = str(input("Digite uma sequencia: "))
tamanhostring = frase10.title()
print(f"toda a primeira letra em maiusculo de cada palavra: ")


frase11 = str(input("Digite uma sequencia: "))
tamanhofrase = frase11.replace("Javascript", "Python")
print(f"Tamano da frase é: {tamanhofrase}")
