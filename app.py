from flask import Flask, request, render_template
#import train as baz
app = Flask(__name__)
print("a")
import argparse
print("b")
import torch
print("c")
import numpy as np
print("d")
from torch import nn, optim
print("e")
from torch.utils.data import DataLoader
print("f")
from model import Model
print("g")
from dataset import Dataset

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yes', methods=['POST'])
def updatetext():
    data= "ich bin data"
    return render_template('index.html', data=data )

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    hell = open("input.txt","r+")
    hell.truncate(0)
    hell.write(text)
    hell.close()
    print("logilogi2")
    himmel =open("data/out.csv", "r+")
    top = himmel.read()
    himmel.close()
    print("logilogi1")

    if (str(text) not in str(top)):
      return render_template('index.html',data="Missing Data - 'Menschen' Eike hat darüber noch keinen Witz geschrieben.")  
    else:
      print("logilogi2,6")
      print("logilogi2,4")
      
      print("logilogi2,5")
      from train import dataset, model, text, args  

      print("logilogi3")
      #besult= train.train(dataset,model,args)
      print("logilogi4")
      #result= train.predict(dataset,model,text)
      #train.predict(dataset, model, text, next_words=9)
      #print(result)
      
      holy = open("end.txt", "r+")
      #bdata = holy.read()
      bdata = "jojojo"
      holy.truncate(0)
      holy.close()
      hell = open("input.txt","r+")
      hell.truncate(0)
      hell.close()
    
      
      
      return render_template('index.html',data=bdata)


if __name__ == '__main__':
    app.run()
