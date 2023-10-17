#Programação Dinâmica 
#Corte da tora com bottom up 

def bottom_up_cutRod(prices, size):
    r = [None] * (size+1)
    r[0] = 0

    for j in range(1, size+1):
        profit = float('-inf')
        for i in range(1, j+1):
            profit = max(profit, prices[i-1] + r[j-i])

        r[j] = profit
    return r[size]



'''TESTE DE FUNCIONAMENTO
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = int(input("Digite o tamanho da tora a ser cortada: "))
result = bottom_up_cutRod(p,n)
print(f"o valor máximo de arrecadação em tora de tamanho {n} é : {result}")
'''