from flask import Flask, url_for, redirect, render_template
import os
from cfenv import AppEnv
import redis
env = AppEnv()


app = Flask(__name__)

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@app.route('/')
def default():
###################################################################
    redis_connection_info = env.services[0].credentials

    r = redis.StrictRedis(
            host=redis_connection_info['host'],
            port=redis_connection_info['port'],
            password=redis_connection_info['password']
    )
    counter = r.get('counter')
    if not counter:
        counter = 1
    else:
        counter = int(counter) + 1
    r.set('counter',counter)

################################################################
    return render_template('index.html',title="Basic Title", counter=counter, filename="redis")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=env.port)