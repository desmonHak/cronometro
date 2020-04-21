from time import sleep
from os import system
from sys import platform
from multiprocessing import Process

def _reloj(TiempoEstimulado):
    _time = 1
    TiempoEstimulado = int(TiempoEstimulado)
    segundos = []
    minutos = []
    horas = []
    dias = []
    scondsTime = 0.8

    def actualizador(scondsTime, TiempoEstimulado):
        try:
            scondsTime = int(scondsTime)
        except ValueError:
            scondsTime = float(scondsTime)
        TiempoEstimulado = int(TiempoEstimulado) -1

        for i in range(int(TiempoEstimulado)):

            sleep(scondsTime)
            if platform == "win32":
                system("cls")
            elif platform == 'linux' or platform == 'linux':
                system('clear')
            else:
                system('clear')
            sleep(0.2)

    def interno(scondsTime, _time, segundos, minutos, horas, dias, TiempoEstimulado):
        try:
            scondsTime = int(scondsTime)
        except ValueError:
            scondsTime = float(scondsTime)
        TiempoEstimulado = int(TiempoEstimulado)
        for i in range(int(TiempoEstimulado)):
            
            _time = int(_time)
            #print(type(_time))
            print(str(_time))
            sleep(scondsTime)
            segundos.append(int(_time))
            _time = int(_time) + 1

            if len(segundos) == 60:            
                _time = 1
                segundos = []
                minutos.append(1)
                
            elif len(minutos) == 60:
                minutos = []
                horas.append(1)
            
            elif len(horas) == 24:
                horas = []
                dias.append(1)
            
            else:
                pass

            sleep(0.2)
            print("calculando")
        actualizador(scondsTime, 1)
        print("segundos: "+str(len(segundos)) +"\nminutos: "+ str(len(minutos))+"\nhoras: "+str(len(horas)))

    hilo1 = Process(target=interno, args=(str(scondsTime), str(_time), segundos, minutos, horas, dias, str(TiempoEstimulado)))
    hilo2 = Process(target=actualizador, args=(str(scondsTime), TiempoEstimulado))
    hilo1.start()
    hilo2.start()

            
    #print(str(_time), segundos, minutos)

relojTiempo = int(input("cuantos segundos quieres pasarle al cronometro: "))

_reloj(relojTiempo)
