# 38.	Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.

#Declarar as váriaveis
n: int = 0
maiorNumero: int = 0
menorNumero: int = 0
nAnterior: int = 0
#Inicio
for i in range(1, 100):
    n = int(input("Digite número: "))

    if (n > maiorNumero):
        maiorNumero = n
        if (i == 1):
            menorNumero = maiorNumero
    elif (n < menorNumero):
        menorNumero = n
    nAnterior = n

print("Maior número:",maiorNumero, "/ Menor número:", menorNumero)
#Fim