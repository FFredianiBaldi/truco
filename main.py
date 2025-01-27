from objetos import *
from os import system

system("cls")
nombre_jugador = input("Cual es tu nombre? ")

mazo = Mazo()
jugador = Jugador(nombre_jugador)
cpu = CPU()

system("cls")
partida = Partida()