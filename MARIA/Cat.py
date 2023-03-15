class cat:
    #6 ATRIBUTOS
    def __init__(self, nombre, sexo, edat,especie, ciudad, pais):  
        self.nombre=nombre
        self.sexo=sexo
        self.edat=edat
        self.especie=especie
        self.ciudad=ciudad
        self.pais=pais

    #DECLARAMOS LOS GETTERS Y SETTERS
    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre=nombre


    def getSexo(self):
        return self.sexo

    def setSexo(self,sexo):
        self.sexo=sexo


    def getEdat(self):
        return self.edat

    def setEdat(self,edat):
        self.edat=edat
        

    def getEspecie(self):
        return self.especie

    def setEspecie(self,especie):
         self.especie=especie

        
    def getCiudad(self):
        return self.ciudad

    def setCiudad(self,ciudad):
        self.ciudad=ciudad

    def getPais(self):
        return self.pais

    def setPais(self, pais):
        self.pais=pais


    def info(self):
        print(self.nombre, self.sexo,self.edat ,self.especie ,self.ciudad ,self.pais)


    def to_dict(self):
        return {
            "nombre":self.nombre,
            "sexo":self.sexo,
            "edat":self.edat,
            "especie":self.especie,
            "ciudad":self.ciudad,
            "pais":self.pais
        }

    
