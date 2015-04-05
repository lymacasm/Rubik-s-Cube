from globals import *
import copy

Colors = colors()

# This function maps the face to the opposite face of cube
# SHOULD MOVE TO GLOBALS.PY
def faceMapper(face):
	if face == 0:
		return 4
	elif face == 1:
		return 3
	elif face == 2:
		return 5
	elif face == 3:
		return 1
	elif face == 4:
		return 0
	elif face == 5:
		return 2

# Finds the largest value in an array
def findIndexOfMax(array):
	max = 0
	index = 0
	for i in range(0, len(array)):
		if array[i] > max:
			max = array[i]
			index = i
	return index
		

class Solve:
	def __init__(self, rubiks):
		self.Rubiks = rubiks
		self.Cross = ""
		self.Count = 0
		
	def Update(self, rubiks):
		self.Rubiks = rubiks
	
	# Chooses which color cross is best to go for
	def ChooseCross(self):
		# This array is used to count 
		# the number of side square occurrences
		# of a specific color on a face. Each face is 
		# represented by the index of the array
		faceArray = []
		for i in range(0,6):
			faceArray.append(int())
		
		for f in range(0,6):
			for x in range(0,3):
				for y in range(0,3):
					if x != y and x == 1 or y == 1:
						if (self.Rubiks.CubeArray[f].FaceMatrix[x][y].Square.Color == 
							Colors(faceColors.intToString(faceMapper(f)))):
							faceArray[f] += 1
							
		face = faceMapper(findIndexOfMax(faceArray))
		self.Cross = faceColors.intToString(face)
	
	# Chooses best direction to go to make a cross
	def MakeCross(self):
		# Checks to see if there is a piece lined up for an easy cross placement
		def CheckStrip(position):
			rubiksCopy = copy.deepcopy(self.Rubiks)
			moves = []
			f = position[0]
			x = position[1]
			y = position[2]
			if x == 0:
				if f == 0:
					for i in range(0,3):
						rotate.left()
						moves.append(rotate.left)
						if (Colors(rubiksCopy.CubeArray[f].FaceMatrix[x][y].Square.Color) ==
							self.Cross):
							return moves
				elif f == 1:
					for i in range(0,3):
						 
							
			
			
			
			