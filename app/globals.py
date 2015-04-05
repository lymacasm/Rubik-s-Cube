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
		
