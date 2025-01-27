from objetos import *

mazo = Mazo()
jugador = Jugador()
cpu = CPU()

mazo.repartir(jugador, cpu)


mazo.mostrar_cartas()
jugador.mostrar_cartas()
cpu.mostrar_cartas()