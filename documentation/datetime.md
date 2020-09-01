:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 39. Módulo datetime


El módulo contiene las clases time y datetime donde manejaremos tiempo, horas y fechas.

````python
from datetime import datetime

dt = datetime.now()    # Fecha y hora actual

print(dt)
print(dt.year)         # año
print(dt.month)        # mes
print(dt.day)          # día

print(dt.hour)         # hora
print(dt.minute)       # minutos
print(dt.second)       # segundos
print(dt.microsecond)  # microsegundos

print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
print("{}/{}/{}".format(dt.day, dt.month, dt.year))
````
>from datetime import datetime

>dt = datetime.now()    # Fecha y hora actual

>print(dt)
>print(dt.year)         # año
>print(dt.month)        # mes
>print(dt.day)          # día

>print(dt.hour)         # hora
>print(dt.minute)       # minutos
>print(dt.second)       # segundos
>print(dt.microsecond)  # microsegundos

>print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
>print("{}/{}/{}".format(dt.day, dt.month, dt.year))