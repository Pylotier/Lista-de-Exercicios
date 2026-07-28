# 18.	Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

#Declarar as váriaveis
n1: int = 0
n2: int = 0
dif: int = 0
#Inicio
n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))

if (n1 == n2):
    print("Números iguais")
elif (n1 > n2):
    res = n1 - n2
    print("A diferença entre",n1,"e",n2,"é:",res)
else:
    res = n2 - n1
    print("A diferença entre",n2,"e",n1,"é:",res)
#Fim