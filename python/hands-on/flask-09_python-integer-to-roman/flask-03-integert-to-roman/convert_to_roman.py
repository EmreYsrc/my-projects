from flask import Flask, render_template
from numpy import number

app = Flask(__name__)

@app.route('/')
def cevir():
        
    result = 2546
        
    dict_roman = { 
        0:"",
        1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",
        10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LI",70:"LII",80:"LIII",90:"XC",
        100:"C",200:"CC",300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM",
        1000:"M"
                }
    binler = (result // 1000)
    yuzler = (result % 1000)//100
    onlar = (result % 100)//10
    birler =  result % 10
    number = (dict_roman[1000]*binler + dict_roman[yuzler*100] + dict_roman[onlar*10]+dict_roman[birler])
    return render_template('index.html',number1=number)          
        
if __name__=='__main__':
    app.run(debug = True)