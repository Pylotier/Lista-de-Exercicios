# 33.	Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.

#Declarar as váriaveis
n: int = 0
res: float = 0
montante: int = 0
#Inicio
n = int(input("Digite o número para o cálculo em série: "))

for i in range(2, n+1, 1):
    print(1, "/", i)
    montante += 1/i
res = 1 + montante
print("Resultado do cálculo:", res)
#Fim