# 24.	Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

#Declarar as váriaveis
n1: int = 0
respostaMod2 = 0
respostaMod3 = 0
#Inicio
n1 = int(input("Digite um número: "))
respostaMod2 = n1%2
respostaMod3 = n1%3

if (respostaMod2 == 0):
    if (respostaMod2 == respostaMod3):
        print("Divisível por 2 e 3")
    else:
        print("Divisível por 2")
else:
    if (respostaMod3 == 0):
        print("Divisível por 3")
    else:
        print("Não é divisível por 2 nem 3")
#Fim