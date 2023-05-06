from lista import Lista

class Superheroe:
    def __init__(self,nombre,aparicion,casa,biografia):
        self.nombre = nombre
        self.aparicion = aparicion
        self.casa = casa
        self.biografia = biografia
    
    def __str__(self):
        return f'{self.nombre} {self.aparicion} {self.casa}, {self.biografia}' 

superheroes = [
        {'name':'batman','year':1939,'comic':'dc','bio':'el caballero de la noche'},
        {'name':'linterna verde','year':1940,'comic':'dc','bio':'orden de las linternas'},
        {'name':'wolverine','year':1974,'comic':'marvel','bio':'garras de adamantium'},
        {'name':'dr. strange','year':1963,'comic':'dc','bio':'cirujano hechicero maestro'},
        {'name':'star lord','year':1986,'comic':'marvel','bio':'...'},
        {'name':'flash','year':1940,'comic':'dc','bio':'el velocista escarlata'},
        {'name':'mujer maravilla','year':1941,'comic':'dc','bio':'guerrera de las amazonas'},
        {'name':'dr. doom','year':1962,'comic':'marvel','bio':'genio inventor'},
        {'name':'capitana marvel','year':1968,'comic':'marvel','bio':'traje azul y rojo'}, 
        {'name':'iron man','year':1963,'comic':'dc','bio':'armadura de alta tecnologia'},
        ]

lista = Lista()
for valor in superheroes:
    lista.insertar(Superheroe(valor['name'],
                              valor['year'],
                              valor['comic'],
                              valor['bio']),'nombre')

lista.barrido()
print('')

# punto a 
nodo = lista.eliminar('linterna verde','nombre')
if nodo:
    print(f'se elimino a {nodo.nombre}')
else:
    print('{nodo.nombre} no esta en la lista')
# punto b 
nodo = lista.elemento_valor('wolverine','nombre')
if nodo:
    print(f'primera aparicion de {nodo.nombre} {nodo.aparicion}')
else:
    print(f'wolverine no esta en la lista')
# punto c 
nodo = lista.elemento_valor('dr. strange','nombre')
if nodo:
    nodo.casa = 'marvel'
    print(f'{nodo.nombre} ahora esta en marvel')
else:
    print(f'dr. strange no esta en la lista')
# punto d 
print('\ntiene la palabra traje o armadura en la bio')
lista.traje_armadua()








