from objetos import *
from os import system

system("cls")
nombre_jugador = input("Cual es tu nombre? ")

mazo = Mazo()
jugador = Jugador(nombre_jugador)
cpu = CPU()

system("cls")
partida = Partida()

while True:
    if len(jugador.cartas) < 1 and len(cpu.cartas) < 1:
        mazo.repartir(jugador, cpu)

    jugador.elegir_opcion(partida.ronda_actual)
    break