class colors:
	def __init__(self):
		self.red = "#CC0000"
		self.blue = "#1E40BE"
		self.white = "#FFFFFF"
		self.green = "#23B41D"
		self.orange = "#FF901C"
		self.yellow = "#FDF044"
		self.borderColor = "#000000"
		
	def __call__(self, color):
		if color == "red":
			return self.red
		elif color == "blue":
			return self.blue
		elif color == "white":
			return self.white
		elif color == "green":
			return self.green
		elif color == "orange":
			return self.orange
		elif color == "yellow":
			return self.yellow
		elif color == self.red:
			return "red"
		elif color == self.blue:
			return "blue"
		elif color == self.white:
			return "white"
		elif color == self.green:
			return "green"
		elif color == self.orange:
			return "orange"
		elif color == self.yellow:
			return "yellow"

class faceColors:
	red = 5;
	blue = 4;
	white = 1;
	green = 0;
	orange = 2;
	yellow = 3;
		

	def __call__(self, face):
		if face == self.red:
			return "red"
		elif face == self.blue:
			return "blue"
		elif face == self.white:
			return "white"
		elif face == self.green:
			return "green"
		elif face == self.orange:
			return "orange"
		elif face == self.yellow:
			return "yellow"
		else:
			return "none"

	@staticmethod
	def intToString(num):
		if num == faceColors.red:
			return "red"
		elif num == faceColors.blue:
			return "blue"
		elif num == faceColors.white:
			return "white"
		elif num == faceColors.green:
			return "green"
		elif num == faceColors.orange:
			return "orange"
		elif num == faceColors.yellow:
			return "yellow"
		else:
			return "none"
			
	@staticmethod
	def stringToInt(string):	
		if string == "red":
			return faceColors.red
		elif string == "blue":
			return faceColors.blue
		elif string == "white":
			return faceColors.white
		elif string == "green":
			return faceColors.green
		elif string == "orange":
			return faceColors.orange
		elif string == "yellow":
			return faceColors.yellow
		else:	
			return -1

			
		
class dimensions:
	def __init__(self):
		self.width = 25
		self.height = 25
		self.origin = [25, 240]
		self.gap = 4
		
def connectingPiecesLoc(face, x, y):
	if x == 0 and y == 0:
		if face == 0:
			return [{"face":3, "cords":[0,0]}, {"face":5, "cords":[2,0]}] 
		
		elif face == 1:
			return [{"face":2, "cords":[0,2]}, {"face":0, "cords":[2,2]}] 
		
		elif face == 2:
			return [{"face":0, "cords":[2,0]}, {"face":3, "cords":[0,2]}] 
		
		elif face == 3:
			return [{"face":0, "cords":[0,0]}, {"face":5, "cords":[2,0]}] 
			
		elif face == 4:
			return [{"face":2, "cords":[2,0]}, {"face":3, "cords":[2,2]}]
			
		elif face == 5:
			return [{"face":4, "cords":[2,0]}, {"face":3, "cords":[2,0]}]
		
		else:
			return None
			
	elif x == 1 and y == 0:
		if face == 0:
			return [{"face" : 3, "cords" : [0,1]}]
			
		elif face == 1:
			return [{"face" : 2, "cords" : [1,2]}]
		
		elif face == 2:
			return [{"face" : 3, "cords" : [1,2]}]
		
		elif face == 3:
			return [{"face":5, "cords" : [1,0]}]
			
		elif face == 4:
			return [{"face":3, "cords": [2,1]}]
		
		elif face == 5:
			return [{"face":3, "cords": [1,0]}]
		
		else:
			return None
			
	elif x == 2 and y == 0:
		if face == 0:
			return [{"face":2, "cords":[0,0]}, {"face":3, "cords":[0,2]}]
		
		elif face == 1:
			return [{"face":2, "cords":[2,2]}, {"face":4, "cords":[0,2]}]
		
		elif face == 2:
			return [{"face":3, "cords":[2,2]}, {"face":4, "cords":[0,0]}]
		
		elif face == 3:
			return [{"face":4, "cords":[2,0]}, {"face":5, "cords":[0,0]}]
			
		elif face == 4:
			return [{"face":3, "cords":[2,0]}, {"face":5, "cords":[0,0]}]
			
		elif face == 5:
			return [{"face":3, "cords":[0,0]}, {"face":0, "cords":[0,0]}]
		else: 
			return None	
	
	elif x == 0 and y == 1:
		if face == 0:
			return [{"face":5, "cords":[2,1]}]
		
		elif face == 1:
			return [{"face":0,"cords":[1,2]}]
			
		elif face == 2:
			return [{"face":0, "cords":[2,1]}]
			
		elif face == 3:
			return [{"face":0,"cords":[1,0]}]
			
		elif face == 4:
			return [{"face":2, "cords":[2,1]}]
			
		elif face == 5:
			return [{"face":4, "cords":[2,1]}]
			
		else:	
			return None
			
	elif x == 2 and y == 1:
		if face == 0:
			return [{"face":2, "cords":[0,1]}]
		
		elif face == 1:
			return [{"face":4, "cords":[1,2]}]
			
		elif face == 2:
			return [{"face":4,"cords":[0,1]}]
			
		elif face == 3:
			return [{"face":4,"cords":[1,0]}]
			
		elif face == 4:
			return [{"face":5,"cords":[0,1]}]
			
		elif face == 5:
			return [{"face":0, "cords":[0,1]}]
			
		else:
			return None
			
	elif x == 0 and y == 2:
		if face == 0:
			return [{"face":5,"cords":[2,2]},{"face":1,"cords":[0,2]}]
			
		elif face == 1:
			return [{"face":5,"cords":[2,2]},{"face":0,"cords":[0,2]}]
			
		elif face == 2:
			return [{"face":1, "cords":[0,0]},{"face":0,"cords":[2,2]}]
			
		elif face == 3:
			return [{"face":2,"cords":[0,0]},{"face":0,"cords":[2,0]}]
			
		elif face == 4:
			return [{"face":1,"cords":[2,0]},{"face":2,"cords":[2,2]}]
			
		elif face == 5:
			return [{"face":1,"cords":[2,2]},{"face":4,"cords":[2,2]}]
			
		else:
			return None
			
	elif x == 1 and y == 2:
		if face == 0:
			return [{"face":1,"cords":[0,1]}]
			
		elif face == 1:
			return [{"face":5,"cords":[1,2]}]
			
		elif face == 2:
			return [{"face":1,"cords":[1,0]}]
			
		elif face == 3:
			return [{"face":2,"cords":[1,0]}]
			
		elif face == 4:
			return [{"face":1,"cords":[2,1]}]
			
		elif face == 5:
			return [{"face":1,"cords":[1,2]}]
			
		else:	
			return None
			
	elif x == 2 and y == 2:
		if face == 0:
			return [{"face":1,"cords":[0,0]},{"face":2,"cords":[0,2]}]
		
		elif face == 1:
			return [{"face":5,"cords":[0,2]},{"face":4,"cords":[2,2]}]
			
		elif face == 2:
			return [{"face":1,"cords":[2,0]},{"face":4,"cords":[0,2]}]
			
		elif face == 3:
			return [{"face":2,"cords":[2,0]},{"face":4,"cords":[0,0]}]
		
		elif face == 4:
			return [{"face":1,"cords":[2,2]},{"face":5,"cords":[0,2]}]
			
		elif face == 5:
			return [{"face":1,"cords":[0,2]},{"face":0,"cords":[0,2]}]
		
		else:
			return None