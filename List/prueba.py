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

# actividad 11 
class Personaje:
    def __init__(self,nombre,altura,edad,genero,especie,planeta,episodios):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.genero = genero
        self.especie = especie
        self.planeta = planeta
        self.episodios = episodios

    def __str__(self):
        return f'{self.nombre}  {self.altura}  {self.edad}  {self.genero}  {self.especie}  {self.planeta}  {self.episodios}'


personajes = [
        {'name':'luke skywalker','height':1.72,'age':350,'sex':'M','kind':'humano','planet':'tatooine','ep':[4,5,6,7,8,9]},
        {'name':'r2-d2','height':0.96,'age':250,'sex':'-','kind':'droide','planet':'naboo','ep':[1,2,3,4,5,6,7,8,9]},
        {'name':'leila organa','height':1.50,'age':50,'sex':'F','kind':'humano','planet':'alderaan','ep':[4,5,6,7,8,9]},
        {'name':'darth vader','height':2.05,'age':300,'sex':'M','kind':'humano','planet':'tatooine','ep':[1,2,3,4,5,6]},
        {'name':'obi-wan kenobi','height':1.82,'age':900,'sex':'M','kind':'humano','planet':'tatooine','ep':[1,2,3,4,5,6,7]},
        {'name':'yoda','height':0.50,'age':1000,'sex':'M','kind':'yodas','planet':'-','ep':[1,2,3,4,5,8]},
        {'name':'han solo','height':172,'age':870,'sex':'M','kind':'humano','planet':'corellia','ep':[4,5,6,7]}, 
        {'name':'ashoka tano','height':1.53,'age':100,'sex':'F','kind':'-','planet':'corellia','ep':[4,5,6,7]},
        ]

lista = Lista()
for personaje in personajes:
    lista.insertar(Personaje(personaje['name'].title(),
                             personaje['height'],
                             personaje['age'],
                             personaje['sex'],
                             personaje['kind'],
                             personaje['planet'].title(),
                             personaje['ep'],
                             ),'nombre')
print('')
# punto a 
lista.barrido()
print('\npersonajes femeninos')
for i in range(lista.tam()):
    personaje = lista.elemento_indice(i)
    if personaje.genero == 'F':
        print(personaje.nombre)
# punto b
print('\ndroides que aparecen los 6 primeros episodios')
for i in range(lista.tam()):
    personaje = lista.elemento_indice(i)
    if personaje.especie == 'droide':
        for episodio in personaje.episodios:
            if episodio <= 6:
                print(personaje.nombre)
                break
# punto c 
print('\ninfo de Han Solo y Darth Vader')
data = lista.elemento_indice(lista.buscar('Darth Vader','nombre'))
if data is not None:
    print(data)
data = lista.elemento_indice(lista.buscar('Han Solo','nombre'))
if data is not None:
    print(data)
# punto d 
print('\npersonajes que aparecen en el episodio 7 y los tres anteriores')
for i in range(lista.tam()):
    personaje = lista.elemento_indice(i)
    if 7 in personaje.episodios and 6 in personaje.episodios and 5 in personaje.episodios and 4 in personaje.episodios:
        print(personaje.nombre)
# punto e 
lista.reordenar('edad')
print('\nmayores a 850 años de edad')
for i in range(lista.tam()):
    personaje = lista.elemento_indice(i)
    if personaje.edad > 850:
        print(personaje.nombre) 
print(f'personaje con mayor edad {lista.elemento_indice(lista.tam()-1).nombre}')

# eliminar n cantidad de datos de un campo en particular
# punto f 
lista.reordenar('nombre')
episodios_borrar = [4,5,6]
indice = 0
for i in range(lista.tam()):
    control = True
    episodepersonaje = lista.elemento_indice(indice).episodios 
    for episode in episodios_borrar:
        if episode not in episodepersonaje:
            control = False
            break
    if control:
        lista.eliminar(lista.elemento_indice(indice).nombre,'nombre')
        indice -= 1 
    indice += 1 
lista.barrido()
print('')


















