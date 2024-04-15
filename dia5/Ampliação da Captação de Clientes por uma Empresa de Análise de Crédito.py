import re

def main():
    ve = float(input("Digite o valor do seu empréstimo: "))
    sl = float(input("Digite seu Salário Líquido do Solicitante: "))
    qm = int(input("Digite a quantidade de Meses para Pagamento: "))
    nc = str(input("Digite seu Nome Completo: "))
    nc_lm = nc.title()

    valida = True
    while valida:
        cpf = input("Digite seu Número do CPF: ")
        cpf = re.sub(r'\D', '', cpf)
        if len(cpf) != 11:
            print("CPF inválido! Digite um cpf com 11 números.")
        else:
            valida = False

    validapt2 = True
    while validapt2:
        tel = input("Digite seu Número de Telefone para Contato: ")
        tel = re.sub(r'\D', '', tel)
        if len(tel) != 11:
            print("Número de telefone inválido! Digite um Telefone com 11 digitos e apenas com números.")
        else:
            validapt2 = False

    validapt3 = True
    while validapt3:
        cep = input("Digite seu cep: ")
        cep = re.sub(r'\D', '', cep)
        if len(cep) != 8:
            print("CEP inválido! Digite um CEP com 8 digitos.")
        else:
            validapt3 = False

    validapt4 = True
    while validapt4:
        email = input("Digite seu email: ")
        if not email.endswith('@gmail.com'):
            print("O endereço de email deve ser obrigatoriamente gmail!")
            email = email.lower()
        else:
            validapt4 = False

    End = input("Digite seu Endereço: ")

    print(f"Nome: {nc_lm}\nNúmero do CPF: {cpf}\nE-mail: {email}\nTelefone: {tel}\nEndereço: {End}\nCEP: {cep}\nSalário Líquido do Solicitante: {sl}\nValor do empréstimo: {ve}\nQuantidade de meses para pagamento: {qm}")
    pres = ve/qm
    if pres <= sl * 0.3:
        print(f"Seu empréstimo foi aprovado! O valor da sua prestação é de: {pres}")
    else:
        print("Seu empréstimo foi negado!")

main()
