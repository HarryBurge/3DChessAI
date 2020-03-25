import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import Utils.generalUtil as gerneralUtil
class Rook: ## TODO: Make sure can move in just z aswell

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
	def getValidMoveCoords(self, game):
		x = self.x
		y = self.y
		z = self.z
		validMoveCoords = []
		for j in range(-1, 2):
			for i in gerneralUtil.lineMoves(self, game, x+1, y+1, z+j, 1, 1, 0):
				validMoveCoords.append(i)
			for i in gerneralUtil.lineMoves(self, game, x+1, y-1, z+j, 1, -1, 0):
				validMoveCoords.append(i)
			for i in gerneralUtil.lineMoves(self, game, x-1, y+1, z+j, -1, 1, 0):
				validMoveCoords.append(i)
			for i in gerneralUtil.lineMoves(self, game, x-1, y-1, z+j, -1, -1, 0):
				validMoveCoords.append(i)

		return validMoveCoords

	def peice(self):
		return "r"

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
