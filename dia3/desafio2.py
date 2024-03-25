numero = str(input("Digite uma sequencia de numeros de 0 a 999: "))

unidade = numero//1%10
dezena = numero//10%10
centena = numero//100%10
milhar = numero//1000%10

print(f"Unidade: {unidade} \nDezena: {dezena} \nCentena: {centena} \n{milhar}")