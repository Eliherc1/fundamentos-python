#1. Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
#Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

def big(x):
    for i in range(0,len(x)):
        if x[i] > 0 :
            x[i] = "Big"
    return x

a = [-11, 12, -13, -9, 7, 15]
print(big(a))

#2. Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
#Ejemplo: count_positives([- 1, 1, 1,1 ]) cambia la lista original a [-1, 1, 1, 3] y la devuelve
#Ejemplo: count_positives([1, 6, -4, -2, -7, -2]) cambia la lista a [1, 6, -4, -2, -7, 2] y la devuelve

def contPositivos(x):
    positivos=0
    for i in range(0,len(x)):
        if x[i] > 0 :
            positivos=positivos+1
    x[len(x)-1]=positivos
    return x;

a = [-11, -12, 13, -9, 7, 15]
print(contPositivos(a))

#3. Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
#Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
#Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def sumaArr(lista):
    suma=0
    for valor in lista:
        suma += valor
    return suma
print(sumaArr([5,8,6,9,20]))

#4. Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
#Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def promedio(a):
    suma=0
    for i in range(0,len(a)):
        suma += a[i]
    return suma/len(a)

a = [2, 6, 8, 10]
print(promedio(a))

#5. Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
#Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
#Ejemplo: longitud ([]) debería devolver 0

def longitud(lista):
    return len(lista)

a = [2, 6, 8, 10]
print(longitud(a))


#6. Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
#Ejemplo: mínimo ([]) debería devolver False

def minimo(a):
    if len(a)==0:
        return False
    else:
        valor= a[0]
        for i in range(0,len(a)):
            if a[i] < valor:
                valor = a[i]
        return valor

a = []
print(f"El valor Minimo de la lista es: {minimo(a)}")

#7. Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
#Ejemplo: máximo ([]) debería devolver False

def maximo(a):
    if len(a)==0:
        return False
    else:
        valor= a[0]
        for i in range(0,len(a)):
            if a[i] > valor:
                valor = a[i]
        return valor

a = [5,8,6,33,56]
print(f"El valor Maximo de la lista es: {maximo(a)}")

#8. Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
#Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}

def analisis(x):
    suma= 0
    minimo=x[0]
    maximo=x[0]
    for i in range(0,len(x)):
        suma = suma + x[i]
        if x[i] < minimo:
            minimo=x[i]
        else: 
            if x[i] > maximo:
                maximo=x[i]
    dicc = { "Suma": suma, "Minimo": minimo, "Maximo": maximo, "Promedio": suma/len(x),"Longitud": len(x) }
    return dicc

x = [11, 12, 3, 20, 7, 15, 88]
print(analisis(x))



#9. Lista inversa : crea una función que tome una lista y la devuelva con los 
# valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
#Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

def Inversa(x):
    for i in range(0,int(len(x)/2)):
        primero= x[i]
        ultimo= x[(len(x)-1)-i]
        x[i]=ultimo
        x[(len(x)-1)-i]= primero
    return x
a = [11, 13, 15, -9, 7, 2, 3, 4, 6, 8, 10]
print(Inversa(a))

















