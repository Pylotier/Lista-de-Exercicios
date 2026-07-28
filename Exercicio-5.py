#Declaração de variáveis
A: int = 0
B: int = 0
C: int = 0
delta: float = 0
resPositivo: float = 0.0
resNegativo: float = 0.0
#Início
A = int(input("Digite o valor do coeficiente A:"))
B = int(input("Digite o valor do coeficiente B:"))
C = int(input("Digite o valor do coeficiente C:"))

if (B==A and A>2 and A<=3):{

}

delta = B**2 - 4*A*C
delta = delta**0.5
print(delta)
resPositivo = (-B+delta)/ (2*A)
resNegativo = (-B-delta)/ (2*A)
print("Resultado positivo:", resPositivo, "e negativo:", resNegativo)
#Fim
