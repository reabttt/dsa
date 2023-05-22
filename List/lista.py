def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        # print('es un primitivo')
        return value
    else:
        # print('no es un dato primitivo')
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('no se puede ordenar por este criterio')


class Lista():

    def __init__(self):
        self.__elements = []

    def insertar(self, value, criterio=None):
        # print('criterio de insercion', criterio)
        if len(self.__elements) == 0 or criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[-1], criterio):
            self.__elements.append(value)
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0], criterio):
            self.__elements.insert(0, value)
        else:
            index = 1
            while criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index], criterio):
                index += 1
            self.__elements.insert(index, value)

    
    def buscar(self, search_value, criterio=None):
        position = None
        first = 0
        last = self.tam() - 1
        while (first <= last and position == None):
            middle = (first + last) // 2
            if search_value == criterio_comparacion(self.__elements[middle], criterio):
                position = middle
            elif search_value > criterio_comparacion(self.__elements[middle], criterio):
                first = middle + 1
            else:
                last = middle - 1
        return position 

    
    def eliminar(self, value, criterio=None):
        return_value = None
        pos = self.buscar(criterio_comparacion(value, criterio), criterio)
        if pos is not None:
            return_value = self.__elements.pop(pos)
        return return_value

    def tam(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value)

    def reordenar(self, criterio=None):
        def criterio_clave(valor):
            return criterio_comparacion(valor, criterio) 
        self.__elements.sort(key=criterio_clave)

    # def get_element_by_value(self, value):
    #     return_value = None
    #     pos = self.search(value)

    #     if pos is not None:
    #         return_value = self.__elements[pos]
    #     return return_value

    def elemento_indice(self, index):
        return_value = None
        if index >= 0 and index < self.tam():
            return_value = self.__elements[index]
        return return_value

    def modificar_valor(self, value, new_value):
        pos = self.buscar(value)
        if pos is not None:
            value = self.eliminar(value)
            self.insertar(new_value)

    # actividad 6 
    def eliminarLinternaVerde(self):
        return self.eliminar('Linterna Verde','nombre')
    
    def aparicionWolverine(self):
        node = self.elemento_indice(self.buscar('Wolverine','nombre'))
        if node is not None:
            return node.aparicion 
        else:
            return None

    def cambiarCasa(self):
        node = self.elemento_indice(self.buscar('Dr. Strange','nombre'))
        if node is not None:
            node.casa = 'marvel'
        else:
            return None
    
    def armaduraTraje(self):
        heroes = []
        for node in self.__elements:
            if 'traje' in node.biografia or 'armadura' in node.biografia:
                heroes.append(node.nombre)
        return heroes

    def aparicion_1963(self):
        heroes = []
        for node in self.__elements:
            if node.aparicion < 1963:
                heroes.append((node.nombre, node.casa))
        return heroes
    
    # le paso como parametro una lista con los nombres de los superheroes que estoy buscando
    def mostrarCasaPersonajes(self,heroes):
        casas_heroes = []
        for heroe in heroes:
            casa = self.elemento_indice(self.buscar(heroe,'nombre')).casa # devuelve el superheroe con el campo casa
            if casa is not None:
                casas_heroes.append((heroe,casa))
        return casas_heroes

    def infoFlshStarLord(self,heroes):
        infos = []
        for heroe in heroes:
            node = self.elemento_indice(self.buscar(heroe,'nombre'))
            if node is not None:
                infos.append(node)
        return infos

    def inicialBMS(self):
        heroes = []
        for heroe in self.__elements:
            if heroe.nombre[0] in ['B','M','S']:
                heroes.append(heroe)
        return heroes
    
    def ContarPorCasa(self):
        contador = []
        dc = 0
        marvel = 0
        for node in self.__elements:
            if node.casa == 'dc':
                dc += 1 
            else:
                marvel += 1 
        contador.append((dc,marvel))
        return contador

    # actividad 10 
    def cancionMasLarga(self):
        self.reordenar('duracion')
        return self.elemento_indice(self.tam()-1)
    
    def topCanciones(self,top):
        self.reordenar(criterio='reproducciones')
        self.__elements.reverse()
        return self.__elements[:top]

    def cancionesBanda(self,artista):
        canciones = []
        for i in range(self.tam()):
            node = self.elemento_indice(i)
            if node.artista == artista:
                canciones.append(node)
        return canciones 

    







