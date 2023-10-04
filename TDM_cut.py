#Resolvendo o problema do corte da tora com programação Dinâmica

#PD - Top Down With Memorization

import time

def memorized_cut_rod(p, n):  #p é o vetor de preço e n o tamanho da tora
    r = [-999] * (n+1)   #inicializando um vetor de n + 1 elementos, cada um com o valor simbólico (-999)
    return memorized_cut_rod_aux(p, n, r)


def memorized_cut_rod_aux(p, n, r):
    if ( r[n] >= 0 ):
        return r[n]
    
    elif ( n == 0 ) :
        q = 0

    else: 
        q = -999
    
        for i  in range(n):
            q = max(q, p[i] + memorized_cut_rod_aux(p, n-i-1, r))  # q vai representar o lucro máximo


    r[n] = q
    return q      #retorna o valor máximo que pode ser arrecadado com uma tora de tamanho n



''' 
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = int(input("Digite o tamanho da tora a ser cortada: "))
result = memorized_cut_rod(p,n)
print(f"o valor máximo de arrecadação em tora de tamanho {n} é : {result}")  
'''

