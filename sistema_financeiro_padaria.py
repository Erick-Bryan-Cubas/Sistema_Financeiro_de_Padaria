# Declarando as variáveis
pao_frances = 0.80
broa = 2.50

# Questionando a quantidade vendida
qtd_paes = int(input('Qual foi a quantidade de pães franceses vendida? '))
qtd_broas = int(input('Qual foi a quantidade de broas vendida? '))

# Calculando o total de vendas
total_paes = (qtd_paes * pao_frances)
total_broas = (qtd_broas * broa)
total_arrecadacao = (total_paes + total_broas)

# Imprimindo o total de arrecadação
print(f"O total arrecadado de paes foi de R${total_paes:.2f} e o total de arrecadação das broas foi de R${total_broas:.2f}")

# Obtendo o percentual das distribuições
insumo = ((total_arrecadacao * 43) / 100)
lucro = (((total_arrecadacao - insumo) * 15)/100)
viagem_europa = ((((total_arrecadacao - insumo)-lucro) * 15) /100)

# Convertendo reais em euros
euro = 4.60
euro_arrecadado = (viagem_europa / euro)

print(f"O total para pagar insumos é de R${insumo:.2f}, o total de lucro obtido é de R${lucro:.2f} e o total de reais convertidos para euros com fins para viagem foi de {euro_arrecadado:.2f}")
