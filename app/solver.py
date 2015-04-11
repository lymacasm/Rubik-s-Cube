from rotations import *
from globals import colors, faceColors
from face import Face
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
		
	    #### Checks to see if there is a piece lined up for an easy cross placement
		def CheckStrip(position):	
			
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
		    
		#### Checks the face opposite of cross construction for a matching color
		def CheckTop(faceIndex):
		
			#### Checks adjacent side color for a match
			def CheckSideMiddle(face, x, y):
			
				#### Checks the color of a square with the given faceColor
				def SideColorCheck(color, face, x, y):
					if (faceColors.intToString(color) == Colors(
						self.Rubiks.CubeArray[face].FaceMatrix[x][y].SquareSecn.Color)):
						return True
				#### end of SideColorCheck
				
				if face == 0:
					if x == 1:
						if y == 0:
							return SideColorCheck(3, face, x, y)
						elif y == 2:
							return SideColorCheck(1, face, x, y)
					elif y == 1:
						if x == 0:
							return SideColorCheck(5, face, x, y)
						elif x == 2:
							return SideColorCheck(2, face, x, y)
							
				elif face == 1:
					if x == 1:
						if y == 0:
							return SideColorCheck(2, face, x, y)
						elif y == 2:
							return SideColorCheck(5, face, x, y)
					elif y == 1:
						if x == 0:
							return SideColorCheck(0, face, x, y)
						elif x == 2:
							return SideColorCheck(4, face, x, y)
							
				elif face == 2:
					if x == 1:
						if y == 0:
							return SideColorCheck(3, face, x, y)
						elif y == 2:
							return SideColorCheck(1, face, x, y)
					elif y == 1:
						if x == 0:
							return SideColorCheck(0, face, x, y)
						elif x == 2:
							return SideColorCheck(4, face, x, y)
						
				elif face == 3:
					if x == 1:
						if y == 0:
							return SideColorCheck(5, face, x, y)
						elif y == 2:
							return SideColorCheck(2, face, x, y)
					elif y == 1:
						if x == 0:
							return SideColorCheck(0, face, x, y)
						elif x == 2:
							return SideColorCheck(4, face, x, y)
				
				elif face == 4:
					if x == 1:
						if y == 0:
							return SideColorCheck(3, face, x, y)
						elif y == 2:
							return SideColorCheck(1, face, x, y)
					elif y == 1:
						if x == 0:
							return SideColorCheck(2, face, x, y)
						elif x == 2:
							return SideColorCheck(5, face, x, y)
				
				elif face == 5:
					if x == 1:
						if y == 0:
							return SideColorCheck(3, face, x, y)
						elif y == 2:
							return SideColorCheck(1, face, x, y)
					elif y == 1:
						if x == 0:
							return SideColorCheck(4, face, x, y)
						elif x == 2:
							return SideColorCheck(0, face, x, y)
			#### End of CheckSideMiddle
			
			# Checks the position opposite it to see if that position is free
			# If is the face you're currently sitting at, will check faceMapped f
			# returns the color of the opposite piece
			def OppositePositionColor(rubiks, f, x, y):
				fOp = faceMapper(f) # opposite face
				
				# For faces 1 and 3, their coordinates are mirrored in y
				if f == 1 or f == 3:
					if y == 0:
						xOp = x
						yOp = 2
					elif y == 2:
						xOp = x
						yOp = 0
					else:
						xOp = x
						yOp = y
						
				# For all the other face, their coordinates are mirrored in x
				else: 
					if x == 0:
						xOp = 2
						yOp = y
					elif x == 2:
						xOp = 0
						yOp = y
					else:
						xOp = x
						yOp = y
				
				return rubiks.CubeArray[fOp].FaceMatrix[xOp][yOp].Square.Color
				#### End of OppositePositionColor
							
			f = Face(faceIndex)
			f_Top = Face(faceMapper(faceIndex))
			x0y1 = False
			x1y0 = False
			x1y2 = False
			x2y1 = False
			
			if (Colors(self.Rubiks.CubeArray[f_Top.Number].FaceMatrix[0][1].Square.Color) == 
				self.Cross):
				x0y1 = True
			if (Colors(self.Rubiks.CubeArray[f_Top.Number].FaceMatrix[1][0].Square.Color) ==
				self.Cross):
				x1y0 = True
			if (Colors(self.Rubiks.CubeArray[f_Top.Number].FaceMatrix[1][2].Square.Color) ==
				self.Cross):
				x1y2 = True
			if (Colors(self.Rubiks.CubeArray[f_Top.Number].FaceMatrix[2][1].Square.Color) ==
				self.Cross):
				x2y1 = True
			
			# Spins back piece and checks if top is lined up for move
			def MakeMoves(f_Top, direction, x, y):
				if CheckSideMiddle(f_Top.Number, x, y) == False:
					rubiksCopy = copy.deepcopy(self.Rubiks)
					for i in range(0,3):
						f_Top.Back(rubiksCopy)
						self.Moves.append(f_Top.Back)
						if OpositePositionColor(rubiksCopy, f_Top.Number, x, y) != self.Cross:
							if i != 2:
								self.Moves.append(direction)
								self.Moves.append(direction)
								return
							else:
								del self.Moves
								self.Moves.append(f_Top.BackInv)
								self.Moves.append(direction)
								self.Moves.append(direction)
								return
					del self.Moves
			
			if x0y1:
				MakeMoves(f_Top, f_Top.Left, 0, 1)
				return
			elif x1y0:
				MakeMoves(f_Top, f_Top.Upper, 1, 0)
				return
			elif x1y2:
				MakeMoves(f_Top, f_Top.Down, 1, 0)
				return
			elif x2y1:
				MakeMoves(f_Top, f_Top.Right, 1, 0)
			return
			#### End of CheckTop	
			
		# If there is something in the moves queue, do that move
		if len(self.Moves) != 0:
			self.Count += 1
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
					self.Count += 1
					return self.Moves.pop(0)
			
			CheckTop(face)
			if len(self.Moves) != 0:
				self.Count += 1
				return self.Moves.pop(0)
			
				
			
			
			