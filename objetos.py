from random import shuffle
from os import system
class Partida:
    def __init__(self):
        self.preguntarPuntos()

    def preguntarPuntos(self):
        puntos_para_ganar = input("A cuantos puntos queres jugar? (15/30)\n")
        try:
            puntos_para_ganar = int(puntos_para_ganar)
        except:
            system("cls")
            print("El numero ingresado no es valido. Usando el valor por defecto (15)")
            puntos_para_ganar = 15
        
        while puntos_para_ganar != 15 and puntos_para_ganar != 30:
            system("cls")
            puntos_para_ganar = input("Porfavor ingrese 15 o 30:\n")
            try:
                puntos_para_ganar = int(puntos_para_ganar)
            except:
                system("cls")
                print("El numero ingresado no es valido. Usando el valor por defecto (15)")
                puntos_para_ganar = 15

        self.puntos_para_ganar = puntos_para_ganar

class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
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

