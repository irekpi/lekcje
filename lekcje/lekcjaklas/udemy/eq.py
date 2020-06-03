class Chleb:
    def __init__(self, cena, maka):
        self.cena = cena
        self.maka = maka


    def __eq__(self, inny_chleb):
        return self.cena == inny_chleb.cena and self.maka == inny_chleb.maka


ziarno = Chleb(22, "biala")
jesc = Chleb(33, "czarna")
ziarno2 = Chleb(22, "biala")
print(ziarno == jesc)
print(ziarno == ziarno2)
