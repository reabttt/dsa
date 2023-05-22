from lista import Lista 
import random 

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
        {'name':'deadpool','year':1991,'comic':'marvel','bio':'...'},
        {'name':'capitana marvel','year':1968,'comic':'marvel','bio':'traje azul y rojo'}, 
        {'name':'iron man','year':1963,'comic':'marvel','bio':'armadura de alta tecnologia'},
        ]

lista = Lista()
for valor in superheroes:
    lista.insertar(Superheroe(valor['name'].title(),
                              valor['year'],
                              valor['comic'],
                              valor['bio']),'nombre')

lista.barrido()
print('')

# punto a 
data = lista.eliminarLinternaVerde()
if data is not None:
    print('se elimino Linterna Verde')
else:
    print('Linterna Verde no esta en la lista')
# punto b 
data = lista.aparicionWolverine()
print(f'primera aparicion de Wolverine {data}') 
# punto c 
data = lista.cambiarCasa()
print('se cambio la casa comic de Dr. Strange\n')
lista.barrido()
# punto d 
print('\nla palabra traje o armadura aparece en la bio')
data = lista.armaduraTraje()
for valor in data:
    print(valor)
# punto e 
print('\naño de aparicion anterior a 1963')
data = lista.aparicion_1963()
for valor in data:
    print(valor[0], valor[1])
# punto f 
print('')
heroes = ['Capitana Marvel','Mujer Maravilla']
data = lista.mostrarCasaPersonajes(heroes)
for heroe, casa in data:
    print('{} es de la casa {}'.format(heroe,casa))
# punto g
print('')
info = ['Flash','Star Lord']
data = lista.infoFlshStarLord(info)
for heroe in data:
    print(heroe)
# punto h
print('\nsuperheroes cuyas iniciales son B M o S')
data = lista.inicialBMS()
for valor in data:
    print(valor)
# punto i 
data = lista.ContarPorCasa()
for valor in data:
    print(f'\nsuperheroes de dc {valor[0]}')
    print(f'superheroes de marvel {valor[1]}')



class Cancion:
    def __init__(self,titulo,artista,duracion,reproducciones):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
        self.reproducciones = reproducciones
    
    def __str__(self):
        return f'{self.titulo}  {self.artista}  {self.duracion}  {self.reproducciones}'
        
lista_canciones = Lista()

canciones = [
            {'title':'do i wannna know?','art':'artic monkeys','dur':'4:25','rep':random.randint(1,100)},
            {'title':'cancion 1','art':'artista 1','dur':'3:00','rep':random.randint(1,100)},       
            {'title':'cancion 2','art':'artista 2','dur':'1:33','rep':random.randint(1,100)},      
            {'title':'cancion 3','art':'artista 3','dur':'3:45','rep':random.randint(1,100)},      
            {'title':'cancion 4','art':'artista 4','dur':'2:05','rep':random.randint(1,100)},      
            {'title':'cancion 5','art':'artista5','dur':'5:00','rep':random.randint(1,100)},       
            {'title':'cancion 6','art':'artista 6','dur':'3:06','rep':random.randint(1,100)},       
            {'title':'cancion 7','art':'artista 7','dur':'1:07','rep':random.randint(1,100)},      
            {'title':'cancion 8','art':'artista 8','dur':'4:45','rep':random.randint(1,100)},      
            {'title':'cancion 9','art':'artista9','dur':'2:00','rep':random.randint(1,100)},       
        ]

print('\nlista de canciones')
for cancion in canciones:
    lista_canciones.insertar(Cancion(cancion['title'].title(),
                           cancion['art'].title(),
                           cancion['dur'],
                           cancion['rep']),'titulo')

lista_canciones.barrido()
# punto a 
data = lista_canciones.cancionMasLarga()
print(f'\ncancion mas larga {data}') 
# punto b
print('\ntop 5 de canciones mas escuchadas')
data = lista_canciones.topCanciones(5)
for cancion in data:
    print(cancion)
print('\ntop 10 de canciones mas escuchadas')
data = lista_canciones.topCanciones(10)
for cancion in data:
    print(cancion)
# punrto c
print('\ncancones de Artic Monkeys')
data = lista_canciones.cancionesBanda('Artic Monkeys')
for cancion in data:
    print(cancion)






