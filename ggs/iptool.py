import os
import PySimpleGUI as sg
import tkinter as tk
from termcolor import colored
from tkinter import *
from pythonping import ping
import subprocess
import time
import socket
import netifaces


sg.theme('Light Green 5')
# sg.ChangeLookAndFeel('GreenTan')

# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]

# ------ Column Definition ------ #


colum1 = [
    [sg.Frame(layout=[
        [sg.Radio('CONTEC', "RADIO1", default=True, size=(10, 1), key="-IN1-", tooltip='192.168.0.30')],
        [sg.Radio('CI-5 - DRBW-10 - RBW-150', "RADIO1", default=True, size=(25, 1), key="-IN2-",
                  tooltip='192.168.0.25')],
        [sg.Radio('RBG-200 LAN 1', "RADIO1", default=True, size=(13, 1), key="-IN3-", tooltip='192.168.0.1'),
         sg.Radio('LAN 2', "RADIO1", key="-IN4-", tooltip='192.168.1.1')],
        [sg.Radio('NEXCOM LAN 1', "RADIO1", default=True, size=(13, 1), key="-IN5-", tooltip='10.117.3.85'),
         sg.Radio('LAN 2', "RADIO1", key="-IN6-", tooltip='192.168.0.201')]
        , [sg.Button('SET', pad=(60, 15), size=(18, 1))]],
        title='PC Model ', title_color='#00226F', relief=sg.RELIEF_SUNKEN)]]

colum2 = [
    [sg.Frame('COMMS Test ', [
        [sg.Button('Automatic', size=(18, 1))],
        [sg.Button('Manual', size=(18, 1))]], title_color='#00226F', )],
    [sg.Button('DHCP', pad=(10, 22), size=(18, 1))],  [sg.Text('ATTENTION : \nDisable Wifi Connection and Connect RJ45 cable ', size=(26, 3), justification='center', text_color='red',
             font=("Helvetica", 8), relief=sg.RELIEF_RIDGE)],]

layout = [

    [sg.Text('Ethernet IP Configuration & Tests', size=(33, 1), justification='center', text_color='#00226F',
             font=("Helvetica", 18), relief=sg.RELIEF_RIDGE)],

    [sg.Frame('Console Reports ', [[sg.Button('SHOW IPs', pad=(7, 22), size=(18, 1))],
        [sg.Output(size=(61, 11), key='-OUTPUT-')] ], title_color='#00226F', )],[sg.Frame('IPs Info ', [
         ], title_color='#00226F', )],
    [sg.Column(colum1), sg.Column(colum2)
     ]
]


#  Set ethernet connection with Dynamic or Static IP


def dynamic_ip():
    print("\n>>   Dynamic Host Configuration Protocol (DHCP)... OK")
    window['-OUTPUT-'].update()
    import subprocess
    dhcpCommand = '''netsh interface ip set address "Ethernet 4" dhcp'''
    command = dhcpCommand.split()
    subprocess.run(command)
    time.sleep(1)
    gws = netifaces.gateways()
    gateway = socket.gethostbyname(socket.gethostname())
    print("\n>>   Done !! - Now our IP address is Dynamic: DHCP")


def static_ip():
    dhcpCommand = '''netsh interface ip set address name="Ethernet 4" static 192.168.0.29 255.255.255.0 192.168.0.30'''
    command = dhcpCommand.split()
    subprocess.run(command)
    time.sleep(4)

    
    try:

        a=mynet()
        print("\n>>   Done !! Now our Gateway IP address is: ", a[1])
        window['-OUTPUT-'].update()
    except:
        print ("\n>   ERROR getting the IP")
        print (">   Network card NOT FOUND")
    


def static_ip2():
    dhcpCommand = '''netsh interface ip set address name="Ethernet 4" static 192.168.0.24 255.255.255.0 192.168.0.25'''
    command = dhcpCommand.split()
    subprocess.run(command)
    time.sleep(4)

    try:

        a=mynet()
        print("\n>>   Done !! Now our Gateway IP address is: ", a[1])
        window['-OUTPUT-'].update()
    except:
        print ("\n>   ERROR getting the IP")
        print (">   Network card NOT FOUND")


def static_ip3():
    dhcpCommand = '''netsh interface ip set address name="Ethernet 4" static 192.168.0.4 255.255.255.0 192.168.0.1'''
    command = dhcpCommand.split()
    subprocess.run(command)
    time.sleep(4)

    try:

        a=mynet()
        print("\n>>   Done !! Now our Gateway IP address is: ", a[1])
        window['-OUTPUT-'].update()
    except:
        print ("\n>   ERROR getting the IP")
        print (">   Network card NOT FOUND")


def static_ip4():
    dhcpCommand = '''netsh interface ip set address name="Ethernet 4" static 192.168.1.4 255.255.255.0 192.168.1.1'''
    command = dhcpCommand.split()
    subprocess.run(command)
    time.sleep(4)

    try:

        a=mynet()
        print("\n>>   Done !! Now our Gateway IP address is: ", a[1])
        window['-OUTPUT-'].update()
    except:
        print ("\n>   ERROR getting the IP")
        print (">   Network card NOT FOUND")

def static_ip5():
    dhcpCommand = '''netsh interface ip set address name="Ethernet 4" static 10.117.3.84 255.255.255.224 10.117.3.85'''
    command = dhcpCommand.split()
    subprocess.run(command)
    time.sleep(4)

    try:

        a=mynet()
        print("\n>>   Done !! Now our Gateway IP address is: ", a[1])
        window['-OUTPUT-'].update()
    except:
        print ("\n>   ERROR getting the IP")
        print (">   Network card NOT FOUND")


def static_ip6():
    dhcpCommand = '''netsh interface ip set address name="Ethernet 4" static 192.168.0.202 255.255.255.0 192.168.0.201'''
    command = dhcpCommand.split()
    subprocess.run(command)
    time.sleep(4)

    try:

        a=mynet()
        print("\n>>   Done !! Now our Gateway IP address is: ", a[1])
        window['-OUTPUT-'].update()
    except:
        print ("\n>   ERROR getting the IP")
        print (">   Network card NOT FOUND")


# Show IPs

def show():


    try:
        a=mynet()
        print("\n>>   Host IP ", a[0], " --  Gateway IP ",a[1])
        window['-OUTPUT-'].update()

    except:
        print ("\n>   ERROR getting the IP")
        print (">   Network card NOT FOUND")



    



# Send Ping

def ip_test():

    try:

        a=mynet()
        result = ping(a[1])


        if result.success():
            print("\n>>   Manual PING to Gateway", a[1], " TX / RX  ... OK")
            window['-OUTPUT-'].update()
        elif socket.error:
            print("\n>>   Conexion ERROR to Gateway", a[1], " TX / RX  ... FAILED")
            window['-OUTPUT-'].update()

    except:
        print ("\n>   ERROR getting the IP")
        print (">   Network card NOT FOUND")




# Send Loop Ping

def loop_ip_test():
    try:

        a=mynet()
        for x in range(99):
            result = ping(a[1])

            if result.success():
                print("\n",x + 1, "- Automatic PING to Gateway", a[1], " TX / RX  ... OK")
                window['-OUTPUT-'].update()
            elif socket.error:
                print("\n>> Conexion ERROR to Gateway", a[1], " TX / RX  ... FAILED")
                window['-OUTPUT-'].update()
                break
    except:
        print ("\n>   ERROR getting the IP")
        print (">   Network card NOT FOUND")

def func(message):
    print(message)

def mynet():
    import socket
    from ipaddress import ip_network as ipn
    import re
    #     i         regular expression, including the mask
    pr = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
         # Get the gateway address by the default route, there may be a number, but only the first one [0], the third element obtained by the list of IP is looking for ip [2]
    gw = re.findall(pr,os.popen('route print | find " 0.0.0.0 "').read().strip().split('\n')[0])[2]
         #     u UDP request package, avoid brainless casual UDP package, in the intranet, get the source address of the package through the UDP IP header, that is, the unit production site
    ip = [ (s.connect((gw, 53)), s.getsockname()[0], s.close()) for s in [ socket.socket(socket.AF_INET, socket.SOCK_DGRAM) ] ][0][1]
         # If the native IP and gateway are obtained correctly
    if ip and gw:
        cmd = 'wmic Path Win32_NetworkAdapterConfiguration get DefaultIPGateway,IPAddress,IPSubnet | find "' + ip + '"'
                 # Get the gateway, IP and mask through the operating system WMIC command, in order to avoid accidental returns, only the first line of data
        nw = [ i for i in os.popen(cmd).read().strip().split('\n') if i.strip() ][0]
                 # Looking for an IP-related character in this row, if the production network card is configured with multiple IP, multiple records are listed here
        nw = re.findall(pr, nw)
                 # Judging whether the IP and gateway acquired above in this record in the IP result found in this record
        if ip in nw and gw in nw:
                         #   in the first, it is determined whether it is correct, then remove the gateway from the list
            if gw == nw[0]:
                nw = nw[1:]
            else:
                return False
                         #            , ip, IP, .., Mask, Mask].
                         # First, find the index position of IP in NW, the IP corresponding mask index is divided by the length of the element divided by 2 and the IP index value
            mdex = int(len(nw) / 2 + nw.index(ip))
            mask = str(ipn(ip + '/' + nw[mdex], strict=False)).split('/')[-1]
            return [ip + '/' + mask, gw]
        else:
            return False
    else:
        return False


window = sg.Window('GGS in Python by Romerof', layout, default_element_size=(40, 1), grab_anywhere=False,
                   margins=(18, 18))
event, values = window.read()

while True:  # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break

    if event == 'Automatic':
        loop_ip_test()

    elif event == 'Manual':
        ip_test()

    elif event == "DHCP":
        dynamic_ip()
    elif event == "SHOW IPs":
        show()

    elif values["-IN1-"] == True:
        print("\n- Setting Up for CONTEC PC ... Wait a Moment")
        static_ip()

    elif values["-IN2-"] == True:
        print("\n- Setting Up for CI-5/DRBW-10/RBW-150 ... Wait a Moment")
        static_ip2()

    elif values["-IN3-"] == True:
        print("\n- Setting Up for RBG-200 LAN 1 ... Wait a Moment")
        static_ip3()

    elif values["-IN4-"] == True:
        print("\n- Setting Up for RBG-200 LAN 2 ... Wait a Moment")
        static_ip4()

    elif values["-IN5-"] == True:
        print("\n- Setting Up for NEXCOM LAN 1 ... Wait a Moment")
        static_ip5()

    elif values["-IN6-"] == True:
        print("\n- Setting Up for NEXCOM LAN 2 ... Wait a Moment")
        static_ip6()

window.close()

