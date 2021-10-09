import sys
import fitz
import PySimpleGUI as sg
#fname = sys.argv[1]
fname = 'C:/test.pdf'
doc = fitz.open(fname)
#title = "PyMuPDF display of '%s' (%i pages)" % (fname, len(doc))
 
def get_page(pno):
    pix = doc[pno].getPixmap(alpha = False)
    return pix.getPNGData()
 
#form = sg.FlexForm(title)
 
data = get_page(0)
image_elem = sg.Image(data=data)
layout = [  [image_elem],
            [sg.ReadFormButton('Next'),
             sg.ReadFormButton('Prev'),
             sg.ReadFormButton('First'),
             sg.ReadFormButton('Last'),
             sg.Quit()]  ]
 
form.Layout(layout)
i = 0
while True:
    button,value = form.Read()
    if button in (None, 'Quit'):
        break
    i -= 1 * button == 'Prev'
    i += 1* button == 'Next'
    i = 0 if button =='First' else -1 if button == 'Last' else i
    try:
        data = get_page(i)
    except:
        i = 0
        data = get_page(i)
    image_elem.Update(data=data)