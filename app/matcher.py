from globals import colors, faceColors

Colors = colors()
ColorCode = faceColors()

def magicBox(color, location):
	if location[1] == 0 and location[2] == 0:
		if location[0] == 0:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(5)),
					 "connects" : [{"face":3, "cords":[0,0]}, {"face":5, "cords":[2,0]}] }
		
		elif location[0] == 1:
			return { "vert":Colors(ColorCode(2)), 
					 "hori":Colors(ColorCode(0)),
					 "connects" : [{"face":2, "cords":[0,2]}, {"face":0, "cords":[2,2]}] }
		
		elif location[0] == 2:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(0)),
					 "connects" : [{"face":0, "cords":[2,0]}, {"face":3, "cords":[0,2]}] }
		
		elif location[0] == 3:
			return { "vert":Colors(ColorCode(5)), 
					 "hori":Colors(ColorCode(0)),
					 "connects" : [{"face":0, "cords":[0,0]}, {"face":5, "cords":[2,0]}] }
			
		elif location[0] == 4:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(2)),
					 "connects" : [{"face":2, "cords":[2,0]}, {"face":3, "cords":[2,2]}] }
			
		elif location[0] == 5:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(4)),
					 "connects" : [{"face":4, "cords":[2,0]}, {"face":3, "cords":[2,0]}] }
		
		else:
			return None
			
	elif location[1] == 1 and location[2] == 0:
		if location[0] == 0:
			return {"Color": Colors(ColorCode(3)),
					"connects" : [{"face" : 3, "cords" : [0,1]}]}
			
		elif location[0] == 1:
			return {"Color" : Colors(ColorCode(2)), 
					"connects" : [{"face" : 2, "cords" : [1,2]}]}
		
		elif location[0] == 2:
			return {"Color": Colors(ColorCode(3)),
					"connects" : [{"face" : 3, "cords" : [1,2]}]}
		
		elif location[0] == 3:
			return {"Color": Colors(ColorCode(5)),
					"connects": [{"face":5, "cords" : [1,0]}]}
			
		elif location[0] == 4:
			return {"Color":Colors(ColorCode(3)),
					"connects":[{"face":3, "cords": [2,1]}]}
		
		elif location[0] == 5:
			return {"Color":Colors(ColorCode(3)),
					"connects":[{"face":3, "cords": [1,0]}]}
		
		else:
			return None
			
	elif location[1] == 2 and location[2] == 0:
		if location[0] == 0:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(2)),
					 "connects" : [{"face":2, "cords":[0,0]}, {"face":3, "cords":[0,2]}] }
		
		elif location[0] == 1:
			return { "vert":Colors(ColorCode(2)), 
					 "hori":Colors(ColorCode(4)),
					 "connects" : [{"face":2, "cords":[2,2]}, {"face":4, "cords":[0,2]}] }
		
		elif location[0] == 2:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(4)),
					 "connects" : [{"face":3, "cords":[2,2]}, {"face":4, "cords":[0,0]}] }
		
		elif location[0] == 3:
			return { "vert":Colors(ColorCode(5)), 
					 "hori":Colors(ColorCode(4)),
					 "connects" : [{"face":4, "cords":[2,0]}, {"face":5, "cords":[0,0]}] }
			
		elif location[0] == 4:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(5)),
					 "connects" : [{"face":3, "cords":[2,0]}, {"face":5, "cords":[0,0]}] }
			
		elif location[0] == 5:
			return { "vert":Colors(ColorCode(3)), 
					 "hori":Colors(ColorCode(0)),
					 "connects" : [{"face":3, "cords":[0,0]}, {"face":0, "cords":[0,0]}] }
		else: 
			return None	
	
	elif location[1] == 0 and location[2] == 1:
		if location[0] == 0:
			return {"Color":Colors(ColorCode(5)),
					"connects":[{"face":5, "cords":[2,1]}]}
		
		elif location[0] == 1:
			return {"Color":Colors(ColorCode(0)),
					"connects":[{"face":0,"cords":[1,2]}]}
			
		elif location[0] == 2:
			return {"Color":Colors(ColorCode(0)),
					"connects":[{"face":0, "cords":[2,1]}]}
			
		elif location[0] == 3:
			return {"Color":Colors(ColorCode(0)),
					"connects":[{"face":0,"cords":[1,0]}]}
			
		elif location[0] == 4:
			return {"Color":Colors(ColorCode(2)),
					"connects":[{"face":2, "cords":[2,1]}]}
			
		elif location[0] == 5:
			return {"Color":Colors(ColorCode(4)),
					"connects":[{"face":4, "cords":[2,1]}]}
			
		else:	
			return None
			
	elif location[1] == 2 and location[2] == 1:
		if location[0] == 0:
			return {"Color":Colors(ColorCode(2)),
					"connects":[{"face":2, "cords":[0,1]}]}
		
		elif location[0] == 1:
			return {"Color":Colors(ColorCode(4)),
					"connects":[{"face":4, "cords":[1,2]}]}
			
		elif location[0] == 2:
			return {"Color":Colors(ColorCode(4)),
					"connects":[{"face":4,"cords":[0,1]}]}
			
		elif location[0] == 3:
			return {"Color":Colors(ColorCode(4)),
					"connects":[{"face":4,"cords":[1,0]}]}
			
		elif location[0] == 4:
			return {"Color":Colors(ColorCode(5)),
					"connects":[{"face":5,"cords":[0,1]}]}
			
		elif location[0] == 5:
			return {"Color":Colors(ColorCode(0)),
					"connects":[{"face":0, "cords":[0,1]}]}
			
		else:
			return None
			
	elif location[1] == 0 and location[2] == 2:
		if location[0] == 0:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(5)),
					 "connects":[{"face":5,"cords":[2,2]},{"face":1,"cords":[0,2]}] }
			
		elif location[0] == 1:
			return { "vert":Colors(ColorCode(5)), 
					 "hori":Colors(ColorCode(0)),
					 "connects":[{"face":5,"cords":[2,2]},{"face":0,"cords":[0,2]}] }
			
		elif location[0] == 2:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(0)),
					 "connects":[{"face":1, "cords":[0,0]},{"face":0,"cords":[2,2]}] }
			
		elif location[0] == 3:
			return { "vert":Colors(ColorCode(2)), 
					 "hori":Colors(ColorCode(0)),
					 "connects":[{"face":2,"cords":[0,0]},{"face":0,"cords":[2,0]}] }
			
		elif location[0] == 4:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(2)),
					 "connects":[{"face":1,"cords":[2,0]},{"face":2,"cords":[2,2]}] }
			
		elif location[0] == 5:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(4)),
					 "connects":[{"face":1,"cords":[2,2]},{"face":4,"cords":[2,2]}] }
			
		else:
			return None
			
	elif location[1] == 1 and location[2] == 2:
		if location[0] == 0:
			return {"Color":Colors(ColorCode(1)),
					"connects":[{"face":1,"cords":[0,1]}]}
			
		elif location[0] == 1:
			return {"Color":Colors(ColorCode(5)),
					"connects":[{"face":5,"cords":[1,2]}]}
			
		elif location[0] == 2:
			return {"Color":Colors(ColorCode(1)),
					"connects":[{"face":1,"cords":[1,0]}]}
			
		elif location[0] == 3:
			return {"Color":Colors(ColorCode(2)),
					"connects":[{"face":2,"cords":[1,0]}]}
			
		elif location[0] == 4:
			return {"Color":Colors(ColorCode(1)),
					"connects":[{"face":1,"cords":[2,1]}]}
			
		elif location[0] == 5:
			return {"Color":Colors(ColorCode(1)),
					"connects":[{"face":1,"cords":[1,2]}]}
			
		else:	
			return None
			
	elif location[1] == 2 and location[2] == 2:
		if location[0] == 0:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(2)),
					 "connects":[{"face":1,"cords":[0,0]},{"face":2,"cords":[0,2]}] }
		
		elif location[0] == 1:
			return { "vert":Colors(ColorCode(5)), 
					 "hori":Colors(ColorCode(4)),
					 "connects":[{"face":5,"cords":[0,2]},{"face":4,"cords":[2,2]}] }
			
		elif location[0] == 2:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(4)),
					 "connects":[{"face":1,"cords":[2,0]},{"face":4,"cords":[0,2]}] }
			
		elif location[0] == 3:
			return { "vert":Colors(ColorCode(2)), 
					 "hori":Colors(ColorCode(4)),
					 "connects":[{"face":2,"cords":[2,0]},{"face":4,"cords":[0,0]}] }
		
		elif location[0] == 4:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(5)),
					 "connects":[{"face":1,"cords":[2,2]},{"face":5,"cords":[0,2]}] }
			
		elif location[0] == 5:
			return { "vert":Colors(ColorCode(1)), 
					 "hori":Colors(ColorCode(0)),
					 "connects":[{"face":1,"cords":[0,2]},{"face":0,"cords":[0,2]}] }
		
		else:
			return None
	
			
		
				
			
	