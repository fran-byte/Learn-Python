import PySimpleGUI as sg
import pandas as pd
import webbrowser





sg.theme('Light Green 5')

# sg.ChangeLookAndFeel('GreenTan')

 
# ------ Menu Definition ------ #

menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],

            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],

            ['&Help', '&About...'], ]

 

# ------ Column Definition ------ #

 


 


 

layout = [

 
   [sg.Text('B R M  -  1 0  Error Log Analysis Tools', size=(46, 1), justification='center', text_color='#00226F',

             font=("Helvetica", 19), relief=sg.RELIEF_RIDGE)],

       [
        sg.Graph(
            canvas_size=(1065, 460),
            graph_bottom_left=(0, 0),
            graph_top_right=(1065, 460),
            key="-GRAPH-"
        )
    ],

    

     [sg.Frame('Error Code: [ XXXX ] ', 

        [[sg.Input(size=(25, 1),  enable_events=True)],

        [sg.Button('Display Error Code', size=(22, 1))],
        [sg.Button('Submit', visible=False, bind_return_key=True)]], title_color='#00226F')],



    [sg.Frame('PDF Viewer ', [

        [sg.Button('Part LIST', size=(22, 1)),sg.Button('RAS TEST', size=(22, 1))],

        ], title_color='#00226F', )]

    

]





window = sg.Window('GGS in Python by Romerof', layout, default_element_size=(40, 1), grab_anywhere=False, margins=(18, 18))
window.Finalize()


event, values = window.read()

graph = window.Element("-GRAPH-")

graph.DrawImage(filename="C:/Users/franc/Desktop/1.png", location=(1, 450))
 


def circle_position(x,y,r):

   graph.DrawCircle((x,y), r, line_color='red')


id = None

while True:  # Event Loop
    

    event, values = window.Read()

    if event in (None, 'Exit'):

        break

 
    

# **************************** RAS TEST  **********************************************************

 

    if (event == 'RAS TEST'):

       
        webbrowser.open('T:/INFOTEC/Nivel 2 [REPAIR]/RECICLADORES/BRM-10/2020_BRM-10_(RAS_Specification)_(TMB6-7948-07)_(Level6).pdf#page=3')
      
# **************************** PART LIST  **********************************************************
    

    elif (event =="Part LIST"):

        webbrowser.open('C:/Users/franc/Desktop/brm-10.pdf')



# **************************** ERRORS LOG **********************************************************


    elif (event =="Display Error Code") or (event == 'Submit'):

        if (values[0] == "1001") :

          
            graph.Erase()
            circle_position(324,257,16)

        if (values[0] == "1002") :

            
            graph.Erase()
            circle_position(342,303,16)






window.close()