from tkinter import *
import playsound
from gtts import gTTS
from deep_translator import GoogleTranslator
import googletrans
import os
from tkinter import ttk, messagebox

window = Tk()
language = googletrans.LANGUAGES
language_value = list(language.values())
lbl0 = Label(window, text='Feel at home', bg='white')
lbl0.place(x=300, y=2, width=600)
comb1 = ttk.Combobox(window, values=language_value, font='calibri 12', state='r')
comb1.place(x=5, y=100, width=600)
comb2 = ttk.Combobox(window, values=language_value, font='Verdana 12', state='r')
# this is where we extract languages and their from googletrans

value = comb2.get()


# Function that helps you to get key of any languages
def get_key(val):
    for key, value in language.items():
        if val == value:
            return key


# Function that is going to be passed in translate button for translation
def trans():
    try:
        value = comb2.get()
        comb2.set(value)
        tar = get_key(str(value))
        tex = text1.get(1.0, END)
        translate = tex

        translated = GoogleTranslator(source='auto', target=tar).translate(translate)
        text2.delete(1.0, END)
        text2.insert(END, translated)
    except Exception as e:
        messagebox.showerror('warning', 'please make sure that you have chosen the language to translate into')


# this is the design of the layout of the interface
comb2.place(x=650, y=100, width=600)
lbl1 = Label(window, text='Welcome to your friendly translator', font='verdana 12', bg='white')
lbl1.place(x=5, y=50, width=600)
lbl2 = Label(window, text='select the language you want to translate into', font='verdana 12', bg='white')
lbl2.place(x=650, y=50, width=600)

f1 = Frame(window, bg='white', bd=10)
f1.place(x=5, y=200, width=600, height=400)
text1 = Text(f1, font='verdana 12', bg='white', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=550, height=400)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side='right', fill='y')
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)
lbl3 = Label(window, text='Write the text you want to translate below', font='Verdana', bg='white')
lbl3.place(x=5, y=150, width=600)
lbl4 = Label(window, text='the translated text is below', font='Verdana', bg='white')
lbl4.place(x=650, y=150, width=600)
f2 = Frame(window, bg='white', bd=10)
f2.place(x=650, y=200, width=600, height=400)
text2 = Text(f2, font='verdana 12', bg='white', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=550, height=400)
scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side='right', fill='y')
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


# button 1 command
def but1():
    try:
        tex1 = text1.get(1.0, END)
        value = comb1.get()
        comb1.set(value)
        langue = get_key(str(value))
        myaudio1 = gTTS(text=tex1, lang=langue, slow=True)
        myaudio1.save('transla.mp3')
        try:
            playsound.playsound("transla.mp3")
        except:
            os.system("transla.mp3")

    except Exception as e:
        messagebox.showerror('warning', 'the language you selected is not supported by this application')


# Function for reading out the content of frame two
def but2():
    try:
        tex2 = text2.get(1.0, END)
        value = comb2.get()
        comb2.set(value)
        langue = get_key(str(value))
        myaudio = gTTS(text=tex2, lang=langue, slow=True)
        myaudio.save('translated.mp3')
        try:
            playsound.playsound("translated.mp3")
        except:
            os.system("translated.mp3")


    except Exception as e:
        messagebox.showerror('Warning', 'the language you selected is not supported by this application')


def save1():
    try:
        tex1 = text1.get(1.0, END)
        value = comb1.get()
        comb1.set(value)
        langue = get_key(str(value))
        myaudio1 = gTTS(text=tex1, lang=langue, slow=True)
        myaudio1.save('audio file for text1.mp3')
    except:
        messagebox.showerror('Warning', 'the language you selected is not supported by this application')


def save2():
    try:
        tex2 = text2.get(1.0, END)
        value = comb2.get()
        comb2.set(value)
        langue = get_key(str(value))
        myaudio = gTTS(text=tex2, lang=langue, slow=True)
        myaudio.save('audio file for text2.mp3')
    except:
        messagebox.showerror('Warning', 'the language you selected is not supported by this application')

    # button for reading out frame 1


button = Button(window, text='listen', bg='white', font='verdana 12', activebackground='purple', command=but1)
button.place(x=5, y=610, width=200)
# button for saving the audio file only
b4 = Button(window, text="save the file audio only", bg='white', font='verdana 12', activebackground='purple',
            command=save1)
b4.place(x=250, y=610, width=200)
# button for reading out frame 2
b3 = Button(window, text='listen', bg='white', font='verdana 12', activebackground='red', cursor='hand2', command=but2)
b3.place(x=650, y=610, width=200)
b5 = Button(window, text="save the file audio only", bg='white', font='verdana 12', activebackground='purple',
            command=save2)
b5.place(x=900, y=610, width=200)
# Button for translation
trans = Button(window, text='Translate', bg='white', font='verdana 6 italic', bd=5, activebackground='purple',
               cursor='hand2', command=trans)
trans.place(x=601, y=350, width=49)
window.geometry('4000x4000')
window.title('TRANSLATOR AND TEXT TO SPEECH PROGRAMM')
window.configure(bg='light gray')
window.mainloop

# references:
# we draw mor insight on this website such getting to know different modules to use for different purpose
# GeeksforGeeks | A computer science portal for geeks
# https://www.geeksforgeeks.org


