from flask import Flask, request, render_template

my_awesome_app = Flask(__name__)


@my_awesome_app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/updatetext', methods=['POST'])
def updatetext():
    data= "ich bin data"
    return render_template('index.html', data=data )

if __name__ == '__main__':
    my_awesome_app.run()
