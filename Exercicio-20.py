# 20.	Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.

#Declarar as váriaveis
A: int = 0
B: int = 0
C: int = 0

delta: float = 0.0
quadradoDelta: float = 0.0
respostaRaizNegativa: float = 0.0
respostaRaizPositiva: float = 0.0
respostaUmaRaiz: float = 0.0
#Inicio
A = int(input("Digite o coeficiente A:"))
B = int(input("Digite o coeficiente B:"))
C = int(input("Digite o coeficiente C:"))

delta = B**2 - 4*A*C
quadradoDelta = delta**0.5
if (delta < 0):
    print("Não existe raizes")
elif (quadradoDelta == 0):
    respostaUmaRaiz = -B/(2*A)
    print("Resultado com apenas uma raiz:", respostaUmaRaiz)
else:
    respostaRaizPositiva = (-B + quadradoDelta) / (2*A)
    respostaRaizNegativa = (-B - quadradoDelta) / (2*A)
    print("Resultado do x1(positivo):",respostaRaizPositiva)
    print("Resultado do x2(negativo):",respostaRaizNegativa)
#Fim