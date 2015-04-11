from globals import faceColors
from rotations import rotate

# A class that assumes the face you are looking at is front
# Can perform rotations based while assuming any face is front
class Face:
	def __init__(self, f):
		self.Number = f
		self.Color = faceColors.intToString(f)
		# For upper and down
		if f == 0 or f == 2 or f == 4 or f == 5:
			self.Upper = rotate.upper
			self.UpperInv = rotate.upperInv
			self.Down = rotate.down
			self.DownInv = rotate.downInv
		elif f == 1: 	
			self.Upper = rotate.front
			self.UpperInv = rotate.frontInv
			self.Down = rotate.back
			self.DownInv = rotate.backInv
		elif f == 3:
			self.Upper = rotate.back
			self.UpperInv = rotate.backInv
			self.Down = rotate.front
			self.DownInv = rotate.frontInv
		
		# For left and right
		if f == 1 or f == 2 or f == 3:
			self.Left = rotate.left
			self.LeftInv = rotate.leftInv
			self.Right = rotate.right
			self.RightInv = rotate.rightInv
		elif f == 0:
			self.Left = rotate.back
			self.LeftInv = rotate.backInv
			self.Right = rotate.front
			self.RightInv = rotate.frontInv
		elif f == 4:
			self.Left = rotate.front
			self.LeftInv = rotate.frontInv
			self.Right = rotate.back
			self.RightInv = rotate.backInv
		elif f == 5:
			self.Left = rotate.right
			self.LeftInv = rotate.rightInv
			self.Right = rotate.left
			self.RightInv = rotte.leftInv
		
		# For front and back
		if f == 0:
			self.Front = rotate.left
			self.FrontInv = rotate.leftInv
			self.Back = rotate.right
			self.BackInv = rotate.rightInv
		elif f == 1:
			self.Front = rotate.down
			self.FrontInv = rotate.downInv
			self.Back = rotate.upper
			self.BackInv = rotate.upperInv
		elif f == 2:
			self.Front = rotate.front
			self.FrontInv = rotate.frontInv
			self.Back = rotate.back
			self.BackInv = rotate.backInv
		elif f == 3:
			self.Front = rotate.upper
			self.FrontInv = rotate.upperInv
			self.Back = rotate.down
			self.BackInv = rotate.downInv
		elif f == 4:
			self.Front = rotate.right
			self.FrontInv = rotate.rightInv
			self.Back = rotate.left
			self.BackInv = rotate.leftinv
		elif f == 5:
			self.Front = rotate.back
			self.FrontInv = rotate.backInv
			self.Back = rotate.front
			self.BackInv = rotate.frontInv