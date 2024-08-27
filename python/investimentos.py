valor_inicial = 30000
retorno_mensal = 0.01
valor_final = valor_inicial

for _ in range(120):
    ganho_mensal = valor_final * retorno_mensal
    valor_final += ganho_mensal
    valor_final = valor_final + 1000
    
print(f'Retorno mensal: {ganho_mensal:.2f} reais.')
print(f'O valor final após 5 anos, reinvestindo os ganhos mensais, seria de aproximadamente {valor_final:.2f} reais.')
