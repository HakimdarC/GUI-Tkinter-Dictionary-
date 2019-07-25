from tkinter import *

windows=Tk()

import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json",'r'))

def translate(w):
    w = w.get()
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        return "Did u mean %s instead!!! "%get_close_matches(w, data.keys())[0]
    else:
        return "The word does not exist please double check it!!!"

def afficher(list):
    output = translate(w) 
    if type(output) == list:
        for items in output.items():
            return items
    else:
        return output
    
        
def translatetk():
    wd = translate(w)
    afficher(wd)
    t1.delete("1.0", END)
    t1.insert(END,wd)

    
b1=Button(windows,text="search",command=translatetk)
b1.grid(row=0,column=2)

e0=Label(windows,text="Dict@Hakim")
e0.grid(row=0,column=0)

w=StringVar()
e1=Entry(windows,textvariable=w)
e1.grid(row=0,column=1)

t1=Text(windows,height=8,width=80)
t1.grid(row=1,column=1)





windows.mainloop()
