# 32.	Receba um número inteiro. Calcule e mostre o seu fatorial.

#Declarar as váriaveis
n: int = 0
res: int = 0
montante: int = 1
#Inicio
n = int(input("Digite um número para ver o fatorial dele: "))

for i in range(1, n+1, 1):
    montante *= i
    print(montante)
res += montante
print("Fatorial de",n,"é",res)
#Fim