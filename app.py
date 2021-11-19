from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/updatetext', methods=['POST'])
def updatetext():
    data= "ich bin data"
    return render_template('index.html', data=data )

if __name__ == '__main__':
    app.run()
