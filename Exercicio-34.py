# 34.	Receba um número. Calcule e mostre os resultados da tabuada desse número.

#Declarar as váriaveis
n: int = 0
#Inicio
n = int(input("Digite o número da tabuada: "))
for i in range(1,11,1):
    print(n,"x",i,"=",n*i)
#Fim