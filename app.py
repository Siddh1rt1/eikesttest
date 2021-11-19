from flask import Flask, request, render_template

app = Flask(__name__)


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
      #data = text.upper()
      print("logilogi2,6")
      print("logilogi2,4")
      #import train
      print("logilogi2,5")
      #from train import dataset, model, text, args  

      print("logilogi3")
      #besult= train.train(dataset,model,args)
      print("logilogi4")
      #result= train.predict(dataset,model,text)
      #train.predict(dataset, model, text, next_words=9)
      #print(result)
      
      holy = open("end.txt", "r+")
      bdata = holy.read()
      holy.truncate(0)
      holy.close()
      hell = open("input.txt","r+")
      hell.truncate(0)
      hell.close()
    
      
      
      return render_template('index.html',data=bdata)


if __name__ == '__main__':
    app.run()
