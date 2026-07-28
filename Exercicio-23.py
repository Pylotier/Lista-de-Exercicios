# 23.	Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.

#Declarar as váriaveis
n1: float = 0.0
n2: float = 0.0
n3: float = 0.0
n4: float = 0.0
#Inicio
n1 = float(input("Digite o 1° número: "))
n2 = float(input("Digite o 2° número: "))
n3 = float(input("Digite o 3° número: "))
n4 = float(input("Digite o 4° número: "))

if (n4 > n3):
    print("1°",n1,"2°",n2, "3°",n3,"#4°",n4)
elif (n4 >= n2 and n4 < n3):
    print("1°",n1,"2°",n2, "#3°",n4,"4°",n3)
elif (n4 >= n1 and n4 < n2):
    print("1°",n1,"#2°",n4, "3°",n2,"4°",n3)
else:
    print("#1°",n4,"2°",n1, "3°",n2,"4°",n3)
#Fim