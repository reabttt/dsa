from Queues.cola import Cola
from Stacks.pila import Pila
from List.lista import Lista 

# punto 1 
def barrido(arr,indice=0):
    if indice<len(arr):
        print(arr[indice])
        barrido(arr,indice+1)

def busqueda(arr,indice=0):
    if indice<len(arr):
        if arr[indice] == 'yoda':
            return indice
        else:
            return busqueda(arr,indice+1)
    else:
        return -1

starwars = ['luke skywalker','yoda','darth vader','r2d2']
barrido(starwars)
indice = busqueda(starwars)
if indice != -1:
    print(f'yoda esta en la posicion {indice}')
else:
    print('yoda no se encuentra')


# punto 2 
cola = Cola()
cola1 = Cola()
pila = Pila()

notificaciones = [
        {'app':'facebook','hora':'14:30','mensaje':'nuevo mensaje de asdasd'},
        {'app':'twitter','hora':'11:30','mensaje':'hola mundo en python'},
        {'app':'telegram','hora':'15:00','mensaje':'asdasda'},
        {'app':'instagram','hora':'11:20','mensaje':'coso'}
        ]
# punto a 
for notificacion in notificaciones:
    cola.arribo(notificacion)
while not cola.es_vacia():
    data = cola.atencion()
    if data['app'] != 'facebook':
        cola1.arribo(data)
while not cola1.es_vacia():
    cola.arribo(cola1.atencion())
# punto b 
for i in range(cola.tamano()):
    data = cola.mover_al_final()
    if data['app'] == 'twitter' and 'python' in data['mensaje']:
        print(data['hora'],data['app'],data['mensaje'])
# punto c 
for i in range(cola.tamano()):
    data = cola.mover_al_final()
    if data['app'] == 'instagram':
        pila.apilar(data)
print(f'cantidad de notificaciones en la pila {pila.tam()}')
while not cola.es_vacia():
    print(cola.atencion())


# punto 3
class Personaje:
    def __init__(self,nombre):
        self.nombre = nombre
    def __str__(self):
        return f'{self.nombre}'

lista = Lista()
personajes = [
        {'name':'iron man'},
        {'name':'hulk'},
        {'name':'thor'},
        {'name':'scalet witch'},
        {'name':'loki'},
        ] 

for valor in personajes:
    lista.insertar(Personaje(valor['name'].title()),'nombre')
print('')
lista.barrido()
# punto a 
data = lista.buscar('Thor','nombre')
if data is not None:
    print(f'\nThor esta en la posicion {data}')
else:
    print('\nThor no esta en la lista')
# punto b 
data = lista.buscar('Scalet Witch','nombre')
if data is not None:
    lista.modificar_valor('Scalet Witch', 'Scarlet Witch','nombre')
    print('se modifico el nombre de Scalet Witch')
else:
    print('Scalet Witch no se encuentra en la lista')
# punto c
personajes_aux = ['Black Widow','Hulk','Rocket Racoonn','Loki']
for personaje in personajes_aux:
    if lista.buscar(personaje,'nombre') is None: # si no lo encuentra que lo agregue
        lista.insertar(personaje,'nombre')
print('se agregaron nuevos personajes a la lista')
# punto d 
print('barrido ascendente de la lista de personajes')
lista.barrido()
print('barrido descendente de la lista de personajes')
for i in range(lista.tam()-1,-1,-1):
    data = lista.elemento_indice(i)
    print(data)
# punto e 
posicion = 7
data = lista.elemento_indice(posicion)
if data is not None:
    print(data)
else:
    print(f'no hay personaje en la posicion {posicion}')


# nada



