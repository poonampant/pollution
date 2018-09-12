from flask import Flask
import os

app=Flask(__name__)

port=int(os.getenv("PORT"))

@app.route('/')
def hello_world():
    return 'Welcome'

if __name__=='__main__':
    #port=8080
    app.run(host='0.0.0.0',port=port)
