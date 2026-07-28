#Declaração de variáveis
catetoOPosto: float = 0.0
catetoAdjacente: float = 0.0
hipotenusa: float = 0.0
#Início
catetoAdjacente = float(input("Digite o valor do cateto adjacente: "))
catetoOPosto = float(input("Digite o valor do cateto oposto: "))

hipotenusa = (catetoAdjacente**2 + catetoOPosto**2)**0.5

print("A hipotenusa é:", hipotenusa)
#Fim