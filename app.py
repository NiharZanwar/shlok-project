from flask import Flask, render_template, request
import json
from time import sleep
from functions import add_user

app = Flask(__name__)

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/world')
def world():
    return render_template('world.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/accecpt_values', methods=['POST'])
def accecpt_values():

    data_string = request.get_data(as_text=True)
    data = json.loads(data_string)
    print(data["name"])

    add_user(data["name"],'hello','hello')

    sleep(4)
    return json.dumps({"success":0,
                       "message":"some error occured"})


if __name__ == '__main__':
    app.run(port=5010, debug=True)