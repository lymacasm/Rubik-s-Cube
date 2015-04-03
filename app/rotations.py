#from shapes import cube
import copy

# Rotates a matrix either clockwise or counter clockwise
# Variables:
# 	matrix: A 3x3 matrix
# 	direction: a string either:
#		- "cw" : For clockwise
#		- "ccw" : For counter clockwise
# returns rotated matrix (return original matrix if direction
# 	is in the wrong format)
def rotateMatrix(matrix, direction):
	column1 = copy.deepcopy(matrix[0])
	column3 = copy.deepcopy(matrix[2])
	row1 = []
	row3 = []
	for j in range(0,3):
		row1.append(copy.deepcopy(matrix[j][0]))
		row3.append(copy.deepcopy(matrix[j][2]))
	
	if direction == "cw":
		matrix[0][0] = column1[2]
		matrix[1][0] = column1[1]
		matrix[2][0] = column1[0]
	
		matrix[2][1] = row1[1]
		matrix[2][2] = row1[2]
	
		matrix[1][2] = column3[1]
		matrix[0][2] = column3[2]
	
		matrix[0][1] = row3[1]
		
	elif direction == "ccw":
		matrix[0][0] = column3[0]
		matrix[1][0] = column3[1]
		matrix[2][0] = column3[2]
		
		matrix[2][1] = row3[1]
		matrix[2][2] = row3[0]
		
		matrix[1][2] = column1[1]
		matrix[0][2] = column1[0]
		
		matrix[0][1] = row1[1]
		
	else:
		print "Invalid input for variable, direction"
		print "Input: " + direction
		
	return matrix
	

def rotateL(rubiks):
	
	rubiks.CubeArray[0].FaceMatrix = rotateMatrix(rubiks.CubeArray[0].FaceMatrix, "cw")
	
	
	#Gathering of columns
	face1left = copy.deepcopy(rubiks.CubeArray[1].FaceMatrix[0])
	face2left = copy.deepcopy(rubiks.CubeArray[2].FaceMatrix[0])
	face3left = copy.deepcopy(rubiks.CubeArray[3].FaceMatrix[0])
	face5right = copy.deepcopy(rubiks.CubeArray[5].FaceMatrix[2])
	
	#Moving columns
	rubiks.CubeArray[1].FaceMatrix[0] = face2left
	rubiks.CubeArray[2].FaceMatrix[0] = face3left
	for i in range(0,3):
		rubiks.CubeArray[3].FaceMatrix[0][i] = face5right[2-i]
		rubiks.CubeArray[5].FaceMatrix[2][i] = face1left[2-i]
	
def rotateLi(rubiks):
	
	rubiks.CubeArray[0].FaceMatrix = rotateMatrix(rubiks.CubeArray[0].FaceMatrix, "ccw")
	
	#Gathering of columns
	face1left = copy.deepcopy(rubiks.CubeArray[1].FaceMatrix[0])
	face2left = copy.deepcopy(rubiks.CubeArray[2].FaceMatrix[0])
	face3left = copy.deepcopy(rubiks.CubeArray[3].FaceMatrix[0])
	face5right = copy.deepcopy(rubiks.CubeArray[5].FaceMatrix[2])
	
	#Moving columns
	rubiks.CubeArray[2].FaceMatrix[0] = face1left
	rubiks.CubeArray[3].FaceMatrix[0] = face2left
	for i in  range(0,3):
		rubiks.CubeArray[5].FaceMatrix[2][i] = face3left[2-i]
		rubiks.CubeArray[1].FaceMatrix[0][i] = face5right[2-i]
	
def rotateR(rubiks):
	
	rubiks.CubeArray[4].FaceMatrix = rotateMatrix(rubiks.CubeArray[4].FaceMatrix, "cw")
	
	#Gathering of columns
	face1right = copy.deepcopy(rubiks.CubeArray[1].FaceMatrix[2])
	face2right = copy.deepcopy(rubiks.CubeArray[2].FaceMatrix[2])
	face3right = copy.deepcopy(rubiks.CubeArray[3].FaceMatrix[2])
	face5left = copy.deepcopy(rubiks.CubeArray[5].FaceMatrix[0])
	
	#Moving columns
	rubiks.CubeArray[2].FaceMatrix[2] = face1right
	rubiks.CubeArray[3].FaceMatrix[2] = face2right
	for i in range(0,3):
		rubiks.CubeArray[5].FaceMatrix[0][i] = face3right[2-i]
		rubiks.CubeArray[1].FaceMatrix[2][i] = face5left[2-i]
	
def rotateRi(rubiks):
	
	rubiks.CubeArray[4].FaceMatrix = rotateMatrix(rubiks.CubeArray[4].FaceMatrix, "ccw")
	
	#Gathering of columns
	face1right = copy.deepcopy(rubiks.CubeArray[1].FaceMatrix[2])
	face2right = copy.deepcopy(rubiks.CubeArray[2].FaceMatrix[2])
	face3right = copy.deepcopy(rubiks.CubeArray[3].FaceMatrix[2])
	face5left = copy.deepcopy(rubiks.CubeArray[5].FaceMatrix[0])
	
	#Moving columns
	rubiks.CubeArray[1].FaceMatrix[2] = face2right
	rubiks.CubeArray[2].FaceMatrix[2] = face3right
	for i in range(0,3):
		rubiks.CubeArray[5].FaceMatrix[0][i] = face1right[2-i]
		rubiks.CubeArray[3].FaceMatrix[2][i] = face5left[2-i]
		
	
def rotateU(rubiks):

	rubiks.CubeArray[3].FaceMatrix = rotateMatrix(rubiks.CubeArray[3].FaceMatrix, "cw")
	
	#Gathering of rows
	face0up = []
	face2up = []
	face4up = []
	face5up = []
	for i in range(0,3):
		face0up.append(copy.deepcopy(rubiks.CubeArray[0].FaceMatrix[i][0]))
		face2up.append(copy.deepcopy(rubiks.CubeArray[2].FaceMatrix[i][0]))
		face4up.append(copy.deepcopy(rubiks.CubeArray[4].FaceMatrix[i][0]))
		face5up.append(copy.deepcopy(rubiks.CubeArray[5].FaceMatrix[i][0]))
	
	#Moving rows
	for i in range(0,3):
		rubiks.CubeArray[0].FaceMatrix[i][0] = face2up[i]
		rubiks.CubeArray[2].FaceMatrix[i][0] = face4up[i]
		rubiks.CubeArray[4].FaceMatrix[i][0] = face5up[i]
		rubiks.CubeArray[5].FaceMatrix[i][0] = face0up[i]
		
def rotateUi(rubiks):

	rubiks.CubeArray[3].FaceMatrix = rotateMatrix(rubiks.CubeArray[3].FaceMatrix, "ccw")
	
	#Gathering of rows
	face0up = []
	face2up = []
	face4up = []
	face5up = []
	for i in range(0,3):
		face0up.append(copy.deepcopy(rubiks.CubeArray[0].FaceMatrix[i][0]))
		face2up.append(copy.deepcopy(rubiks.CubeArray[2].FaceMatrix[i][0]))
		face4up.append(copy.deepcopy(rubiks.CubeArray[4].FaceMatrix[i][0]))
		face5up.append(copy.deepcopy(rubiks.CubeArray[5].FaceMatrix[i][0]))
	
	#Moving rows
	for i in range(0,3):
		rubiks.CubeArray[0].FaceMatrix[i][0] = face5up[i]
		rubiks.CubeArray[2].FaceMatrix[i][0] = face0up[i]
		rubiks.CubeArray[4].FaceMatrix[i][0] = face2up[i]
		rubiks.CubeArray[5].FaceMatrix[i][0] = face4up[i]
	
def rotateD(rubiks):
	
	rubiks.CubeArray[1].FaceMatrix = rotateMatrix(rubiks.CubeArray[1].FaceMatrix, "cw")
	
	#Gathering of rows
	face0down = []
	face2down = []
	face4down = []
	face5down = []
	for i in range(0,3):
		face0down.append(copy.deepcopy(rubiks.CubeArray[0].FaceMatrix[i][2]))
		face2down.append(copy.deepcopy(rubiks.CubeArray[2].FaceMatrix[i][2]))
		face4down.append(copy.deepcopy(rubiks.CubeArray[4].FaceMatrix[i][2]))
		face5down.append(copy.deepcopy(rubiks.CubeArray[5].FaceMatrix[i][2]))
	
	#Moving rows
	for i in range(0,3):
		rubiks.CubeArray[0].FaceMatrix[i][2] = face5down[i]
		rubiks.CubeArray[2].FaceMatrix[i][2] = face0down[i]
		rubiks.CubeArray[4].FaceMatrix[i][2] = face2down[i]
		rubiks.CubeArray[5].FaceMatrix[i][2] = face4down[i]
	
def rotateDi(rubiks):

	rubiks.CubeArray[1].FaceMatrix = rotateMatrix(rubiks.CubeArray[1].FaceMatrix, "ccw")
	
	#Gathering of rows
	face0down = []
	face2down = []
	face4down = []
	face5down = []
	for i in range(0,3):
		face0down.append(copy.deepcopy(rubiks.CubeArray[0].FaceMatrix[i][2]))
		face2down.append(copy.deepcopy(rubiks.CubeArray[2].FaceMatrix[i][2]))
		face4down.append(copy.deepcopy(rubiks.CubeArray[4].FaceMatrix[i][2]))
		face5down.append(copy.deepcopy(rubiks.CubeArray[5].FaceMatrix[i][2]))
	
	#Moving rows
	for i in range(0,3):
		rubiks.CubeArray[0].FaceMatrix[i][2] = face2down[i]
		rubiks.CubeArray[2].FaceMatrix[i][2] = face4down[i]
		rubiks.CubeArray[4].FaceMatrix[i][2] = face5down[i]
		rubiks.CubeArray[5].FaceMatrix[i][2] = face0down[i]
	
def rotateF(rubiks):

	rubiks.CubeArray[2].FaceMatrix = rotateMatrix(rubiks.CubeArray[2].FaceMatrix, "cw")
	
	#Gathering of rows
	face0right = []
	face1up = []
	face3down = []
	face4left = []
	for i in range(0,3):
		face0right.append(copy.deepcopy(rubiks.CubeArray[0].FaceMatrix[2][2-i]))
		face1up.append(copy.deepcopy(rubiks.CubeArray[1].FaceMatrix[i][0]))
		face3down.append(copy.deepcopy(rubiks.CubeArray[3].FaceMatrix[i][2]))
		face4left.append(copy.deepcopy(rubiks.CubeArray[4].FaceMatrix[0][2-i]))
	
	#Moving rows/columns
	for i in range(0,3):
		rubiks.CubeArray[0].FaceMatrix[2][i] = face1up[i]
		rubiks.CubeArray[1].FaceMatrix[i][0] = face4left[i]
		rubiks.CubeArray[3].FaceMatrix[i][2] = face0right[i]
		rubiks.CubeArray[4].FaceMatrix[0][i] = face3down[i]
		
def rotateFi(rubiks):

	rubiks.CubeArray[2].FaceMatrix = rotateMatrix(rubiks.CubeArray[2].FaceMatrix, "ccw")
	
	#Gathering of rows and columns
	face0right = []
	face1up = []
	face3down = []
	face4left = []
	for i in range(0,3):
		face0right.append(copy.deepcopy(rubiks.CubeArray[0].FaceMatrix[2][i]))
		face1up.append(copy.deepcopy(rubiks.CubeArray[1].FaceMatrix[2-i][0]))
		face3down.append(copy.deepcopy(rubiks.CubeArray[3].FaceMatrix[2-i][2]))
		face4left.append(copy.deepcopy(rubiks.CubeArray[4].FaceMatrix[0][i]))
	
	#Moving rows/columns
	for i in range(0,3):
		rubiks.CubeArray[0].FaceMatrix[2][i] = face3down[i]
		rubiks.CubeArray[1].FaceMatrix[i][0] = face0right[i]
		rubiks.CubeArray[3].FaceMatrix[i][2] = face4left[i]
		rubiks.CubeArray[4].FaceMatrix[0][i] = face1up[i]
		
def rotateB(rubiks):

	rubiks.CubeArray[5].FaceMatrix = rotateMatrix(rubiks.CubeArray[5].FaceMatrix, "cw")
	
	#Gathering of rows and columns
	face0left = []
	face1down = []
	face3up = []
	face4right = []
	for i in range(0,3):
		face0left.append(copy.deepcopy(rubiks.CubeArray[0].FaceMatrix[0][i]))
		face1down.append(copy.deepcopy(rubiks.CubeArray[1].FaceMatrix[2-i][2]))
		face3up.append(copy.deepcopy(rubiks.CubeArray[3].FaceMatrix[2-i][0]))
		face4right.append(copy.deepcopy(rubiks.CubeArray[4].FaceMatrix[2][i]))
		
	#Moving rows/columns
	for i in range(0,3):
		rubiks.CubeArray[0].FaceMatrix[0][i] = face3up[i]
		rubiks.CubeArray[1].FaceMatrix[i][2] = face0left[i]
		rubiks.CubeArray[3].FaceMatrix[i][0] = face4right[i]
		rubiks.CubeArray[4].FaceMatrix[2][i] = face1down[i]
		
def rotateBi(rubiks):

	rubiks.CubeArray[5].FaceMatrix = rotateMatrix(rubiks.CubeArray[5].FaceMatrix, "ccw")
	
	#Gathering of rows and columns
	face0left = []
	face1down = []
	face3up = []
	face4right = []
	for i in range(0,3):
		face0left.append(copy.deepcopy(rubiks.CubeArray[0].FaceMatrix[0][2-i]))
		face1down.append(copy.deepcopy(rubiks.CubeArray[1].FaceMatrix[i][2]))
		face3up.append(copy.deepcopy(rubiks.CubeArray[3].FaceMatrix[i][0]))
		face4right.append(copy.deepcopy(rubiks.CubeArray[4].FaceMatrix[2][2-i]))
	
	#Moving rows/columns
	for i in range(0,3):
		rubiks.CubeArray[0].FaceMatrix[0][i] = face1down[i]
		rubiks.CubeArray[1].FaceMatrix[i][2] = face4right[i]
		rubiks.CubeArray[3].FaceMatrix[i][0] = face0left[i]
		rubiks.CubeArray[4].FaceMatrix[2][i] = face3up[i]
		
	
	
		
