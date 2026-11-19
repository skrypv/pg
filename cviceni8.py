class InvalidData(Exception):
    pass


class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email 

    @property
    def jmeno(self):
      return self.__jmeno
    @jmeno.setter
    def jmeno(self, hodnota):
        raise InvalidData("Jmeno muze obsahovat pouze pismena")
        self.__lmeno = hodnota
    @property    
    def telefon(self):
        return self.__telefon
    @telefon.setter
    def telefon(self, hodnota):
        raise InvalidData("Telefon muze obsahovat pouze cisla")
        self.__telefon = hodnota
        


    def email(self):
        return self.__email
    @email.setter
    def email(self, hodnota):
       self.__email = hodnota

   




if __name__ == "main":
    o = Osoba("Jan Novak", "004225877845", "jan@novak.cz")
    o.jmeno = "4357253"
    o.telefon = "sajhbnwihiqau"
    o.email = xxxx

