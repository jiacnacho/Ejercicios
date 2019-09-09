"""     Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
        a)	La cantidad de valores negativos ingresados.
        b)	La cantidad de valores positivos ingresados.
        c)	La cantidad de múltiplos de 15.
        d)	El valor acumulado de los números ingresados que son pares. 
 """


contador=0
countneg=0
numeros=0
countpos=0
for i in range(1,10,1):
    numeros=input('Ingrese un numero')
    if (numeros<=0):
        countneg+=1
    elif (numeros >=0):
        countpos+=1

print(u"Hay", countneg, "numeros negativos.")
print(u"Hay", countpos, "numeros positivos.")

