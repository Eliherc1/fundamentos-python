#Actualiza los valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ] 

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
def cambio(xlista):
    print(xlista)
    for i in range (len(xlista)):
        for ii in range(len(xlista[i])):
            if xlista[i][ii]==10:
                xlista[i][ii]=15
    return xlista

x = [ [5,2,3], [10,8,9] ] 
print(cambio(x))

#Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
def listaEst(students):
    for est in students:
        #print(est['last_name'])
        if est['last_name'] == 'Jordan':
            est['last_name']='Bryant'
    return  students

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
newList = listaEst(students)
print(newList)


#En el directorio sports_directory, cambia 'Messi' a 'Andres'

#sports_directory['soccer'][0]= 'andres'  #cambiar directo el nombre

def deportes(sports_directory):
    for valor in sports_directory:
        for sp in range(len(sports_directory[valor])):
            if sports_directory[valor][sp]=='Messi':
                sports_directory[valor][sp]= 'Andres'
    print(sports_directory)
       

##diccionario
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
newArreglo = deportes(sports_directory)
print(newArreglo)



#Camba el valor 20 en z a 303

def cambiar(lista):
    for valor in lista:
        #print(valor['y'])
        valor['y']=303
    return lista
          

z = [ {'x': 10, 'y': 20} ]
print(cambiar(z))


def listaEst(students):
    for est in students:
        #print(est['last_name'])
        if est['last_name'] == 'Jordan':
            est['last_name']='Bryant'
    return  students

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
newList = listaEst(students)
print(newList)

#2. Itera a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, 
# la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. 
# Por ejemplo, dada la siguiente lista:

def iterateDictionary(students):
    for est in students:
        print(f"first_name - {est['first_name']} , last_name - {est['last_name']}")

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 


#3. Obtén valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
# la función imprima el valor almacenado en esa clave para cada diccionario. 
# Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:

def iterateDictionary2(students):
    for est in students:
        print(est['first_name'])

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary2(students) 

#Y iterateDictionary2('last_name', students) debería generar:

def iterateDictionary2(students):
    for est in students:
        print(est['last_name'])

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary2(students) 

#4. Itera a través de un diccionario con valores de listas
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, imprima el nombre de cada clave 
# junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:


def printInfo(lista):
    for valor in lista:
        print(len(valor), valor)
        #print(valor)
        for ciudad in range(len(lista[valor])):
            print(lista[valor][ciudad])       

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)