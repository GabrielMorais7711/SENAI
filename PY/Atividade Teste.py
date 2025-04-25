#@title Atividade 4
# Ler o nome e a idade da pessoa
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Calcular os dias de vida (considerando 365 dias por ano)
dias_de_vida = idade * 365

# Exibir o resultado
print(f"{nome.upper()}, VOCÊ JÁ VIVEU {dias_de_vida} DIAS")