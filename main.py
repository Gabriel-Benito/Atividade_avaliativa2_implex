# Alunos: Gabriel Benito Beting - RGA:202219060613 e Jecelen Adriane Campos - RGA: 202219060095
import time
import TDM_cut as dp
import auxFunctions as aux
import greedy_cut as greedy



#prices[n] representa o valor de uma tora tamanho n
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
prices1 = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def cutRod (inicio, fim, step): # inc = tamanho inicial da entrada/ fim = fim da entrada/  
                            # stp = intervalo entre tamanhos de entrada
    aux.headder()
    for tamanhoTora in range(inicio, fim + 1, step):

        #cálculos referentes ao algoritmo dinâmico
        startDP = time.time() 
        solutionDP = dp.memorized_cut_rod(prices,tamanhoTora)
        stopDP = time.time()
        timeDP = stopDP -startDP

        #Cálculos referentes ao algoritmo guloso
        starGreedy = time.time()
        solutionGR = greedy.greedyCut(prices1, tamanhoTora)
        stopGreedy = time.time()
        timeGreedy = stopGreedy - starGreedy


        #Cálculo da porcentagem do Greedy em relação ao Dinâmico
        percent = (solutionGR/solutionDP) * 100


        print(f"   {tamanhoTora}    {solutionDP}    {timeDP:.6f}  {solutionGR}    {timeGreedy:.6f}   {percent:.2f}")






#Rodando o algoritmo completo
cutRod(5,50, 5)
    
