# 37.	Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.

#Declarar as váriaveis
n: int = 0
nAnterior: int = 0
nPresente: int = 0
nProximo: int = 0
#Inicio
n = int(input("Digite qual número de Fibonacci quer chegar: "))

nPresente = 1

for i in range(1, n+1):
    print(i,"°número:",nPresente)
    nProximo = nAnterior + nPresente 
    nAnterior = nPresente
    nPresente = nProximo
res = nPresente
#Fim