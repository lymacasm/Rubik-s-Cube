from flask import Flask
from flask import render_template
import os
from random import choice
from shapes import cube
from graphics import drawRubiks
from rotations import *
from scrambler import scramble, scramble2
from globals import colors
import pprint

app = Flask(__name__)
Rubiks = cube()
Rubiks.initialize()
scramble2(Rubiks)
Colors = colors() 

rotateStringToFunc = {
	"right" : rotate.right,
	"right-inverse" : rotate.rightInv,
	"left" : rotate.left,
	"left-inverse": rotate.leftInv,
	"up": rotate.upper,
	"up-inverse": rotate.upperInv,
	"down": rotate.down,
	"down-inverse": rotate.downInv,
	"front": rotate.front,
	"front-inverse": rotate.frontInv,
	"back": rotate.back,
	"back-inverse": rotate.backInv
}

@app.route('/')
def index():
	squares = drawRubiks(Rubiks)
	return render_template('index.html', squares=squares)

@app.route('/update')
def update(): 
	rotate.leftInv(Rubiks)
	squares = drawRubiks(Rubiks)
	return squares

@app.route('/move/<direction>')
def move(direction):
	rotateStringToFunc[direction](Rubiks)
	squares = drawRubiks(Rubiks)
	return squares 

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	
	if port == 5000:
		app.debug = True
		
	app.run(host='0.0.0.0', port=port)