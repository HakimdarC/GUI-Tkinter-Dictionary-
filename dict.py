import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json",'r'))

def translate(w):
        w = w.lower()
        if w in data:
            return data[w]
        elif len(get_close_matches(w, data.keys()))>0:
            op= input("Did u mean %s instead!!!,Enter Y if yes AND N if no: " %get_close_matches(w, data.keys())[0])
            if op == "Y":
                return data[get_close_matches(w, data.keys())[0]]
            elif op == "N":
                return "word doesn't exist!!!, Please double check it."
            else:
                return "entry invalid."
        else:
            return "The word does not exist please double check it!!!"
        
word="TRUE"
while word:
    word = input("Enter word: ")
    if word == 'exit': break
    output = translate(word)
    if type(output) == list:
        for items in output:
            print(items)
    else:
        print(output)
    

                
                

                



        

