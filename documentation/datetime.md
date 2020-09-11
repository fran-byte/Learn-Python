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

Es posible crear un datetime manualmente pasando los parámetros (year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None).

Sólo son obligatorios el año, el mes y el día.


````python
from datetime import datetime

dt = datetime(2000,1,1)
print(dt)
````

> datetime.datetime(2000, 1, 1, 0, 0)

No podemos cambiarlo al vuelo:
````python
dt.year = 2050
````

> ---------------------------------------------------------------------------
> AttributeError                            Traceback (most recent call last)
>
> ipython-input-18-f655491f2afa in <module>()
>
> ----> 1 dt.year = 3000
>
>AttributeError: attribute 'year' of 'datetime.date' objects is not writable

Tendremos que usar método replace:

````python
dt = dt.replace(year=3000) // Duplica y reemplaza la fecha por 3000, pero dt.year sigue valiendo 2000
print(dt)
````
> datetime.datetime(3000, 1, 1, 0, 0)

## Formateos
Formato automático ISO (Organización Internacional de Normalización):

````python
from datetime import datetime
dt = datetime.now()
print(dt.isoformat())
````
> from datetime import datetime

Formateo munual (inglés por defecto):

````python
from datetime import datetime

dt = datetime.now()

print(dt.strftime("%A %d %B %Y %I:%M"))
````
> Tuesday 01 September 2020 05:46

El Inglés es el idioma por defecto, aunque se puede modificar:

````python
import locale

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es-ES') 

print(dt.strftime("%A %d %B %Y %I:%M"))
print(dt.strftime("%A %d de %B del %Y - %H:%M"))  # %I 12h - %H 24h
````
## Operaciones
Podemos sumar y restar tiempo con la función timedelta():

````python
from datetime import datetime, timedelta

dt = datetime.now()
print(dt.strftime("%A %d de %B del %Y - %H:%M"))

# Generamos 14 días con 4 horas y 1000 segundos de tiempo
t = timedelta(days=14, hours=4, seconds=1000)

# Lo operamos con el datetime de la fecha y hora actual
dentro_de_dos_semanas = dt + t
print(dentro_de_dos_semanas.strftime("%A %d de %B del %Y - %H:%M"))
hace_dos_semanas = dt - t
print(hace_dos_semanas.strftime("%A %d de %B del %Y - %H:%M"))
````
>Tuesday 01 de September del 2020 - 17:57

>Tuesday 15 de September del 2020 - 22:14

>Tuesday 18 de August del 2020 - 13:41

## Zonas horarias

Para establecer zonas horarias en nuestras fechas y horas necesitamos instalar el módulo pytz desde Anaconda Prompt:

> pip install pytz

Una vez instalado podemos consultar las diferentes zonas horarias disponibles con:

````python
print(pytz.all_timezones)
````
Ahora por ejemplo para crear la hora actual en Tokyo (Japón) haríamos lo siguiente:

````python
dt = datetime.now(pytz.timezone('Asia/Tokyo'))
print(dt.strftime("%A %d de %B del %Y - %H:%M"))  # %I 12h - %H 24h
````

> martes 1 de septiembre del 2020 - 20:02