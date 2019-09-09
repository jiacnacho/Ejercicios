tablas=0
multitablas=0

tablas=int(input('Ingrese un numero para saber su tabla'))
print(u"El numero ingresado fue", tablas)
for i in range(1,11,1):
    multitablas= tablas*i
    print(multitablas)

