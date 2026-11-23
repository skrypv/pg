[
{"jmeno": "Jan Novak", "telefon": "775889854", "email": "jan@novak.cz"},
{"jmeno": "Tomas Novotny", "telefon": "0042775889854", "email": "tom@seznam.cz"},
{"jmeno": "Eva Dvorakova", "telefon": "77755687844", "email": "eva@jcu.cz"}
]

import json


class Osob:
    
    def __init__(jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email

    def __str__(self):
        return f"Osoba: {self.jmeno} {self.telefon} is {self.email}"
    
    def __repr__(self):
        return f"Osoba({self.jmeno}, {self.telefon}, {self.email})"

@classmethod 
def load_data(cls, data):
        if 'jmeno' not in data or 'telefon' not in data or 'email' not in data:
            return None
        return Osoba(data['jmeno'], data['telefon'], data['email'])

   


if __name__ == "__main__":

    Osoby = []

    with open("osoby.json") as f:
        data = json.loads(fp.read())
        for record in data:
            osoby.append(osoba.load_data(record))
    
    print(osoby)
    