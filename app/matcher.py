from globals import colors, faceColors

Colors = colors()
ColorCode = faceColors()

def magicBox(color, location):
	if location[1] == 0 and location[2] == 0:
		if location[0] == 0:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(5)) }
		
		elif location[0] == 1:
			return { "vert":Colors(ColorCode(2)), 
					 "hori":Colors(ColorCode(0)) }
		
		elif location[0] == 2:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(0)) }
		
		elif location[0] == 3:
			return { "vert":Colors(ColorCode(5)), 
					 "hori":Colors(ColorCode(0)) }
			
		elif location[0] == 4:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(2)) }
			
		elif location[0] == 5:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(4)) }
		
		else:
			return None
			
	elif location[1] == 1 and location[2] == 0:
		if location[0] == 0:
			return Colors(ColorCode(3))
			
		elif location[0] == 1:
			return Colors(ColorCode(2))
		
		elif location[0] == 2:
			return Colors(ColorCode(3))
		
		elif location[0] == 3:
			return Colors(ColorCode(5))
			
		elif location[0] == 4:
			return Colors(ColorCode(3))
		
		elif location[0] == 5:
			return Colors(ColorCode(3))
		
		else:
			return None
			
	elif location[1] == 2 and location[2] == 0:
		if location[0] == 0:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(2)) }
		
		elif location[0] == 1:
			return { "vert":Colors(ColorCode(2)), 
				"hori":Colors(ColorCode(4)) }
		
		elif location[0] == 2:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(4)) }
		
		elif location[0] == 3:
			return { "vert":Colors(ColorCode(5)), 
					 "hori":Colors(ColorCode(4)) }
			
		elif location[0] == 4:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(5)) }
			
		elif location[0] == 5:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(0)) }
		
		else: 
			return None	
	
	elif location[1] == 0 and location[2] == 1:
		if location[0] == 0:
			return Colors(ColorCode(5))
		
		elif location[0] == 1:
			return Colors(ColorCode(0))
			
		elif location[0] == 2:
			return Colors(ColorCode(0))
			
		elif location[0] == 3:
			return Colors(ColorCode(0))
			
		elif location[0] == 4:
			return Colors(ColorCode(2))
			
		elif location[0] == 5:
			return Colors(ColorCode(4))
			
		else:	
			return None
			
	elif location[1] == 2 and location[2] == 1:
		if location[0] == 0:
			return Colors(ColorCode(2))
		
		elif location[0] == 1:
			return Colors(ColorCode(4))
			
		elif location[0] == 2:
			return Colors(ColorCode(4))
			
		elif location[0] == 3:
			return Colors(ColorCode(4))
			
		elif location[0] == 4:
			return Colors(ColorCode(5))
			
		elif location[0] == 5:
			return Colors(ColorCode(0))
			
		else:
			return None
			
	elif location[1] == 0 and location[2] == 2:
		if location[0] == 0:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(5)) }
			
		elif location[0] == 1:
			return { "vert":Colors(ColorCode(5)), 
					 "hori":Colors(ColorCode(0)) }
			
		elif location[0] == 2:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(0)) }
			
		elif location[0] == 3:
			return { "vert":Colors(ColorCode(2)), 
					 "hori":Colors(ColorCode(0)) }
			
		elif location[0] == 4:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(2)) }
			
		elif location[0] == 5:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(4)) }
			
		else:
			return None
			
	elif location[1] == 1 and location[2] == 2:
		if location[0] == 0:
			return Colors(ColorCode(1))
			
		elif location[0] == 1:
			return Colors(ColorCode(5))
			
		elif location[0] == 2:
			return Colors(ColorCode(1))
			
		elif location[0] == 3:
			return Colors(ColorCode(2))
			
		elif location[0] == 4:
			return Colors(ColorCode(1))
			
		elif location[0] == 5:
			return Colors(ColorCode(1))
			
		else:	
			return None
			
	elif location[1] == 2 and location[2] == 2:
		if location[0] == 0:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(2)) }
		
		elif location[0] == 1:
			return { "vert":Colors(ColorCode(5)), 
					 "hori":Colors(ColorCode(4)) }
			
		elif location[0] == 2:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(4)) }
			
		elif location[0] == 3:
			return { "vert":Colors(ColorCode(2)), 
					 "hori":Colors(ColorCode(4)) }
		
		elif location[0] == 4:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(5)) }
			
		elif location[0] == 5:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(0)) }
		
		else:
			return None
	
			
		
				
			
	