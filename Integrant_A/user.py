class user:
    def __init__(self,nom,edat,dni,adressa,correo,nacionalitat):
        self.nom=nom
        self.edat=edat
        self.dni=dni
        self.adressa=adressa
        self.correo=correo
        self.nacionalitat=nacionalitat

    
    def getNom(self):
        return self.nom

    def setNom(self,nom):
        self.nom=nom

    def getEdat(self):
        return self.edat

    def setEdat(self,edat):
        self.edat=edat

    def getDNI(self):
        return self.dni

    def setDNI(self,dni):
        self.dni=dni
    
    def getAdressa(self):
        return self.adressa

    def setAdressa(self,adressa):
        self.adressa=adressa

    def getCorreo(self):
        return self.correo

    def setCorreo(self,correo):
        self.correo=correo

    def getNacionalitat(self):
        return self.nacionalitat

    def setNacionalitat(self,n):
        self.nacionalitat=n

    
    def salutacio(self):
        print(self.nom,self.edat,self.dni,self.adressa,self.correo,self.nacionalitat)

    def to_dict(self):
        return {
            "nom":self.nom,
            "edat":self.edat,
            "dni":self.dni,
            "adressa":self.adressa,
            "correo":self.correo,
            "nacionalitat":self.nacionalitat
        }

     