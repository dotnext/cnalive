from flask import Flask, url_for, redirect, render_template
import os
from cfenv import AppEnv

env = AppEnv()


try:
    filename = str(os.environ['FILENAME'])
except KeyError:
    filename = "counter.txt"

app = Flask(__name__)

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@app.route('/')
def default():
    counter = 0
    try:
        fo = open(filename, "r")
        counter = fo.readline()
        fo.close()
        if is_number(counter):
            counter = int(counter) + 1
        else:
            counter = 1
    except:
        print("No File Found, Starting new one")

    fo = open(filename,'w')
    fo.write(str(counter))
    fo.close()
    return render_template('index.html',title="Basic Title", counter=counter, filename=filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=env.port)