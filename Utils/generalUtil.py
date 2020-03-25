def lineMoves(peice, game, x, y, z, dx, dy, dz):
	if game.boardPoi(x, y, z) == "X" or game.boardPoi(x, y, z) == False:
		if game.boardPoi(x, y, z+1) == "X" or game.boardPoi(x, y, z+1) == False:
			if game.boardPoi(x, y, z-1) == "X" or game.boardPoi(x, y, z-1) == False:
				return [] #Base Condition
			else:
				if game.boardPoi(x, y, z-1) == "":
					temp = []
					for i in lineMoves(peice, game, x+dx, y+dy, z+dz-1, dx, dy, dz):
						temp.append(i)
					temp.append([x,y,z-1,"m"])
					return temp
				else:
					if game.boardPoi(x,y,z-1).getTeam() != peice.getTeam():
						return [[x,y,z-1,"t"]]
					elif game.boardPoi(x,y,z-1).getTeam() == peice.getTeam():
						return [[x,y,z-1,"o"]]
					return []
		else:
			if game.boardPoi(x, y, z+1) == "":
				temp = []
				for i in lineMoves(peice, game, x+dx, y+dy, z+dz+1, dx, dy, dz):
					temp.append(i)
				temp.append([x,y,z+1,"m"])
				return temp
			else:
				if game.boardPoi(x,y,z+1).getTeam() != peice.getTeam():
					return [[x,y,z+1,"t"]]
				elif game.boardPoi(x,y,z+1).getTeam() == peice.getTeam():
					return [[x,y,z+1,"o"]]
				return []
	else:
		if game.boardPoi(x, y, z) == "":
			temp = []
			for i in lineMoves(peice, game, x+dx, y+dy, z+dz, dx, dy, dz):
				temp.append(i)
			for i in lineMoves(peice, game, x+dx, y+dy, z+dz+1, dx, dy, dz):
				temp.append(i)
			for i in lineMoves(peice, game, x+dx, y+dy, z+dz-1, dx, dy, dz):
				temp.append(i)
			temp.append([x,y,z,"m"])
			return temp
		else:
			if game.boardPoi(x,y,z).getTeam() != peice.getTeam():
				return [[x,y,z,"t"]]
			elif game.boardPoi(x,y,z).getTeam() == peice.getTeam():
				return [[x,y,z,"o"]]
			return []
