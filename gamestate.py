#Game structure~~~~~~~

class gamestate:

	#Initilisation
	def setup(self, boardint, players):
		self.board = boardint
		self.players = players
		self.playerturn = 0

		self.playersTakenPeices = []
		for i in range(0, len(self.players)):
			self.playersTakenPeices.append([])
	#~~~~

	#Getters
	def getBoard(self): #Returns board array
		return self.board

	def getTurn(self): #Returns the players number that turn it is
		return self.playerturn

	def getPlayers(self): #Returns the list of players
		return self.players

	def boardPoi(self, x, y, z): #Returns the object that is in a certain coord - False if coords out of bounds
		if x < len(self.board) and y < len(self.board[0]) and y >= 0 and x >=0 and z >= 0:
			if type(self.board[x][y]) == list:
				if len(self.board[x][y]) > z:
					return self.board[x][y][len(self.board[x][y]) - 1 - z]
			else:
				if z == 0:
					return self.board[x][y]
		return False
	#~~~~

	#Setters
	def setBoard(self, newboard): #Rewrites board to a new board
		self.board = newboard

	def setPoi(self, x, y, z, peice): #Writes a peice to a coord - False if coord out of bounds
		if x < len(self.board) and y < len(self.board[0]) and y >= 0 and x >=0:
			if type(self.board[x][y]) == list:
				if len(self.board[x][y]) > z:
					self.board[x][y][len(self.board[x][y]) - 1 - z] = peice
					return True
			else:
				if z == 0:
					self.board[x][y] = peice
					return True
		return False
	#~~~~

	#Funcs
	def nextTurn(self): #Changes turns to next player
		self.playerturn += 1
		if self.playerturn >= len(self.players):
			self.playerturn = 0

	def checkSetPoi(self, x, y, z): #Checks whether move will be legal or illegal in terms of coords
		if type(self.board[x][y]) == list:
			if len(self.board[x][y]) > z:
				return True
		else:
			if z == 0:
				return True
		return False

	def move(self, x1, y1, z1, x2, y2, z2): #Moves peice1 to peice2 and takes peice2 - False if out of bounds and if illegal move in general
		peice1 = self.boardPoi(x1,y1,z1)
		peice2 = self.boardPoi(x2,y2,z2)
		if peice2 == "X" or peice1 == "X" or peice1 == "" or peice1 == False or peice2 == False:
			return False
		else:
			if peice2 != "":
				if peice2.getTeam() == peice1.getTeam() or peice2.peice() == "k":
					return False

		if self.checkSetPoi(x1,y1,z1) or self.checkSetPoi(x2,y2,z2):
			self.setPoi(x1,y1,z1,"")
			peice1.setCoords(x2,y2,z2)
			self.setPoi(x2,y2,z2,peice1)
		else:
			return False

		if peice2 != "":
			self.playersTakenPeices[self.playerturn].append(peice2)

	def debugPrint(self):
		counter = 0
		strboard = "    0  \t    1  \t    2  \t    3  \t    4  \t    5\n"
		for i in self.board:
			strboard += str(counter) + "|"
			for j in i:
				if type(j) == list:
					for x in j:
						if x == "":
							strboard += "  "
						elif x == "X":
							strboard += "X "
						elif x == "T":
							strboard += "T "
						elif x == "A":
							strboard += "A "
						elif x == "R":
							strboard += "R "
						else:
							strboard += x.getTeam() + x.peice()
						strboard += "|"
					strboard = strboard[:-1] + "\t|"
				else:
					if j == "":
						strboard += "     \t|"
					elif j == "X":
						strboard += "X    \t|"
					elif j == "T":
						strboard += "T    \t|"
					elif j == "A":
						strboard += "A    \t|"
					elif j == "R":
						strboard += "R    \t|"
					else:
						strboard += j.getTeam() + j.peice() + "   \t|"
			strboard += "\n"
			counter += 1
		return strboard[:-1]
	#~~~~

#~~~~~~~~~~~~~~~~~~~~~
