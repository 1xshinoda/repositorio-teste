import json

def calcular_faturamento(faturamento):
    
    faturamento_validos = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

    if not faturamento_validos:
        return None, None, 0  

    menor = min(faturamento_validos)
    maior = max(faturamento_validos)
    media = sum(faturamento_validos) / len(faturamento_validos)
    
    dias_acima_da_media = sum(1 for valor in faturamento_validos if valor > media)

    return menor, maior, media, dias_acima_da_media

''
with open('faturamento.json', 'r') as file:
    data = json.load(file)


menor, maior, media, dias_acima = calcular_faturamento(data['faturamento'])

if menor is not None and maior is not None:
    print(f"Menor faturamento: {menor}")
    print(f"Maior faturamento: {maior}")
    print(f"Média mensal: {media:.2f}")
    print(f"Número de dias acima da média: {dias_acima}")
else:
    print("Não há dias com faturamento válido para calcular.")