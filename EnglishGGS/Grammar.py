import PySimpleGUI as sg
# Before:  pip install googletrans==3.1.0a0
from googletrans import Translator
import googletrans

# Initial
translator = googletrans.Translator()

theme_dict = {'BACKGROUND': '#2B475D',
              'TEXT': '#FFFFFF',
              'INPUT': '#F2EFE8',
              'TEXT_INPUT': '#000000',
              'SCROLL': '#F2EFE8',
              'BUTTON': ('#000000', '#C2D4D8'),
              'PROGRESS': ('#FFFFFF', '#C7D5E0'),
              'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

# sg.theme_add_new('Dashboard', theme_dict)     # if using 4.20.0.1+

sg.LOOK_AND_FEEL_TABLE['Dashboard'] = theme_dict
sg.theme('Dashboard')
BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20, 10), (20, 10))
BPAD_LEFT = ((10, 5), (10, 20))
BPAD_LEFT_INSIDE = (0, 5)
BPAD_RIGHT = ((5, 20), (10, 20))


value_list = ["0   -  Present Simple","1   -  Prepositions IN ON AT","2   -  Prepositions of Place","3   -  Time","4   -  Date","5   -  Pronunciation of -ED","6   -  PRESENT SIMPLE vs CONTINUOUS",
              "7   -  Questions with Do / Does","8   -  This That These Those","9   -  Question Words","10  -  A - An - Some - Any", "11 -  Very vs Too",
              "12 -  Too + Adjetive", "13 -  So & Too","14 -  Adj. -ED -ING", "15 -  Adj Comparatives-Superlatives", "16 -  Past to Be ( WAS - WERE )", "17 -  DO Verb / DO Aux.",
              "18 -  Do vs Make","19 -  Much / Many","20 -  HOW Much / HOW Many","21 -  PAST SIMPLE vs PRESENT PERFECT" ,"22 -  Few vs Little", "23 -  Adverbs of Frecuency" ,
              "24 -  How Often","25 -  Adverbs of Manner","26 -  FUTURE ( Will vs Going to )","27 -  [ STILL ] - Yet - Already","28 -  Still - [ YET ] - Already" ,
              "29 -  Still - Yet - [ ALREADY ]","30 -  CONDITIONALS","31 -      ZERO Conditional","32 -      FIRST Conditional","33 -      SECOND Conditional","34 -      THIRD Conditional"
              ,"35 -  For Vs Since","36 -  Like vs As","37 -  All - Every - Each","38 -  Another - Other - Others","39 -  Both - Either - Neither","40 -  MODALS VERBS","41 -      CAN - COULD",
              "42 -      MAY - MIGHT","43 -      MUST ( Must vs Have to )","44 -      MUSTN' T vs DON'T HAVE to","45 -      SHALL","46 -      WILL","47 -      SHOULD ( Should vs OUGHT To)"
              ,"48 -      USE to vs WOULD","49 -      PAST MODALS of DEDUCTION","50 -  QUESTION TAGS","51 -      POSITIVE Question Tags","52 -      NEGATIVE Question Tags",
              "53 -  LIKE Preposition vs LIKE Verb","54 -  Passive Voice"]


top_banner = [[sg.Text('Grammar Pills' + ' ' * 75, font='Any 20', background_color=DARK_HEADER_COLOR),
               sg.Text('By Romerof', font='Any 20', background_color=DARK_HEADER_COLOR)]]

block_3 = [[sg.Text('Translator', font='Any 20')],
           [sg.Input(size=(31, 1))],
           [sg.Button('English'),sg.Button('Español')]]

block_2 = [[sg.Text('Grammar', font='Any 20')],
           [sg.Listbox(value_list, enable_events=True, key="-LISTBOX-", size=(38, 18)) ],
            [sg.StatusBar("", size=(30, 1), key='-STATUS-')]
           ]

# [sg.Image(data=sg.DEFAULT_BASE64_ICON)]


block_4 = [[sg.Image(key='-IMAGE-')]

           ]

layout = [[sg.Column(top_banner, size=(975, 55), pad=(0, 0), background_color=DARK_HEADER_COLOR)],
          [sg.Column([[sg.Column(block_2, size=(329, 368), pad=BPAD_LEFT_INSIDE)],
                      [sg.Column(block_3, size=(329, 100), pad=BPAD_LEFT_INSIDE)],[sg.Output(size=(38, 2), key='-OUTPUT-')]], pad=BPAD_LEFT,
                     background_color=BORDER_COLOR),
           sg.Column(block_4, size=(623, 538), pad=BPAD_RIGHT)]]

window = sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0, 0), background_color=BORDER_COLOR,finalize=True,
                    grab_anywhere=True)
listbox, status = window['-LISTBOX-'], window['-STATUS-']

while True:  # Event Loop
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == '-LISTBOX-':
        selection = values[event]
        if selection:
            item = selection[0]
            index = listbox.get_indexes()[0]


            if index == 0:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\present.png"))
            elif index == 1:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\prepositions.png"))
            elif index == 2:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\prepositions place.png"))
            elif index == 3:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\time.png"))
            elif index == 4:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\date.png"))
            elif index == 5:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\ed.png"))
            elif index == 6:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\present cont.png"))
            elif index == 7:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\do does.png"))
            elif index == 8:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\this - that - these - those.png"))
            elif index == 9:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\q words.png"))
            elif index == 10:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\a - an - some - any.png"))
            elif index == 11:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\very too.png"))
            elif index == 12:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\too.png"))
            elif index == 13:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\so too.png"))
            elif index == 14:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\adj ed ing.png"))
            elif index == 15:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\adj.png"))
            elif index == 16:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\was were.png"))
            elif index == 17:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\do.png"))
            elif index == 18:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\do make.png"))
            elif index == 19:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\much many.png"))
            elif index == 20:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\how muchmany.png"))
            elif index == 21:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\past simple vs present perfect many.png"))
            elif index == 22:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\few vs little.png"))
            elif index == 23:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\Adv frec.png"))
            elif index == 24:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\how often.png"))
            elif index == 25:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\Adv manner.png"))
            elif index == 26:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\will going to.png"))
            elif index == 27:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\still.png"))
            elif index == 28:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\yet.png"))
            elif index == 29:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\already.png"))
            elif index == 30:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\conditionals_.png"))
            elif index == 31:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\conditional0.png"))
            elif index == 32:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\conditional1.png"))
            elif index == 33:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\conditional2.png"))
            elif index == 34:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\conditional3.png"))
            elif index == 35:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\for since.png"))
            elif index == 36:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\like as.png"))
            elif index == 37:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\all-every-each.png"))
            elif index == 38:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\another other others.png"))
            elif index == 39:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\both either neither.png"))
            elif index == 40:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\modals.png"))
            elif index == 41:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\can could.png"))
            elif index == 42:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\may might.png"))
            elif index == 43:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\must.png"))
            elif index == 44:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\mustnt.png"))
            elif index == 45:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\shall.png"))
            elif index == 46:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\will going to.png"))
            elif index == 47:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\should ought to.png"))
            elif index == 48:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\use.png"))
            elif index == 49:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\past modals.png"))
            elif index == 50:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\tag.png"))
            elif index == 51:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\positive tag.png"))
            elif index == 52:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\negative tag.png"))
            elif index == 53:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\like.png"))
            elif index == 54:
                window["-IMAGE-"].update(filename=(r"C:\dashboard\passive.png"))



    elif event == 'English':
        print(translator.translate(values[0], src='es', dest='en').text)
        window['-OUTPUT-'].update()

    elif event == 'Español':
        print(translator.translate(values[0], src='en', dest='es').text)
        window['-OUTPUT-'].update()







window.close()
