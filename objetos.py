from random import shuffle

class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

class Jugador:
    def __init__(self):
        self.cartas = []

    def mostrar_cartas(self):
        print("-----CARTAS JUGADOR-----")
        for carta in self.cartas:
            print(f"numero: {carta.numero}, palo: {carta.palo}")

class CPU:
    def __init__(self):
        self.cartas = []

    def mostrar_cartas(self):
        print("-----CARTAS CPU-----")
        for carta in self.cartas:
            print(f"numero: {carta.numero}, palo: {carta.palo}")

class Mazo:
    def __init__(self):
        palos = ["espada", "oro", "basto", "copa"]
        numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
        self.cartas = []
        for palo in palos:
            for numero in numeros:
                self.cartas.append(Carta(numero, palo))
        shuffle(self.cartas)

    def repartir(self, jugador:Jugador, cpu:CPU):
        if len(self.cartas) > 0:
            for i in range(3):
                jugador.cartas.append(self.cartas.pop(i))
                cpu.cartas.append(self.cartas.pop(i+1))

    def mostrar_cartas(self):
        print("-----CARTAS MAZO-----")
        for carta in self.cartas:
            print(f"numero: {carta.numero}, palo: {carta.palo}")

