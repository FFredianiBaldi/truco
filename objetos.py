import random
from os import system

class Mano:
    def __init__(self):
        self.ganador = None

class Ronda:
    def __init__(self):
        self.mano1 = Mano()
        self.mano2 = Mano()
        self.mano3 = Mano()

        self.envido_cantado = {
            "envido" : False,
            "envido2" : False,
            "real envido" : False,
            "falta envido" : False
        }

        self.truco_cantado = {
            "truco" : False,
            "retruco" : False,
            "vale 4" : False
        }

        self.truco = 1
        self.envido = 0
        self.ganador = None

class Partida:
    def __init__(self):
        self.preguntarPuntos()

        self.turno = random.choice(["jugador", "cpu"])
        self.ronda_actual = Ronda()

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

class Usuario:
    def __init__(self):
        self.cartas = []
        self.puntos = 0

class Jugador(Usuario):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def mostrar_cartas(self):
        for i, carta in enumerate(self.cartas):
            print(f"{i+1}. {carta.numero} de {carta.palo}")

    def elegir_opcion(self, ronda:Ronda):
        opciones = [None]
        for opcion, estado in ronda.truco_cantado.items():
            if estado == False:
                opciones.pop(0)
                opciones.append(opcion)
                break

        for i, opcion in enumerate(opciones):
            print(f"{i+1}. {opcion} ", end="")
        print()


class CPU(Usuario):
    def __init__(self):
        super().__init__()

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
        random.shuffle(self.cartas)

    def repartir(self, jugador:Jugador, cpu:CPU):
        if len(self.cartas) > 0:
            for i in range(3):
                jugador.cartas.append(self.cartas.pop(i))
                cpu.cartas.append(self.cartas.pop(i+1))

    def mostrar_cartas(self):
        print("-----CARTAS MAZO-----")
        for carta in self.cartas:
            print(f"numero: {carta.numero}, palo: {carta.palo}")

