'''
Onildo Pereira da Costa junior - UTF-8 - pt-br - 17-04-2024
projeto_x.py
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def olamundo():
    return 'Te amo meu amor',200

app.run(host='0.0.0.0', port=5000)
