#1. Básico : imprime todos los enteros del 0 al 150.
for x in range (150+1):
    print(x)
#2. Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for x in range (5,1000+1,5):
    print(x)
#3. Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" 
# en su lugar. Si es divisible por 10, imprima "Coding Dojo".
for x in range (1,100+1):
    if x % 10==0:
        print("Coding Dojo")
    elif  x % 5==0 :
        print("Coding")
    else:
        print(x)

#4. ¡Uf, Eso es bastante grande!: 
# suma enteros impares de 0 a 500,000 e imprime la suma final.
suma=0
for x in range (1,500000+1,2):
    suma = suma + x
print(suma)


#5. Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
for x in range (2018,0-1,-4):
    print(x)


#6. Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por 
# highNum, imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, 
# el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)

lowNum=2
highNum=21
mult=3
for i in range(lowNum, highNum+1,1):
    if i % mult==0:
        print(i)
