#Algoritmo guloso (greedy) para resolver o corte da tora

#é possível deixar 3 tipos de return
    # 1 - "return cortes, valor" nesse caso a função devolve o tamanho dos cortes feitos e valor arrecadado
    # 2 - "return cortes"
    # 3 - "return valor"

def greedyCut(p, n): # "p" representa o vetor de preços e "n" o tamanho da tora
    cortes = []
    valor = 0
    
    while n > 0:
        melhor_corte = 0
        melhor_valor_por_unidade = 0
        
        for i in range(1, n+1):
            valor_por_unidade = p[i-1] / i
            if valor_por_unidade > melhor_valor_por_unidade:
                melhor_valor_por_unidade = valor_por_unidade
                melhor_corte = i
        
        cortes.append(melhor_corte-1)
        n -= melhor_corte
    
    for i in range(0, len(cortes)):     #for usado para calcular o valor total arrecadado
        valor += p[cortes[i]]

    
    return valor      #retornando uma lista com o tamanho dos cortes que foram feitos / o valor total referente a tais cortes



"""
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # p[i] é o preço do corte de tamanho i
n = int(input("Digite o tamanho ")) # Tamanho da tora
valor = greedyCut(p, n)
print(greedyCut(p, n))
"""

