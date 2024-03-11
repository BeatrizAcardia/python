valor = float(input("Digite o valor: "))
taxa = float(input("Digite o valor da sua taxa: "))
tempo = float(input("Digite o tempo: "))

print(f"O valor da prestação em atraso é: {valor+(valor*(taxa/100)*tempo)}")