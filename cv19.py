class ZapornyZustatek(Exeption):
    pass

    class Bankovniucet:
        def __init__(self):
            self.__zustatek = 0


        @property
        def zusstatek(self):
            return self.__zustatek

        @zusstatek.setter
        def zusstatek(self, hodnota):
            if hodnota < 0:
                raise ZapornyZustatek("Nelze nastavi zaporny zustatek")
            self.__zustatek = hodnota


if __name__ == "__main__":

    u = Bankovniucet()
    print(u.zusstatek)
    u.zusstatek = 100
    print(u.zusstatek)

