#Si no se proporcionan argumentos, la función debería devolver un entero aleatorio entre 0 y 100.
#Si solo se proporciona un número máximo, la función debe devolver un número entero aleatorio entre 0 y el número máximo.
#Si solo se proporciona un número mínimo, la función debe devolver un número entero aleatorio entre el número mínimo y 100
#Si se proporcionan un número mínimo y máximo, la función debe devolver un número entero aleatorio entre esos 2 valores.


import random
def randInt(min=0, max=100):
    num = random.random()*(max-min)+min
    return round(num)
print(randInt())
#debería imprimir un número aleatorio entre 0 a 100
print(randInt(max=50))
# debería imprimir un número aleatorio entre 0 a 50
print(randInt(min=50))
#  # debería imprimir un número aleatorio entre 50 a 100
print(randInt(min=50, max=500))   
#  # debería imprimir un número aleatorio entre 50 y 500
