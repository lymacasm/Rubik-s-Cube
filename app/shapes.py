from globals import colors, faceColors
from matcher import magicBox
from rotations import rotateMatrix

Colors = colors()
ColorCode = faceColors()

# ----------------------------------------
# Basic square
# ----------------------------------------
class square:
	def __init__(self):
		self.Color = "#000000"
	
	def initialize(self, color):
		self.Color = color

# ----------------------------------------
# Middle piece of a face
# ----------------------------------------
class middle:
	def __init__(self):
		self.Square = square()
		
	def initialize(self, color, location):
		self.Square.initialize(color)

# ----------------------------------------		
# Points of the crosses, cube contains two squares	
# ----------------------------------------	
class side:
	def __init__(self):
		self.Square = square()
		self.SquareSecn = square()
		
	def initialize(self, color, location):
		self.Square.initialize(color)
		secnColor = magicBox(color, location)
		if secnColor != None:
			self.SquareSecn.initialize(secnColor)
			
			

# ----------------------------------------	
# Corners of face, cube contains three squares
# ----------------------------------------
class corner:
	def __init__(self):
		self.Square = square()
		self.SquareVert = square()
		self.SquareHori = square()
		
	def initialize(self, color, location):
		self.Square.initialize(color)
		vertHoriObject = magicBox(color, location)
		if vertHoriObject != None:
			self.SquareVert.initialize(vertHoriObject["vert"])
			self.SquareHori.initialize(vertHoriObject["hori"])

# ----------------------------------------	
# A face, contains the following:
#	- 1 middle
#	- 4 corners
#	- 4 sides
# ----------------------------------------			
class face:
	def __init__(self):
		column1 = []
		column1.append(corner())
		column1.append(side())
		column1.append(corner())
		
		column2 = []
		column2.append(side())
		column2.append(middle())
		column2.append(side())
		
		column3 = []
		column3.append(corner())
		column3.append(side())
		column3.append(corner())
		
		self.FaceMatrix = []
		self.FaceMatrix.append(column1)
		self.FaceMatrix.append(column2)
		self.FaceMatrix.append(column3)
		
		self.FaceNumber = -1
	
	def initialize(self, color, face):
		self.FaceNumber = face
		for i in range(0,3):
			for j in range(0,3):
				self.FaceMatrix[i][j].initialize(color, [face, i, j])
		#if face == 1:
			#rotateMatrix(FaceMatrix)		
		

# ----------------------------------------	
# Cube containing 6 faces
# ----------------------------------------		
class cube:
	def __init__(self):
		self.CubeArray = []
		for x in range(0,6):
			self.CubeArray.append(face())
		
	def initialize(self):
		for code in range(0,6):
			if code == ColorCode.red:
				self.CubeArray[code].initialize(Colors.red, code)
			elif code == ColorCode.blue:
				self.CubeArray[code].initialize(Colors.blue, code)
			elif code == ColorCode.white:
				self.CubeArray[code].initialize(Colors.white, code)
			elif code == ColorCode.green:
				self.CubeArray[code].initialize(Colors.green, code)
			elif code == ColorCode.orange:
				self.CubeArray[code].initialize(Colors.orange, code)
			elif code == ColorCode.yellow:
				self.CubeArray[code].initialize(Colors.yellow, code)
			else:
				self.CubeArray[code].initialize(Colors.borderColor, code)
				