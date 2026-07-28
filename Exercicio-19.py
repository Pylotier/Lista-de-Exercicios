# 19.	Receba 2 valores reais. Calcule e mostre o maior deles.

#Declarar as váriaveis
n1: float = 0
n2: float = 0
#Inicio
n1 = float(input("Digite o 1° número:"))
n2 = float(input("Digite o 2° número:"))

if (n1 > n2):
    print("O 1°número:",n1,"é maior do que o 2°número",n2)
elif (n2 > n1):
    print("O 2°número:",n2,"é maior do que o 1°número",n1)
else:
    print("Números iguais")
#Fim