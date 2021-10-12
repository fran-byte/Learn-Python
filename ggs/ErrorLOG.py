import PySimpleGUI as sg
import pandas as pd
import webbrowser

# Excel to dictionary

df = pd.read_excel('C:/Users/franc/Desktop/DICCIONARY_ERROS_LOG.xlsx', header=0, usecols="A,B")




sg.theme('Light Green 5')

# sg.ChangeLookAndFeel('GreenTan')

 
# ------ Menu Definition ------ #

menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],

            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],

            ['&Help', '&About...'], ]

 

# ------ Column Definition ------ #

 

colum1 = [

    [sg.Frame(layout=[

        [sg.Radio('BRM-10', "RADIO1", default=True, size=(16, 1), key="-IN1-")],

        [sg.Radio('CI-5  [RBW-50]', "RADIO1", default=True, size=(16, 1), key="-IN2-"),

        sg.Radio('CI-5  [RCW-50]', "RADIO1", default=True, size=(16, 1), key="-IN3-")],

        [sg.Radio('CI-10B [RBW-100]', "RADIO1", default=True, size=(16, 1), key="-IN4-")

         ,sg.Radio('CI-10C [RCW-100]', "RADIO1", default=True, size=(16, 1), key="-IN5-")],

        [sg.Radio('CI-100  [SDRB-100]', "RADIO1", default=True, size=(16, 1), key="-IN6-"),

        sg.Radio('[SDRC-100]', "RADIO1", default=True, size=(16, 1), key="-IN7-")]],

        title='Machine', title_color='#00226F', relief=sg.RELIEF_SUNKEN)]]

 

colum2 = [

    [sg.Frame('Option ', [[sg.Radio('RAS TEST', "RADIO2", key="-IN9-"),

        sg.Radio('Part LIST', "RADIO2", key="-IN10-")],

        [sg.Button('Search PDF', size=(18, 1))],

        ], title_color='#00226F', )]

      ]

 

layout = [

 
   [sg.Text('Error Log', size=(43, 1), justification='center', text_color='#00226F',

             font=("Helvetica", 19), relief=sg.RELIEF_RIDGE)],

       [sg.Column(colum1), sg.Column(colum2)] ,

    [sg.Frame('Error Code: [ XXXX ] ', 

        [[sg.Input(size=(31, 1),  enable_events=True)],

        [sg.Button('Display Error Code'),sg.Button("Sensor and Actuator Layout")],

    [sg.Output(size=(85, 12), key='-OUTPUT-')]], title_color='#00226F')],[sg.Button('Submit', visible=False, bind_return_key=True)]

    

]



window = sg.Window('GGS in Python by Romerof', layout, default_element_size=(40, 1), grab_anywhere=False, margins=(18, 18))

event, values = window.read()

 

while True:  # Event Loop

    event, values = window.Read()

    if event in (None, 'Exit'):

        break

 
    

# **************************** RAS TEST  **********************************************************

 

    if (event == 'Search PDF') and (values["-IN1-"] == True) and (values["-IN9-"] == True):

        print("\n- Open RAS Test PDF in Browser -")


        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/BRM-10/2020_BRM-10_(RAS_Specification)_(TMB6-7948-07)_(Level6).pdf#page=3')
      

    elif (event == 'Search PDF') and (values["-IN2-"] == True)  and (values["-IN9-"] == True):

        print("\n- Open RAS Test PDF in Browser -")


        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/Cash Infinity/CI-5/RBW-50/2019_RBW-50_(RAS_Specifications)_(TMB6-9854-01)_(Level2.5).pdf#page=3')


    elif (event == 'Search PDF') and (values["-IN3-"] == True)  and (values["-IN9-"] == True):

        print("\n- Open RAS Test PDF in Browser -")

  
        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/Cash Infinity/CI-5/RCW-50/2018_RCW-50_(RAS_Specifications)_(TMB6-9858-00)_(Level2.5).pdf#page=3')


    elif (event == 'Search PDF') and (values["-IN4-"] == True)  and (values["-IN9-"] == True):

        print("\n- Open RAS Test PDF in Browser -")

   
        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/Cash Infinity/CI-10/RBW-100 (CI-10B)/2018_RBW-100A_(RAS_Specifications(USA))_(TMB6-7175-06)_(Level2).pdf#page=3')


    elif (event == 'Search PDF') and (values["-IN5-"] == True)  and (values["-IN9-"] == True):

        print("\n- Open RAS Test PDF in Browser -")       

        
        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/Cash Infinity/CI-10/RCW-100 (CI-10C)/2019_RCW-100_(RAS_Specifications)_(TMB6-7122-09)_(Level2.5).pdf#page=3')


    elif (event == 'Search PDF') and (values["-IN6-"] == True)  and (values["-IN9-"] == True):

        print("\n- Open RAS Test PDF in Browser -")

        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/Cash Infinity/CI-100/SDRB-100/2019_SDRB-100_(RAS_Spec)_(TMB6-7221-17)_(Level.2.5).pdf#page=3')


    elif (event == 'Search PDF') and (values["-IN7-"] == True)  and (values["-IN9-"] == True):

        print("\n- Open RAS Test PDF in Browser -")

      
        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/Cash Infinity/CI-100/SDRC-100/2014_SDRC-100_(RAS_Specifications)_(TMB6-7179-05)(Level2).pdf#page=3')

 

# ****************************** PART LIST *******************************************************

    elif (event == 'Search PDF') and (values["-IN1-"] == True) and (values["-IN10-"] == True):

        print("\n- Open Part List PDF in Browser -")

        
        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/BRM-10/2021_BRM-10_(Parts_list)_(TMB7-3471-04)_(Level6).pdf')

  
    elif (event == 'Search PDF') and (values["-IN2-"] == True)  and (values["-IN10-"] == True):

        print("\n- Open Part List PDF in Browser -")

        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/Cash Infinity/CI-5/RBW-50/2021_RBW-50_(Spare_Parts_List)_(TMB7-3841-10)_(Level2).pdf')


    elif (event == 'Search PDF') and (values["-IN3-"] == True)  and (values["-IN10-"] == True):

        print("\n- Open Part List PDF in Browser -")
 

        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/Cash Infinity/CI-5/RCW-50/2020_RCW-50_(SparePartsList)_(TMB7-3847-03)_(Level2).pdf')


    elif (event == 'Search PDF') and (values["-IN4-"] == True)  and (values["-IN10-"] == True):

        print("\n- Open Part List PDF in Browser -")

    
        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/Cash Infinity/CI-10/RBW-100 (CI-10B)/2021_RBW-100_(Spare_Parts_List(ForFieldTechnician))_(TMB7-3490-11)_(Level2_6).pdf')


    elif (event == 'Search PDF') and (values["-IN5-"] == True)  and (values["-IN10-"] == True):

        print("\n- Open Part List PDF in Browser -")
 

        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/Cash Infinity/CI-10/RCW-100 (CI-10C)/2021_RCW-100_(Parts_list)_(TMB7-3210-10)_(Level6).pdf')


    elif (event == 'Search PDF') and (values["-IN6-"] == True)  and (values["-IN10-"] == True):

        print("\n- Open Part List PDF in Browser -")


        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/Cash Infinity/CI-100/SDRB-100/2021_SDRB-100_(Parts_List)_(TMB7-3183-15)_(Level6).pdf')


    elif (event == 'Search PDF') and (values["-IN7-"] == True)  and (values["-IN10-"] == True):

        print("\n- Open Part List PDF in Browser -")


        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/Cash Infinity/CI-100/SDRC-100/2020_SDRC-100_(Spare_Parts_List(Forfield_technician))_(TMB7-3494-12)_(Level.2.6).pdf')

 

# ********************************** ERRORS LOG *****************************************************************

 
    elif ((event == 'Display Error Code') or (event == 'Submit')) and  (values["-IN1-"] == True)  and (values[0]) :

        print("\n                                                 - [ BRM-10 - ERROR CODE ] -")

        print("\n--------------------------------------------------------------------------------------------------------------------------------------------------")

        print(df[df["COD"] == values[0] ].head().to_string(index=False, justify='center'))

        print("\n--------------------------------------------------------------------------------------------------------------------------------------------------")

        print("\n")

        


    elif (event =="Sensor and Actuator Layout") and  (values["-IN1-"] == True):

        print("\n- Open Sensor and Actuator Layout PDF in Browser -")

        webbrowser.open('C:/Users/franc/Desktop/brm-10.pdf')


window.close()