# Alunos: Gabriel Benito Beting - RGA:202219060613 e Jecelen Adriane Campos - RGA: 202219060095
import time
import BottomUP_cut as btuCut 
import auxFunctions as aux
import greedy_cut as greedy


def cutRod (inicio, fim, step): # inc = tamanho inicial da entrada/ fim = fim da entrada/  
                                # stp = intervalo entre tamanhos de entrada
        
    aux.headder()
    for tamanhoTora in range(inicio, fim + 1, step):

        #Vetor (tamanho = tamanho da tora) de preços aleatórios de (1 a 10).
        prices = aux.generate_prices(tamanhoTora)


        #cálculos referentes ao algoritmo dinâmico
        startDP = time.time() 
        solutionDP = btuCut.bottom_up_cutRod(prices,tamanhoTora)
        stopDP = time.time()
        timeDP = stopDP -startDP

        #Cálculos referentes ao algoritmo guloso
        starGreedy = time.time()
        solutionGR = greedy.greedyCut(prices, tamanhoTora)
        stopGreedy = time.time()
        timeGreedy = stopGreedy - starGreedy


        #Cálculo da porcentagem do Greedy em relação ao Dinâmico
        percent = (solutionGR/solutionDP) * 100


        print(f"{tamanhoTora:4}    {solutionDP:6}    {timeDP:.6f}  {solutionGR:6}    {timeGreedy:.6f}   {percent:.1f}")



#Rodando o algoritmo completo
cutRod(60, 100, 10)
