# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 18:43:28 2022

@author: anees
"""

from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1080x400')
root.config(bg = '#F2CCC3')
root.title("Language Translator")

language = list(LANGUAGES.values())

title_label = Label(root, text = "LANGUAGE TRANSLATOR", bg='#F2CCC3',font=("Sylfaen",18,"bold","italic"))
title_label.place(relx=0.5,rely=0.1, anchor=CENTER)

input_label = Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='#F2CCC3')
input_label.place(relx=0.02,rely=0.2, anchor=W)

Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60, bg="#FFFCF9", bd=0)
Input_text.place(relx=0.02,rely=0.5, anchor=W)

source_language = ttk.Combobox(root,values=language,width=22,state="readonly")
source_language.place(relx=0.13,rely=0.2,anchor=W)
source_language.set('English')

output_label = Label(root,text ="Output", font = 'arial 13 bold', bg ='#F2CCC3')
output_label.place(relx=0.81,rely=0.2, anchor=W)

output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60, bg="#FFFCF9", bd=0)
output_text.place(relx=0.98,rely=0.5, anchor=E)

destination_language = ttk.Combobox(root,values=language,width=22,state="readonly")
destination_language.place(relx=0.8,rely=0.2,anchor=W)
destination_language.set('Choose Output Language')

def translate():
    translator = Translator()
    try:
        translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)
    except:
        print("Try Again")
        
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = translate , bg = '#E78F8E', activebackground = '#95A3A4',relief = FLAT)
trans_btn.place(relx=0.5,rely=0.85, anchor=CENTER )
footer_label = Label(root,text ="Created by Aneesh Parasa", font = 'arial 10 italic', bg ='#F2CCC3')
footer_label.place(relx=0.5,rely=0.97, anchor=CENTER)

root.mainloop()  