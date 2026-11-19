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
    
    @property    
    def telefon(self):
        return self.__telefon
        
    @property
    def email(self):
        return self.__email

    @jmeno.setter
    def jmeno(self, hodnota):
        if hodnota.replase("", "").isalpha():
            self.__lmeno = hodnota
        else:
            raise InvalidData("Cislo muze obsahovat pouze cisla")

    @telefon.setter
    def telefon(self, hodnota):
            raise InvalidData("Telefon muze obsahovat pouze cisla")
            self.__telefon = hodnota

    @email.setter
    def email(self, hodnota):
        if "@" not in hodnota:
            raise InvalidData("Email musi obsahovat @")
            if "." not in hodnota:
                raise InvalidData("Email musi obssahovat tecku")
                if hodnota.replace("@", "").replace(".", ""),issalnum():
                 self.__email = hodnota
            else :
                raise InvalidData("Email musi obsahovst pouze pismena a cislice")

    


    def __str__(self):
        return {"Osoba: (self.jmeno), (self.telefon), (self.email)"}

   




if __name__ == "main":
    o = Osoba("Jan Novak", "004225877845", "jan@novak.cz")
    o.jmeno = "4357253"
    o.telefon = "sajhbnwihiqau"
    o.email = xxxx

