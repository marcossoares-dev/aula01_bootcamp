premio = 1000
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
bonus = float(input("Digite o bonus: "))/100

valor = (salario + (salario * bonus) + premio)

#print(nome+" o valor a receber é de " + str(valor))

print(f"O usuario {nome} possui o bonus de {valor}")