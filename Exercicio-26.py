# 26.	Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

#Declarar as váriaveis
n1: int = 0
n2: int = 0
#Inicio
n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))

if (n1 > n2):
    if (n1 % n2 == 0):
        print(n1, "é multiplo de", n2)
    else:
        print(n1, "não é multiplo de", n2)
else:
    if (n2 % n1 == 0):
        print(n2, "é multiplo de", n1)
    else:
        print(n2, "não é multiplo de", n1)
#Fim