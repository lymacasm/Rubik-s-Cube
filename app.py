from flask import Flask
from flask import render_template
import os
from random import choice
from shapes import cube
from graphics import drawRubiks
from rotations import *
from scrambler import scramble, scramble2
from globals import colors

app = Flask(__name__)
Rubiks = cube()
Rubiks.initialize()
#scramble2(Rubiks)
Colors = colors() 
x = 0
y = 0
f = 0

@app.route('/')
def index():
	scramble2(Rubiks)
	squares = drawRubiks(Rubiks)
	return render_template('index.html', squares=squares)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	
	if port == 5000:
		app.debug = True
		
	app.run(host='0.0.0.0', port=port)