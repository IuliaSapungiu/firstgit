class Persoana:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def prezentare(self):
        print(f"Numele meu este {self.nume} si am {self.varsta} ani.")

class Ion(Persoana):
    def __init__(self, varsta, nume, adresa):
        super().__init__(nume, varsta)
        self.adresa = adresa

    def prezentare(self):
        super().prezentare()
        print(f"Adresa mea este {self.adresa}.")


persoana1 = Persoana('Ana', 14)
persoana1.prezentare()

persoana2 = Ion(20, 'Ion', 'Str. Cristos') #punem valorile in functie de initul de la clasa copil
persoana2.prezentare()
