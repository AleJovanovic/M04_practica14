class university:
    def __init__(self,nom,ciutat,adreça,ranking,tipus,graus):
        self.nom=nom
        self.ciutat=ciutat
        self.adreça=adreça
        self.ranking=ranking
        self.tipus=tipus
        self.graus=graus

     
    def getNom(self):
        return self.nom

    def setNom(self,nom):
        self.nom=nom


    def getAdreça(self):
        return self.adreça

    def setAdreça(self,adreça):
        self.adreça=adreça

    def getCiutat(self):
        return self.ciutat
    
    def setCiutat(self,ciutat):
        self.ciutat=ciutat

    def getRanking(self):
        return self.ranking

    def setRanking(self,ran):
         self.ranking=ran
        
    def getTipus(self):
        return self.tipus

    def setTipus(self,tipus):
        self.tipus=tipus

    def getGraus(self):
        return self.graus

    def setGraus(self, num):
        self.graus=num


    def info(self):
        print(self.nom, self.ciutat,self.adreça ,self.ranking ,self.tipus ,self.graus)


    def to_dict(self):
        return {
            "nom":self.nom,
            "ciutat":self.ciutat,
            "adreça":self.adreça,
            "ranking":self.ranking,
            "tipus":self.tipus,
            "graus":self.graus
        }


    
