#Infomation~~~~~~~~~~~

#This is the setup for a new game of a starTrek 3DChess.
#Holds the control loops for the game as well

#~~~~~~~~~~~~~~~~~~~~~


#External imports
import subprocess as sp
from copy import deepcopy

#Internal imports
import Utils.generalUtil as generalUtil
import drawStarTrekBoard as draw
import AI.AIUtil as AIUtil
import gamestate

import Peices.pawn as pawn
import Peices.knight as knight
import Peices.castle as castle
import Peices.king as king
import Peices.queen as queen
import Peices.rook as rook


#Is the control structure for a new game of starTrek 3DChess
#Input () ~~~ Outputs None
def main():
	#Board Initilisation~~

	bk = king.King()
	bqs = [queen.Queen()]
	brs = [rook.Rook(), rook.Rook()]
	bcs = [castle.Castle(), castle.Castle()]
	bhs = [knight.Knight(), knight.Knight()]
	bps = []
	for i in range(0, 8):
		bps.append(pawn.Pawn())

	wk = king.King()
	wqs = [queen.Queen()]
	wrs = [rook.Rook(), rook.Rook()]
	wcs = [castle.Castle(), castle.Castle()]
	whs = [knight.Knight(), knight.Knight()]
	wps = []
	for i in range(0, 8):
		wps.append(pawn.Pawn())

	bk.setup(0,4,0,"b")
	bqs[0].setup(0,1,0,"b")
	brs[0].setup(0,0,0,"b")
	brs[1].setup(0,5,0,"b")
	bcs[0].setup(1,2,1,"b")
	bcs[1].setup(1,3,0,"b")
	bhs[0].setup(1,1,0,"b")
	bhs[1].setup(1,4,0,"b")
	bps[0].setup(1,0,0,1,0,"b")
	bps[1].setup(1,1,1,1,0,"b")
	bps[2].setup(1,4,1,1,0,"b")
	bps[3].setup(5,1,0,1,0,"b")
	bps[4].setup(2,1,0,1,0,"b")
	bps[5].setup(2,2,0,1,0,"b")
	bps[6].setup(2,3,0,1,0,"b")
	bps[7].setup(2,4,0,1,0,"b")

	wk.setup(9,4,0,"w")
	wqs[0].setup(9,1,0,"w")
	wrs[0].setup(9,0,0,"w")
	wrs[1].setup(9,5,0,"w")
	wcs[0].setup(8,2,0,"w")
	wcs[1].setup(8,3,0,"w")
	whs[0].setup(8,1,0,"w")
	whs[1].setup(8,4,0,"w")
	wps[0].setup(8,0,0,-1,0,"w")
	wps[1].setup(8,1,1,-1,0,"w")
	wps[2].setup(8,4,1,-1,0,"w")
	wps[3].setup(8,5,0,-1,0,"w")
	wps[4].setup(7,1,0,-1,0,"w")
	wps[5].setup(7,2,0,-1,0,"w")
	wps[6].setup(7,3,0,-1,0,"w")
	wps[7].setup(7,4,0,-1,0,"w")

	players = ["User","User"]

	game = gamestate.gamestate()
	game.setup([[brs[0], bqs[0],	  "X",	   "X",	    bk,		     brs[1]],
				[bps[0], [bps[1],bhs[0]], bcs[0],  bcs[1],  [bps[2],bhs[1]], bps[3]],
				["X",	 bps[4],	  bps[5],  bps[6],  bps[7],	     	 "X"],
				["X",	 ["",""],	  ["",""], ["",""], ["",""],	     "X"],
				["X",	 ["",""],	  ["",""], ["",""], ["",""],	     "X"],
				["X",	 ["",""],	  ["",""], ["",""], ["",""],	     "X"],
				["X",	 ["",""],	  ["",""], ["",""], ["",""],	     "X"],
				["X",	 wps[4],	  wps[5],  wps[6],  wps[7],	     "X"],
				[wps[0], [wps[1],whs[0]], wcs[0],  wcs[1],  [wps[2],whs[1]], wps[3]],
				[wrs[0], wqs[0],	  "X",	   "X",	    wk,		     wrs[1]]],players)

	#~~~~~~~~~~~~~~~~~~~~~


	#Game Loop~~~~~~~~~~~~

	yn = True

	while yn:
		if game.getPlayers()[game.getTurn()] == "User":
			controlIfUser(game)
		elif game.getPlayers()[game.getTurn()] == "Bot":
			controlIfBot(game)
		else:
			print("Player " + str(game.getTurn()+1) + " is unrecongised")

	#~~~~~~~~~~~~~~~~~~~~~

def controlIfUser(game):
	#Clears the screen
	tmp = sp.call('clear',shell=True)

	draw.draw(game, None)
	print("\n\n" + "PLayer - " + str(game.getTurn() + 1) + "'s turn")
	moveinput = raw_input("\n\nWhat move would you like to make?")

	#Handles input instructions
	if moveinput[0] == "m":
		#Reads input
		moveinput = moveinput[2:].replace(" ", "").split("-")
		coords1 = moveinput[0].split(",")
		for i in range(0, len(coords1)):
			coords1[i] = int(coords1[i])
		coords2 = moveinput[1].split(",")
		for i in range(0, len(coords2)):
			coords2[i] = int(coords2[i])

		validmoves = game.boardPoi(coords1[0], coords1[1], coords1[2]).getValidMoveCoords(game)
		peice1 = game.boardPoi(coords1[0], coords1[1], coords1[2])

		#Control
		if peice1 == "" or peice1 == "X" or peice1 == False:
			print("Invalid coord 1")
		else:
			coords2.append("m")
			if coords2 in validmoves:
				game.move(coords1[0], coords1[1], coords1[2], coords2[0], coords2[1], coords2[2])
				if peice1.peice() == "p":
					peice1.setMoved()
			else:
				del coords2[-1]

				coords2.append("t")
				if coords2 in validmoves:
					game.move(coords1[0], coords1[1], coords1[2], coords2[0], coords2[1], coords2[2])
					if peice1.peice() == "p":
						peice1.setMoved()
				else:
					print("Invalid coord 2")
		game.nextTurn()

	elif moveinput[0] == "x":
		#Reads input
		moveinput = moveinput[2:].replace(" ", "")
		coords1 = moveinput.split(",")
		for i in range(0, len(coords1)):
			coords1[i] = int(coords1[i])
		peice1 = game.boardPoi(coords1[0], coords1[1], coords1[2])

		#Control
		if peice1 == "" or peice1 == "X" or peice1 == False:
			print("Invalid coord1")
		else:
			temp = []
			for i in game.boardPoi(coords1[0], coords1[1], coords1[2]).getValidMoveCoords(game):
				if i[3] == "m":
					temp.append(["T",i[0],i[1],i[2]])
				elif i[3] == "t":
					temp.append(["A",i[0],i[1],i[2]])
			draw.close()
			draw.draw(game, temp)
	else:
		print("Invalid input, please try again")
	raw_input()
	draw.close()


def controlIfBot(game): ### TODO: Make this
	print("I am robot")
	raw_input()
