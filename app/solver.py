from rotations import *
from globals import colors, faceColors
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
		self.Rubiks = rubiks # The rubiks cube
		self.Cross = "" # The color of the cross
		self.Count = 0 # The number of turns taken
		self.Moves = [] # A queue of moves to execute
		
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
	
	    #### Checks to see if there is a piece lined up for an easy cross placement
		def CheckStrip(position):
		
		    #### Rotates three times in one direction to make a check
			def RotateCheck(direction, directionInv, f, x, y):
				rubiksCopy = copy.deepcopy(self.Rubiks)
				# Make moves to rubiksCopy, and see if we get a desired result
				for i in range(0,3):
					direction(rubiksCopy)
					self.Moves.append(direction)
					# if the color at position is now the color we want
					if (Colors(rubiksCopy.CubeArray[f].FaceMatrix[x][y].Square.Color) ==
						self.Cross):
						# check if we could move there in a more efficient manner
						if len(self.Moves) == 3: 
							del self.Moves[:]
							self.Moves.append(directionInv) # go backwards instead
						return
				del self.Moves[:] # If nothing works out, clear the list of moves
				return
		    #### end of RotateCheck()	
			
			f = position[0] # face
			x = position[1] # x position
			y = position[2] # y position
			if x == 0:
				if f == 0:
					RotateCheck(rotate.back, rotate.backInv, f, x, y)
				elif f == 1:
					RotateCheck(rotate.left, rotate.leftInv, f, x, y)
				elif f == 2:
					RotateCheck(rotate.left, rotate.leftInv, f, x, y)
				elif f == 3:
					RotateCheck(rotate.left, rotate.leftInv, f, x, y)
				elif f == 4:
					RotateCheck(rotate.front, rotate.frontInv, f, x, y)
				elif f == 5:
					RotateCheck(rotate.right, rotate.rightInv, f, x, y)
			elif x == 2:
				if f == 0:
					RotateCheck(rotate.front, rotate.frontInv, f, x, y)
				elif f == 1:
					RotateCheck(rotate.right, rotate.rightInv, f, x, y)
				elif f == 2:
					RotateCheck(rotate.right, rotate.rightInv, f, x, y)
				elif f == 3:
					RotateCheck(rotate.right, rotate.rightInv, f, x, y)
				elif f == 4:
					RotateCheck(rotate.back, rotate.backInv, f, x, y)
				elif f == 5:
					RotateCheck(rotate.left, rotate.leftInv, f, x, y)
			elif y == 0:
				if f == 0:
					RotateCheck(rotate.upper, rotate.upperInv, f, x, y)
				elif f == 1:
					RotateCheck(rotate.front, rotate.frontInv, f, x, y)
				elif f == 2:
					RotateCheck(rotate.upper, rotate.upperInv, f, x, y)
				elif f == 3:
					RotateCheck(rotate.back, rotate.backInv, f, x, y)
				elif f == 4:
					RotateCheck(rotate.upper, rotate.upperInv, f, x, y)
				elif f == 5:
					RotateCheck(rotate.upper, rotate.upperInv, f, x, y)
			elif y == 2:
				if f == 0:
					RotateCheck(rotate.down, rotate.downInv, f, x, y)
				elif f == 1:
					RotateCheck(rotate.back, rotate.backInv, f, x, y)
				elif f == 2:
					RotateCheck(rotate.down, rotate.downInv, f, x, y)
				elif f == 3:
					RotateCheck(rotate.front, rotate.frontInv, f, x, y)
				elif f == 4:
					RotateCheck(rotate.down, rotate.downInv, f, x, y)
				elif f == 5:
					RotateCheck(rotate.down, rotate.downInv, f, x, y)
			return
		    #### end of CheckStrip
			
		# If there is something in the moves queue, do that move
		if len(self.Moves) != 0:
			return self.Moves.pop(0)	
		# Otherwise, do logic that puts something in the moves queue		
		else:
			# face: the face where the cross is to be made
			face = faceMapper(faceColors.stringToInt(self.Cross)) 
			badPositions = []
			if self.Rubiks.CubeArray[face].FaceMatrix[0][1].Square.Color != Colors(self.Cross):
				badPositions.append([face,0,1])
			if self.Rubiks.CubeArray[face].FaceMatrix[1][0].Square.Color != Colors(self.Cross):
				badPositions.append([face,1,0])
			if self.Rubiks.CubeArray[face].FaceMatrix[2][1].Square.Color != Colors(self.Cross):
				badPositions.append([face,2,1])
			if self.Rubiks.CubeArray[face].FaceMatrix[1][2].Square.Color != Colors(self.Cross):
				badPositions.append([face,1,2])
			
			for i in range(0,len(badPositions)):
				CheckStrip(badPositions[i])
				if len(self.Moves) != 0:
					return self.Moves.pop(0)
				
			
			
			