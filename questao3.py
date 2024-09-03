import json

# Carregar dados do faturamento a partir de um arquivo JSON
with open('questao3.json', 'r') as file:
    dados = json.load(file)

faturamentos = [dia["valor"] for dia in dados["faturamento"] if dia["valor"] > 0]

menor_valor = min(faturamentos)
maior_valor = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)
dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")