from flask import render_template
from shapes import *
from globals import dimensions, colors

Dim = dimensions()
Colors = colors()

def drawRubiks(rubiks):
	Dim = dimensions()
	integer = 1
	html = ""
	position = Dim.origin
	
	#Face 0
	face = 0
	html += render_template('border.html', name=str(face), ypos=str(position[1]),
		xpos=str(position[0]), width=str(3*(Dim.width)+1.8*Dim.gap), 
		height=str(3*(Dim.height)+1.8*Dim.gap), border=Colors.borderColor)  
	
	for x in range(0,3):
		for y in range(0,3):
			html += render_template('square.html', 
				integer=integer, ypos=str(Dim.origin[1]), xpos=str(Dim.origin[0]),
				face=str(face + 1), name=("c" + str(face) + str(x) + str(y)), width=str(Dim.width), 
				height=str(Dim.height), border=Colors.borderColor, 
				color=rubiks.CubeArray[face].FaceMatrix[x][y].Square.Color)
			position[1] += Dim.height + Dim.gap
		position[0] += Dim.width + Dim.gap
		position[1] -= 3*(Dim.height + Dim.gap)
	
	#Face 1
	Dim = dimensions()
	position = Dim.origin
	position[0] += 3*(Dim.width + Dim.gap)
	position[1] += 3*(Dim.height + Dim.gap)
	face = 1
	html += render_template('border.html', name=str(face), ypos=str(position[1]),
		xpos=str(position[0]), width=str(3*(Dim.width)+1.8*Dim.gap), 
		height=str(3*(Dim.height)+1.8*Dim.gap), border=Colors.borderColor)    
	
	for x in range(0,3):
		for y in range(0,3):
			html += render_template('square.html', 
				integer=integer, ypos=str(Dim.origin[1]), xpos=str(Dim.origin[0]),
				face=str(face + 1), name=("c" + str(face) + str(x) + str(y)), width=str(Dim.width), 
				height=str(Dim.height), border=Colors.borderColor, 
				color=rubiks.CubeArray[face].FaceMatrix[x][y].Square.Color)
			position[1] += Dim.height + Dim.gap
		position[0] += Dim.width + Dim.gap
		position[1] -= 3*(Dim.height + Dim.gap)
	
	#Face 2
	Dim = dimensions()
	position = Dim.origin
	position[0] += 3*(Dim.width + Dim.gap)
	face = 2
	html += render_template('border.html', name=str(face), ypos=str(position[1]),
		xpos=str(position[0]), width=str(3*(Dim.width)+1.8*Dim.gap), 
		height=str(3*(Dim.height)+1.8*Dim.gap), border=Colors.borderColor)  
	
	for x in range(0,3):
		for y in range(0,3):
			html += render_template('square.html', 
				integer=integer, ypos=str(Dim.origin[1]), xpos=str(Dim.origin[0]),
				face=str(face + 1), name=("c" + str(face) + str(x) + str(y)), width=str(Dim.width), 
				height=str(Dim.height), border=Colors.borderColor, 
				color=rubiks.CubeArray[face].FaceMatrix[x][y].Square.Color)
			position[1] += Dim.height + Dim.gap
		position[0] += Dim.width + Dim.gap
		position[1] -= 3*(Dim.height + Dim.gap)
		
	#Face 3
	Dim = dimensions()
	position = Dim.origin
	position[0] += 3*(Dim.width + Dim.gap)
	position[1] -= 3*(Dim.height + Dim.gap)
	face = 3
	html += render_template('border.html', name=str(face), ypos=str(position[1]),
		xpos=str(position[0]), width=str(3*(Dim.width)+1.8*Dim.gap), 
		height=str(3*(Dim.height)+1.8*Dim.gap), border=Colors.borderColor)  
	
	for x in range(0,3):
		for y in range(0,3):
			html += render_template('square.html', 
				integer=integer, ypos=str(Dim.origin[1]), xpos=str(Dim.origin[0]),
				face=str(face + 1), name=("c" + str(face) + str(x) + str(y)), width=str(Dim.width), 
				height=str(Dim.height), border=Colors.borderColor, 
				color=rubiks.CubeArray[face].FaceMatrix[x][y].Square.Color)
			position[1] += Dim.height + Dim.gap
		position[0] += Dim.width + Dim.gap
		position[1] -= 3*(Dim.height + Dim.gap)
		
	#Face 4
	Dim = dimensions()
	position = Dim.origin
	position[0] += 6*(Dim.width + Dim.gap)
	face = 4
	html += render_template('border.html', name=str(face), ypos=str(position[1]),
		xpos=str(position[0]), width=str(3*(Dim.width)+1.8*Dim.gap), 
		height=str(3*(Dim.height)+1.8*Dim.gap), border=Colors.borderColor)  
	
	for x in range(0,3):
		for y in range(0,3):
			html += render_template('square.html', 
				integer=integer, ypos=str(Dim.origin[1]), xpos=str(Dim.origin[0]),
				face=str(face + 1), name=("c" + str(face) + str(x) + str(y)), width=str(Dim.width), 
				height=str(Dim.height), border=Colors.borderColor, 
				color=rubiks.CubeArray[face].FaceMatrix[x][y].Square.Color)
			position[1] += Dim.height + Dim.gap
		position[0] += Dim.width + Dim.gap
		position[1] -= 3*(Dim.height + Dim.gap)
		
	#Face 5
	Dim = dimensions()
	position = Dim.origin
	position[0] += 9*(Dim.width + Dim.gap)
	face = 5
	html += render_template('border.html', name=str(face), ypos=str(position[1]),
		xpos=str(position[0]), width=str(3*(Dim.width)+1.8*Dim.gap), 
		height=str(3*(Dim.height)+1.8*Dim.gap), border=Colors.borderColor) 
	
	for x in range(0,3):
		for y in range(0,3):
			html += render_template('square.html', 
				integer=integer, ypos=str(Dim.origin[1]), xpos=str(Dim.origin[0]),
				face=str(face + 1), name=("c" + str(face) + str(x) + str(y)), width=str(Dim.width), 
				height=str(Dim.height), border=Colors.borderColor, 
				color=rubiks.CubeArray[face].FaceMatrix[x][y].Square.Color)
			position[1] += Dim.height + Dim.gap
		position[0] += Dim.width + Dim.gap
		position[1] -= 3*(Dim.height + Dim.gap)
	return html
			
				
	