# 45.	Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225

#Declarar as váriaveis
denominador: int = 0
res: int = 0
somaDenominador: int = 0
valorAnterior:int = 0
#Inicio
denominador = 4

for i in range(0, 14):
    somaDenominador = 5+2*i
    print(i+2, "/", denominador)
    denominador = denominador + somaDenominador
    res += i+2/denominador
print("Resultado do cálculo: ", res+1)
#Fim