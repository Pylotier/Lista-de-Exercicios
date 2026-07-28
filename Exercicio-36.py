# 36.	Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

#Declarar as váriaveis
n: int = 0
res: float = 0
montante: int = 0
fatorial: int = 0
#Inicio
n = int(input("Digite o número para o cálculo em série: "))

fatorial = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        fatorial *= j
        print(fatorial)
    print("=====")
    montante += 1/fatorial
    fatorial = 1
res = 1 + montante
print("Resultado do cálculo:", res)
#Fim