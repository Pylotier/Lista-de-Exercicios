# 42.	Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99

#Declarar as váriaveis
numerador:int = 0
denominador:int = 0
proximoDenominador: int = 0
montante: int = 0
#Inicio
numerador = 2
denominador = 3

for i in range(2, 50+1, 1):

    div = i/denominador
    print(i,"/",denominador)
    montante += div
    denominador = 3 + 2 * i-2

print("Resultado do cálculo:",montante+1)
#Fim