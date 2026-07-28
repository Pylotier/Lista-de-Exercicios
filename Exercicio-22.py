# 22.	Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

#Declarar as váriaveis
n1: float = 0.0
n2: float = 0.0
#Inicio
n1 = float(input("Digite o 1° número: "))
n2 = float(input("Digite o 2° número: "))

if (n1 > n2):
    print("1°",n1,",2°",n2)
else:
    print("1°",n2,",2°",n1)
#Fim