# 35.	Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.

#Declarar as váriaveis
n1: int = 0
n2: int = 0
res: int = 0
#Inicio
n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))

if (n1 > n2):
    for i in range(n2+1, n1, 1):
        if (i % 2 != 0):
            # print(i)
            res += i    
    print("A soma dos número impares entre",n1,"e",n2,"é:",res)

elif (n1 < n2):
    for i in range(n1+1, n2, 1):
        if (i % 2 != 0):
            # print(i)
            res += i        
    print("A soma dos número impares entre",n2,"e",n1,"é:",res)
else:
    print("Número iguais")
#Fim