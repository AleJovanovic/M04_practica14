class Car:
    def __init__(self, marca, velocitat, matricula, anyEdicio):
        self.marca=marca
        self.velocitat=velocitat
        self.matricula=matricula
        self.anyEdicio=anyEdicio


    def getMarca(self):
        return self.marca

    def setMarca(self,marca):
        self.marca=marca

    def getVelocitat(self):
        return self.velocitat

    def setVelocitat(self,velocitat):
        self.velocitat=velocitat

    def getMatricula(self):
        return self.matricula

    def setMatricula(self,matricula):
        self.matricula=matricula

    def getAnyEdicio(self):
        return self.anyEdicio

    def setAnyEdicio(self,anyEdicio):
        self.anyEdicio=anyEdicio


    def salutacio(self):
        print("marca: "+ self.marca + "    velocitat: "+self.velocitat+"    matricula: "+self.matricula+"    any: "+self.anyEdicio)

    def to_dict(self):
        return {
            "marca":self.marca,
            "velocitat":self.velocitat,
            "matricula":self.matricula,
            "anyEdicio":self.anyEdicio
        }