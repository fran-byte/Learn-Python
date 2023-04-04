import tkinter as tk
import socket
import netifaces
import subprocess
import os


import configparser
from configparser import ConfigParser

import ctypes
import subprocess

# Ejecuta el comando netsh para desactivar el WiFi
subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "disable"])

# Obtiene el identificador de la ventana de la línea de comandos
hwnd = ctypes.windll.kernel32.GetConsoleWindow()

# Deshabilita la opción de cerrar la ventana de la línea de comandos
hmenu = ctypes.windll.user32.GetSystemMenu(hwnd, False)
ctypes.windll.user32.DeleteMenu(hmenu, 6, 0x400)



# Ejecutar el comando "ipconfig" en la terminal
output = subprocess.check_output(['ipconfig', '/all']).decode('latin-1')



ventana = tk.Tk()

def disable_event():
    pass

ventana.protocol("WM_DELETE_WINDOW", disable_event)

ventana.geometry("350x520")
# Establecer el color de fondo de la ventana
ventana.configure(bg="light gray")

# Creamos un borde con efecto de relieve
borde = tk.Frame(ventana, bd=2, relief='raised', bg='light gray')

# Colocamos el borde en la ventana con un espacio de 10 píxeles
borde.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)



ventana.resizable(False, False)
ventana.title("Terminal IP Conf")



# Crear listas de IPs
ip_host = ["192.168.0.24", "192.168.1.2","192.168.0.2", "10.117.3.84", "192.168.0.205"]
ip_gateway = ["192.168.0.30", "192.168.0.25", "192.168.0.1", "192.168.1.1", "10.117.3.85", "192.168.0.201"]


# Obtener lista de adaptadores de red


adapters = []

# Iterar a través de las líneas de salida del comando ipconfig
for line in output.split('\n'):
    # Si la línea contiene la cadena "Ethernet adapter" o "Adaptador de Ethernet", es un adaptador de Ethernet
    if 'Ethernet adapter' in line or 'Adaptador de Ethernet' in line:
        # Obtener el nombre del adaptador eliminando el prefijo "Ethernet adapter " o "Adaptador de Ethernet "
        adapter_name = line.split(':')[0].replace('Ethernet adapter ', '').replace('Adaptador de Ethernet ', '').strip()
        adapters.append(adapter_name)




# Variables para guardar las IPs y adaptador seleccionados
ip_seleccionada_host = tk.StringVar()
ip_seleccionada_gateway = tk.StringVar()
adaptador_seleccionado = tk.StringVar()

# Crear etiquetas para las selecciones de IP y adaptador
label_host = tk.Label(ventana, text="IP Host:", anchor='w', bg="light gray", font=("Calibri", 12))
label_host.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

label_gateway = tk.Label(ventana, text="IP Gateway:", anchor='w', bg="light gray", font=("Calibri", 12))
label_gateway.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

label_adaptador = tk.Label(ventana, text="Adaptador Ethernet:", anchor='w', bg="light gray", font=("Calibri", 12))
label_adaptador.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)



# Crear desplegables con las IPs
ip_menu_host = tk.OptionMenu(ventana, ip_seleccionada_host, *ip_host)
ip_menu_host.config(bg="light gray", font=("Calibri", 12))
ip_menu_host.grid(row=0, column=1, padx=10, pady=10)

ip_menu_gateway = tk.OptionMenu(ventana, ip_seleccionada_gateway, *ip_gateway)
ip_menu_gateway.config(bg="light gray", font=("Calibri", 12))
ip_menu_gateway.grid(row=1, column=1, padx=10, pady=10)

# Crear desplegable con los adaptadores de red
adaptador_menu = tk.OptionMenu(ventana, adaptador_seleccionado, *adapters)
adaptador_menu.config(bg="light gray", font=("Calibri", 12))
adaptador_menu.grid(row=2, column=1, padx=10, pady=10)


# Enviar_ping a Gateway
def enviar_ping():
    gateway = ip_gateway = ip_seleccionada_gateway.get()
    for i in range(1, 11): 
        response = subprocess.call(['ping', '-n', '1', gateway])
        if response == 0:
            label_resultado.config(text=f" Ping OK a {gateway}",fg="white", bg="dark green")

        else:
            label_resultado.config(text=f" Error de PING a {gateway}", fg="white", bg="dark red")
            break


# Habilitar habilitar el WiFi y salir del programa
def habilitar_wifi_y_salir():
    # Ejecutar el comando netsh para habilitar el WiFi
    subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "enable"])
    # Salir del programa
    ventana.destroy()

# Crear botón para enviar Ping     
boton_ping = tk.Button(ventana, text="Enviar Ping al Gateway", command=enviar_ping, width=25)
boton_ping.config(bg="light gray", font=("Calibri", 12))
boton_ping.grid(row=5, column=0, columnspan=2, padx=10, pady=10)



# Función para guardar las IPs y adaptador seleccionados
def guardar_ip_y_adaptador():
    ip_host = ip_seleccionada_host.get()
    ip_gateway = ip_seleccionada_gateway.get()
    adaptador = adaptador_seleccionado.get()
    label_resultado.config(text=f"IP Host: {ip_host}\nIP Gateway: {ip_gateway}\nAdaptador: {adaptador}", bg="light gray", fg="black")


    a='netsh interface ip set address name='
    c=" static "
    mask= " 255.255.255.0 "
    d=a+'"'+adaptador+'"'+c+ip_host+mask+ip_gateway
    dhcpCommand = d
    command = dhcpCommand.split()
    subprocess.run(command)
    delay = 4
    print("\n  > > > Configure Static IP with the Command [ ",d," ]")

# IP en DHCP
def cambiar_dhcp():

    adaptador = adaptador_seleccionado.get()
    

    a="netsh interface ip set address "
    c=" dhcp"
    d=a+'"'+adaptador+'"'+c
    print(d)
    dhcpCommand = d
    import subprocess
    command = dhcpCommand.split()
    subprocess.run(command)
    delay = 1
    gws = netifaces.gateways()
    gateway = socket.gethostbyname(socket.gethostname())
    label_resultado.config(text=f" La IP ahora es Dinámica", bg="light gray", fg="black")

    print("\n>>   Done !! - Now our ",adaptador," address is Dynamic: DHCP")

# Crear botón para enviar PING
boton_ping = tk.Button(ventana, text="Enviar Ping al Gateway", command=enviar_ping, width=25)
boton_ping.config(bg="light gray", font=("Calibri", 12))
boton_ping.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


# Crear botón para convertir IP a DHCP
button_dhcp = tk.Button(ventana, text='Cambiar a DHCP', command=cambiar_dhcp, width=25)
button_dhcp.config(bg="light gray", font=("Calibri", 12))
button_dhcp.grid(row=6, column=0, columnspan=2, padx=10, pady=10)



# Crear botón para guardar las IPs y adaptador seleccionados
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_ip_y_adaptador, width=15)
boton_guardar.config(bg="light gray", font=("Calibri", 12))
boton_guardar.grid(row=3, column=1, padx=10, pady=10)

# Crear un recuadro para mostrar las IPs y adaptador seleccionados
label_resultado = tk.Label(ventana, text="", bg="light gray", width=30, height=3, relief="sunken", anchor="w")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Crear etiqueta advertencia
label_advertencia0 = tk.Label(ventana, text="ATENCIÓN", anchor='e', bg="light gray", fg="green", font=("Calibri", 12))
label_advertencia0.grid(row=8, column=0, padx=10, pady=0, sticky=tk.E)  # Ajustando anchor a 'E'
label_advertencia = tk.Label(ventana, text="[WIFI OFF]", anchor='w', bg="light gray", fg="red", font=("Calibri", 12))
label_advertencia.grid(row=8, column=1, padx=0, pady=0, sticky=tk.W)

# Crear botón para habilitar Wifi y Salir   
boton_habilitar_wifi = tk.Button(ventana, text="EXIT", command=habilitar_wifi_y_salir, width=25, fg="blue")
boton_habilitar_wifi.config(bg="light gray", font=("Calibri", 12))
boton_habilitar_wifi.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="s")


ventana.mainloop()
