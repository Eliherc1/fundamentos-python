#1
def a():
    return 5
print(a())
# salida sera: 5

#2
def a():
    return 5
print(a()+a())

# salida sera: 10

#3
def a():
    return 5
    return 10
print(a())

# salida sera: 5

#4
def a():
    return 5
    print(10)
print(a())

# salida sera: 5

#5
def a():
    print(5)
x = a()
print(x)

# salida sera: 5 y sin valores ya que al llamar la funcion no tiene valor.

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

# salida sera: 3 y 5

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

# salida sera: 25 pero como string(2 y 5) ya que en el return se esta cambiando el tipo de dato a str.

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

# salida sera: 100 por el primer print y luego entra al if como 100 es mayor a 10 imprime 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))


# salida sera: 7 ya que 2 es menor a 3, luego 14 ya que 5 es mayor a 3 y por ultimo se vuelve a repetir 7 y 14 pero se suman ambos dando 21


#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# salida sera: 8 se suma 3+5 valores de entrada de la funcion

#11
b = 500
print(b) #1er 500
def a():
    b = 300
    print(b) 
print(b) #2do 500
a() #entra a la funcion e imprime 300
print(b) #3er 500

# salida sera: 500 500 300 500

#12
b = 500
print(b) #1er 500
def a():
    b = 300
    print(b)
    return b
print(b) # 2do 500
a() # entra a la funcion e imprime 300 el return no lo toma ya que no se esta indicando
print(b) #3ro 500

# salida sera: 500 500 300 500

#13
b = 500
print(b) #1er 500
def a():
    b = 300
    print(b)
    return b
print(b) #2do 500
b=a() # imprime 300 dentro de la funcion
print(b) #imprime 300

# salida sera: 500 500 300 300

#14
def a():
    print(1) #imprime 1
    b()     #llama a la funcion b imprime 3
    print(2) #imprime 2
def b():
    print(3)
a()

# salida sera: 1 3 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a() #imprime 1 , luego como x es igual la funcion b imprime 3 y retorna 5
print(y) #10 por el return de la funcion a

# salida sera: 1 3 5 10