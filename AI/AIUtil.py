def test():
    print("Hello I am Tom")

def scoreForCurrentBoard(gameboard):
    print("Death to humans")

#Funcs for scoreForCurrentBoard
def getPeicesVunerable(game, team):

    #A list of all moves that have a take action outputs like [[SourceObject, [x,y,z,"t"], TargetObject], ...]
    allTakeMovesWithSource = []
    for i in getAllMovesWithPeices(game):
        if i[1] != None:
            for j in i[1]:
                if j[3] == "t":
                    allTakeMovesWithSource.append([i[0], j, game.boardPoi(j[0], j[1], j[2])])

    #Scrubs the above list to make sure that only gives peices that are part of the team of the AI
    vunerablePeices = []
    for i in allTakeMovesWithSource:
        if i[0].getTeam() != team and i[2].getTeam() == team and i[2] not in vunerablePeices:
            vunerablePeices.append(i[2])

    return vunerablePeices

def getPeicesTakeable(game, team):
    print("Take")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#A list of all moves possible outputs [[PeiceObject, [[x,y,z,{"o","t","m"}], ....]], .....]
def getAllMovesWithPeices(game):
    movesWithPeices = []
    for i in game.getBoard():
        for j in i:
            if type(j) == list:
                for k in j:
                    if k != "" and k != "X":
                        movesWithPeices.append([k, k.getValidMoveCoords(game)])
            else:
                if j != "" and j != "X":
                    movesWithPeices.append([j, j.getValidMoveCoords(game)])
    return movesWithPeices
