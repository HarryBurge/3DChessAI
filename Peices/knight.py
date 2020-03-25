class Knight:

	#Initalisation
	def setup(self, x, y, z, team):
		#Init-Parameters
		self.x = x
		self.y = y
		self.z = z
		self.team = team
		#Init
		self.score = 3
	#~~~~

	#Getters
	def getValidMoveCoords(self, game):
		x = self.x
		y = self.y
		z = self.z
		validMoveCoords = []

		for i in range(-2, 3):
			for j in range(-2, 3):
				for k in range(-2, 3):
					if abs(i) + abs(j) + abs(k) == 3 and not (abs(i)==1 and abs(j)==1 and abs(k)==1):
						if game.boardPoi(x+i, y+j, z+k) == "":
							validMoveCoords.append([x+i, y+j, z+k, "m"])
						elif game.boardPoi(x+i, y+j, z+k) != "X" and game.boardPoi(x+i, y+j, z+k) != False:
							if game.boardPoi(x+i, y+j, z+k).getTeam() != self.getTeam():
								validMoveCoords.append([x+i, y+j, z+k, "t"])
							elif game.boardPoi(x+i, y+j, z+k).getTeam() == self.getTeam():
								validMoveCoords.append([x+i, y+j, z+k, "o"])
		return validMoveCoords

	def peice(self):
		return "h"

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
