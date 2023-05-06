class Lista():
    def __init__(self):
        self.__elements = []

    def __criterio(self, dato, criterio=None):
        if criterio == None:
            return dato
        else:
            return getattr(dato, criterio)

    def insertar(self, value, criterio=None):
        if len(self.__elements) == 0:
            self.__elements.append(value)
        elif self.__criterio(value, criterio) < self.__criterio(self.__elements[0], criterio):
            self.__elements.insert(0, value)
        elif self.__criterio(value, criterio) >= self.__criterio(self.__elements[-1], criterio):
            self.__elements.append(value)
        else:
            index = 1
            while self.__criterio(value, criterio) >= self.__criterio(self.__elements[index], criterio):
                index += 1
            self.__elements.insert(index, value)

    def buscar(self, search_value, criterio=None):
        position = None
        for index, value in enumerate(self.__elements):
            if search_value == self.__criterio(value, criterio):
                position = index
                break
        return position 
    
    def eliminar(self, value, criterio=None):
        return_value = None
        pos = self.buscar(value, criterio)
        if pos is not None:
            return_value = self.__elements.pop(pos)
        return return_value 

    def tamano(self):
        return len(self.__elements)
    
    def es_vacia(self):
        return self.tamano() == 0

    def barrido(self):
        for value in self.__elements:
            print(value)

    def elemento_valor(self, value, criterio=None):
        return_value = None
        pos = self.buscar(value, criterio)
        if pos is not None:
            return_value = self.__elements[pos]
        return return_value

    def elemento_indice(self, index):
        return_value = None
        if index >= 0 and index < self.tamano():
            return_value = self.__elements[index]
        return return_value

    def modificar_valor(self, value, new_value, criterio=None):
        pos = self.buscar(value, criterio)
        if pos is not None:
            value = self.eliminar(value, criterio)
            self.insertar(new_value, criterio)


    # actividad 6 
    def traje_armadua(self):
        for value in self.__elements:
            if 'traje' in value.biografia or 'armadura' in value.biografia:
                print(f'{value.nombre}, {value.biografia}')

    def aparicion_menor_1963(self):
        for value in self.__elements:
            if value.aparicion<1963:
                print(f'{value.nombre} {value.casa}')
    
    def listar_bms(self):
        for value in self.__elements:
            if value.nombre[0] in ['b,m,s']:
                print(value)

    def cantidad_superheroes(self):
        count_dc =0
        count_marvel = 0
        for value in self.__elements:
            if value.casa == 'dc':
                count_dc+=1 
            else:
                count_marvel+=1 
        return count_dc,count_marvel









