from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator
from gtts import gTTS
import os

root=Tk()
root.title("Language Translator")
root.geometry("1080x980")
root.resizable(False,False)
root.configure(background="white")

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)
    language = c1


def translate_now():

    text_=text1.get(1.0,END)
    t1=Translator()
    trans_text=t1.translate(text_,src=combo1.get(),dest=combo2.get())
    trans_text=trans_text.text
    text2.delete(1.0,END)
    text2.insert(END,trans_text)
    trans_text=str(trans_text)
    output = gTTS(text=trans_text, lang="hi", slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")

#icon
image_icon=PhotoImage(file="Bennett.png")
root.iconphoto(False,image_icon)

#Arrow
arrow_image=PhotoImage(file="arrow.png")
image_label=Label(root,image=arrow_image,width=150)
image_label.place(x=460,y=50)
a=1
language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()