class King: #still work needed on check for mate on valid moves

	#Initalisation
	def setup(self, x, y, z, team):
		#Init-Parameters
		self.x = x
		self.y = y
		self.z = z
		self.team = team
		#Init
		self.score = 5
	#~~~~

	#Getters
	def getValidMoveCoords(self, game): ## TODO: Needs to check whether it will be put into a check or mate
		x = self.x
		y = self.y
		z = self.z
		validMoveCoords = []

		for i in range(-1, 2):
			for j in range(-1, 2):
				for a in range(-1, 2):
					if game.boardPoi(x+i, y+j, z+a) != "X" and game.boardPoi(x+i, y+j, z+a) != False:
						if game.boardPoi(x+i, y+j, z+a) == "":
							validMoveCoords.append([x+i, y+j, z+a, "m"])
						elif game.boardPoi(x+i, y+j, z+a).getTeam() != self.getTeam():
							validMoveCoords.append([x+i, y+j, z+a, "t"])
						elif game.boardPoi(x+i, y+j, z+a).getTeam() == self.getTeam():
							validMoveCoords.append([x+i, y+j, z+a, "o"])

	def peice(self):
		return "k"

	def getTeam(self):
		return self.team

	def score(self):
		return self.score
	#~~~~

	#Setters
	def setCoords(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	#~~~~
