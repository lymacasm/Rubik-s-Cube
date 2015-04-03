import copy
from random import shuffle
from shapes import cube
from rotations import *

def scramble(rubiks):
	corners = []
	sides = []
	for f in range(0,6):
		for r in range(0,3):
			for c in range(0,3):
				if r == 1 and c == 1:
					break
				if r == 1 or c == 1:
					sides.append(copy.deepcopy(rubiks.CubeArray[f].FaceMatrix[r][c]))
				else:
					corners.append(copy.deepcopy(rubiks.CubeArray[f].FaceMatrix[r][c]))
					
	shuffle(corners)
	shuffle(sides)
	sidesIndex = 0
	cornersIndex = 0
	for f in range(0,6):
		for r in range(0,3):
			for c in range(0,3):
				if r == 1 and c == 1:
					break
				if r == 1 or c == 1 and sidesIndex < len(sides):
					rubiks.CubeArray[f].FaceMatrix[r][c] = sides[sidesIndex]
					sidesIndex += 1
				elif cornersIndex < len(corners):
					rubiks.CubeArray[f].FaceMatrix[r][c] = corners[cornersIndex]
					cornersIndex += 1
	
	return rubiks
	
def scramble2(rubiks):
	iterations = 5
	moves = []
	for i in range(0,iterations):
		moves.append(rotateL)
		moves.append(rotateLi)
		moves.append(rotateR)
		moves.append(rotateRi)
		moves.append(rotateU)
		moves.append(rotateUi)
		moves.append(rotateD)
		moves.append(rotateDi)
		moves.append(rotateF)
		moves.append(rotateFi)
		moves.append(rotateB)
		moves.append(rotateBi)
		
	shuffle(moves)
	for i in range(0,len(moves)):
		moves[i](rubiks)
	
					