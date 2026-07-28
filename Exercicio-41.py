# 41.	Mostre todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7.

#Declarar as váriaveis
d1: int = 0
d2: int = 0
#Inicio
d1 = 6
d2 = 1
while (d2 <= 6):
    print ("1° dado",d1,"+ 2° dado",d2,"= 7")
    d1 -= 1
    d2 += 1
#Fim