altura_pessoa = float(input("Quanto de altura você tem? (m): "))
sombra_pessoa = float(input("Tamanho da sombra da pessoa (m): "))
s_predio = float(input("Tamanho da sombra do prédio (m): "))
a_predio = (s_predio * altura_pessoa) / sombra_pessoa
print(f"Altura do prédio: {a_predio}m")