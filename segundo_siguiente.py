"""
Tarea:    Siguiente segundo
Autor:    
Fecha:    23/mar/20
Grupo:    ESI-232
Profesor: Jorge A. Zaldívar Carrillo
"""

# Entradas
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

# Proceso
segundos += 1
if segundos > 59:
    segundos = 0
    minutos += 1
    if minutos > 59:
        minutos = 0
        horas += 1
        if horas > 23:
            horas = 0

# Salidas
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos: ", segundos)
