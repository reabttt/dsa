from pila import Pila
from cola import Cola
from lista import Lista

pila = Pila()
cola = Cola()
lista = Lista()

# punto 1 
def contar_palabra(arr,palabra):
    if not arr:
        return 0
    else:
        if arr[0] == palabra:
            return 1 + contar_palabra(arr[1:],palabra)
        else:
            return contar_palabra(arr[1:],palabra)

palabras = ['hola','casa','uva','té','hola','python','perro']
palabra = 'hola'
cantidad = contar_palabra(palabras,palabra)
print(f'la palabra {palabra} aparece {cantidad} veces en el vector')
print('')


# punto 2 
class Personaje:
    def __init__(self,superheroe,nombre,grupo,aparicion):
        self.superheroe = superheroe
        self.nombre = nombre
        self.grupo = grupo
        self.aparicion = aparicion 
    def __str__(self):
        return f'{self.superheroe} {self.nombre} {self.grupo} {self.aparicion}'
    
personajes = [
        {'hero':'iron man','name':'tony stark','group':'vengadores','year':1963},
        {'hero':'capitana marvel','name':'carol danvers','group':'vengadores','year':1986},
        {'hero':'star lord','name':'peter quill','group':'guardianes de la galaxia','year':1975},
        {'hero':'mujer invisible','name':'susan storm','group':'cuatro fantasticos','year':1961},
        {'hero':'vlank widow','name':'natasha romanoff','group':'vengadores','year':1964},
        {'hero':'groot','name':'groot','group':'guardianes de la galaxia','year':1962},
        {'hero':'rocket raccoon','name':'rocket raccoon','group':'guardianes de la galaxia','year':1960},
        {'hero':'hulk','name':'bruce banner','group':'','year':1962}, 
        {'hero':'mr. fantastico','name':'reed richards','group':'cuatro fantasticos','year':1961},
        {'hero':'la cosa','name':'Ben Grimm','group':'cuatro fantasticos','year':1961},
        {'hero':'mantis','name':'','group':'guardianes de la galaxia','year':1960},
        {'hero':'nebula','name':'nebula','group':'guardianes de la galaxia','year':1970},
        {'hero':'gamora','name':'','group':'guardianes de la galaxia','year':1968},
        {'hero':'drax el destructor','name':'drax','group':'guardianes de la galaxia','year':1970},
        {'hero':'yondu udonta','name':'','group':'guardianes de la galaxia','year':1969},
        {'hero':'ant man','name':'hank pym','group':'vengadores','year':1962},
        {'hero':'scarlet witch','name':'wanda maximoff','group':'vengadores','year':1961},
        {'hero':'black panther','name':'','group':'vengadores','year':1961},
        {'hero':'capitan america','name':'steve rogers','group':'vengadores','year':1961},
        {'hero':'vision','name':'','group':'vengadores','year':1961},
        ]
for personaje in personajes:
    lista.insertar(Personaje(personaje['hero'].title(),
                             personaje['name'].title(),
                             personaje['group'].title(),
                             personaje['year'],
                             ),'superheroe')
lista.barrido()
print('')
# punto a 
data = lista.elemento_indice(lista.buscar('Capitana Marvel','superheroe'))
if data is not None:
    print(f'{data.superheroe} se encuentra en la lista')
else:
    print(f'{data.superheroe} no esta en la lista')
# punto b 
for i in range(lista.tam()):
    data = lista.elemento_indice(i)
    if data.grupo == 'Guardianes De La Galaxia':
        cola.arribo(data)
print(f'cantidad de personajes de Guardianes de la Galaxia almacenados en la cola {cola.tamano()}')
# punto c 
print('\nbarrido descendente de Guardianes De La Galaxia')
for i in range(lista.tam()-1,-1,-1):
    data = lista.elemento_indice(i)
    if data.grupo == 'Guardianes De La Galaxia':
        print(data)
print('\nbarrido descendente de Cuatro Fantasticos')
for i in range(lista.tam()-1,-1,-1):
    data = lista.elemento_indice(i)
    if data.grupo == 'Cuatro Fantasticos':
        print(data)
# punto d 
print(f'\npersonajes cuya aparicion es mayor a 1960')
for i in range(lista.tam()):
    data = lista.elemento_indice(i)
    if data.aparicion > 1960:
        print(f'{data.superheroe} {data.aparicion}')
# punto e
data = lista.elemento_indice(lista.buscar('Vlank Widow','superheroe'))
if data is not None:
    data.superheroe = 'Black Widow'
    print('\nse modifico a Vlank Widow')
else:
    print('\n{data.superheroe} no esta en la lista')
lista.reordenar('superheroe')
lista.barrido() 

# punto f 
lista_aux = Lista()
personajes_aux = [
        {'hero':'black cat','name':'','group':'','year':1963},
        {'hero':'hulk','name':'bruce banner','group':'','year':1962},
        {'hero':'groot','name':'groot','group':'guardianes de la galaxia','year':1962}, 
        {'hero':'rocket raccoon','name':'rocket raccoon','group':'guardianes de la galaxia','year':1960}, 
        {'hero':'loki','name':'','group':'','year':1960},
        ]
for personaje in personajes_aux:
    lista_aux.insertar(Personaje(personaje['hero'].title(),
                             personaje['name'].title(),
                             personaje['group'].title(),
                             personaje['year'],
                             ),'superheroe')

for i in range(lista_aux.tam()):
    nuevo = lista_aux.elemento_indice(i)
    indice = lista.buscar(nuevo.superheroe,'superheroe')
    if indice is None:
        lista.insertar(data,'superheroe')
print('\nse insertaron nuevos personajes a la lista')
lista.barrido()

# punto g
print('\nnombres de los personajes que comienzan con C, P o S')
for i in range(lista.tam()):
    data = lista.elemento_indice(i)
    if data.superheroe[0] in ['C','P','S']:
        print(data.superheroe)

# punto h 
# cargar mas personajes

# punto 3 
class Mision:
    def __init__(self,planeta,capturado,costo):
        self.planeta = planeta
        self.capturado = capturado
        self.costo = costo
    def __str__(self):
        return f'{self.planeta} {self.capturado} {self.costo}'

misiones = [
        {'planet':'Tatooine','name':'Jabba the Hutt','price':150},
        {'planet':'-','name':'Yoda','price':200},
        {'planet':'Endor','name':'Leila Organa','price':100},
        {'planet':'Tatooine','name':'Han Solo','price':300}, 
        {'planet':'Endor','name':'Obi Wan Kenobi','price':300},
        ]

for mision in misiones:
    pila.apilar(Mision(mision['planet'],
                       mision['name'],
                       mision['price'],
                       ))
pila1 = Pila() 
creditos = 0 
mision = 1 
encontrado = False
print('\nplanetas visitados en el orden que realizo las misiones')
while not pila.es_vacia():
    data = pila.desapilar()
    pila1.apilar(data)
    print(f'{data.planeta}')
print('')
while not pila1.es_vacia():
    pila.apilar(pila1.desapilar())
while not pila.es_vacia():
    data = pila.desapilar()
    creditos += data.costo
    if data.capturado == 'Han Solo':
        print(f'{data.capturado} fue capturado en la mision {mision} en {data.planeta}')
    mision+=1 
print(f'total de creditos recaudados {creditos}')



























































