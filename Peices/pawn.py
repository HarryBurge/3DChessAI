class Pawn:

	#Initalisation
	def setup(self, x, y, z, directionX, directionY, team):
		#Init-Parameters
		self.x = x
		self.y = y
		self.z = z
		self.directionX = directionX
		self.directionY = directionY
		self.team = team
		#Init
		self.moved = False
		self.score = 1
	#~~~~

	#Getters
	def getValidMoveCoords(self, game): ## TODO: Remake
		x = self.x
		y = self.y
		z = self.z
		validMoveCoords = []
		x0y0z1 = game.boardPoi(x, y, z+1)
		x0y0z2 = game.boardPoi(x, y, z+2)
		x0y0z_1 = game.boardPoi(x, y, z-1)
		x0y0z_2 = game.boardPoi(x, y, z-2)
		for i in range(-1, 2):
			xdy1zi = game.boardPoi(x+self.directionX, y+1, z+i)
			xdy_zi = game.boardPoi(x+self.directionX, y-1, z+i)
			x1ydzi = game.boardPoi(x+1, y+self.directionY, z+i)
			x_ydzi = game.boardPoi(x-1, y+self.directionY, z+i)
			xdydzi = game.boardPoi(x+self.directionX, y+self.directionY, z+i)
			xd2yd2zi = game.boardPoi(x+(self.directionX*2), y+(self.directionY*2), z+i)

			if xdydzi == "": #Forward movements
				validMoveCoords.append([x+self.directionX, y+self.directionY, z+i, "m"])
				if self.moved == False and xd2yd2zi == "": #Forward 1st move
					validMoveCoords.append([x+(self.directionX*2), y+(self.directionY*2), z+i, "m"])

			if self.directionX != 0: #Moves in X
				#+1y
				if xdy1zi != "" and xdy1zi != "X" and xdy1zi != False:
					if xdy1zi.getTeam() != self.getTeam():
						validMoveCoords.append([x+self.directionX, y+1, z+i, "t"])
					elif xdy1zi.getTeam() == self.getTeam():
						validMoveCoords.append([x+self.directionX, y+1, z+i, "o"])
				#-1y
				if xdy_zi != "" and xdy_zi != "X" and xdy_zi != False:
					if xdy_zi.getTeam() != self.getTeam():
						validMoveCoords.append([x+self.directionX, y-1, z+i, "t"])
					elif xdy_zi.getTeam() == self.getTeam():
						validMoveCoords.append([x+self.directionX, y-1, z+i, "o"])
			else: #Moves in Y
				#+1x
				if x1ydzi != "" and x1ydzi != "X" and x1ydzi != False:
					if x1ydzi.getTeam() != self.getTeam():
						validMoveCoords.append([x+1, y+self.directionY, z+i, "t"])
					elif x1ydzi.getTeam() == self.getTeam():
						validMoveCoords.append([x+1, y+self.directionY, z+i, "o"])
				#-1x
				if x_ydzi != "" and x_ydzi != "X" and x_ydzi != False:
					if x_ydzi.getTeam() != self.getTeam():
						validMoveCoords.append([x-1, y+self.directionY, z+i, "t"])
					elif x_ydzi.getTeam() == self.getTeam():
						validMoveCoords.append([x-1, y+self.directionY, z+i, "o"])
		if x0y0z_1 == "": #Forward movements
				validMoveCoords.append([x, y, z-1, "m"])
				if self.moved == False and x0y0z_2 == "": #Forward 1st move
					validMoveCoords.append([x, y, z-2, "m"])
		if x0y0z1 == "": #Forward movements
				validMoveCoords.append([x, y, z+1, "m"])
				if self.moved == False and x0y0z2 == "": #Forward 1st move
					validMoveCoords.append([x, y, z+2, "m"])
		return validMoveCoords

	def getTeam(self): #Returns team
		return self.team

	def peice(self): #Returns peice id
		return "p"

	def score(self): #Returns its value
		return self.score
	#~~~~

	#Setters
	def setMoved(self): #Saves that it has moved
		self.moved = True

	def setCoords(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	#~~~~
