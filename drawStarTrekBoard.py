#Infomation~~~~~~~~~~~

#This is a Util that gives a graphical image to represent the gamestate of the board.

#~~~~~~~~~~~~~~~~~~~~~


#External imports
from PIL import Image
import psutil


#Draw tools~~~~~~~~~~~

#Draws a StarTrekBoard
#Inputs (Class gamestate, [[{"T","R","A"}, int x, int y, int z], ... ]) ~~~ Outputs None
def draw(gameboard, overlay):
    try:

        #Gets all the images for the GUI
        img = Image.open("Images/StarTrekBoard.png")
        atboardTL = Image.open("Images/StarTrekAttackBoardTL.png")
        atboardTR = Image.open("Images/StarTrekAttackBoardTR.png")
        atboardBL = Image.open("Images/StarTrekAttackBoardBL.png")
        atboardBR = Image.open("Images/StarTrekAttackBoardBR.png")

        check = Image.open("Images/Check.png")
        dngr = Image.open("Images/DangerSquare.png")
        takable = Image.open("Images/RedSquare.png")

        bk = Image.open("Images/BlackKing.png")
        bq = Image.open("Images/BlackQueen.png")
        bh = Image.open("Images/BlackKnight.png")
        br = Image.open("Images/BlackRook.png")
        bc = Image.open("Images/BlackCastle.png")
        bp = Image.open("Images/BlackPawn.png")

        wk = Image.open("Images/WhiteKing.png")
        wq = Image.open("Images/WhiteQueen.png")
        wh = Image.open("Images/WhiteKnight.png")
        wr = Image.open("Images/WhiteRook.png")
        wc = Image.open("Images/WhiteCastle.png")
        wp = Image.open("Images/WhitePawn.png")
        #~~~~

        #Puts the attack boards into poisition
        img.paste(atboardTL, (0, 0))
        img.paste(atboardTR, (420, 0))
        img.paste(atboardBL, (0, 810))
        img.paste(atboardBR, (420, 810))
        #~~~~

        #Loops through all x,y coords in the gameboard
        for i in range(len(gameboard.getBoard())):
            for j in range(len(gameboard.getBoard()[i])):
        #~~~~

                #If specfic x,y coord has a z dimension then loop it
                if type(gameboard.getBoard()[i][j]) == list:
                    for k in range(len(gameboard.getBoard()[i][j])):
                #~~~~

                        tempk = gameboard.boardPoi(i,j,len(gameboard.getBoard()[i][j]) - 1 - k) #Gets object that has been iterated onto

                        if tempk != "" and tempk != "X": #Checks if object is not a Peice

                            #If the peice is part of the black team
                            if tempk.getTeam() == "b":

                                #Print the image corresponding to the peice that the object is
                                if tempk.peice() == "k":
                                    img.paste(resize(bk), (boardPoi2Coords(i, j, tempk.z)[0], boardPoi2Coords(i, j, tempk.z)[1]))
                                elif tempk.peice() == "q":
                                    img.paste(resize(bq), (boardPoi2Coords(i, j, tempk.z)[0], boardPoi2Coords(i, j, tempk.z)[1]))
                                elif tempk.peice() == "h":
                                    img.paste(resize(bh), (boardPoi2Coords(i, j, tempk.z)[0], boardPoi2Coords(i, j, tempk.z)[1]))
                                elif tempk.peice() == "r":
                                    img.paste(resize(br), (boardPoi2Coords(i, j, tempk.z)[0], boardPoi2Coords(i, j, tempk.z)[1]))
                                elif tempk.peice() == "c":
                                    img.paste(resize(bc), (boardPoi2Coords(i, j, tempk.z)[0], boardPoi2Coords(i, j, tempk.z)[1]))
                                elif tempk.peice() == "p":
                                    img.paste(resize(bp), (boardPoi2Coords(i, j, tempk.z)[0], boardPoi2Coords(i, j, tempk.z)[1]))
                                #~~~~

                            #If the peice is part of the white team
                            elif tempk.getTeam() == "w":

                                #Print the image corresponding to the peice that the object is
                                if tempk.peice() == "k":
                                    img.paste(resize(wk), (boardPoi2Coords(i, j, tempk.z)[0], boardPoi2Coords(i, j, tempk.z)[1]))
                                elif tempk.peice() == "q":
                                    img.paste(resize(wq), (boardPoi2Coords(i, j, tempk.z)[0], boardPoi2Coords(i, j, tempk.z)[1]))
                                elif tempk.peice() == "h":
                                    img.paste(resize(wh), (boardPoi2Coords(i, j, tempk.z)[0], boardPoi2Coords(i, j, tempk.z)[1]))
                                elif tempk.peice() == "r":
                                    img.paste(resize(wr), (boardPoi2Coords(i, j, tempk.z)[0], boardPoi2Coords(i, j, tempk.z)[1]))
                                elif tempk.peice() == "c":
                                    img.paste(resize(wc), (boardPoi2Coords(i, j, tempk.z)[0], boardPoi2Coords(i, j, tempk.z)[1]))
                                elif tempk.peice() == "p":
                                    img.paste(resize(wp), (boardPoi2Coords(i, j, tempk.z)[0], boardPoi2Coords(i, j, tempk.z)[1]))
                                #~~~~

                else: #Else the specific x,y is flat therefore z = 0

                    tempk = gameboard.boardPoi(i,j,0) #Gets object that has been iterated onto

                    if tempk != "" and tempk != "X":

                        #If the peice is part of the black team
                        if tempk.getTeam() == "b":

                            #Print the image corresponding to the peice that the object is
                            if tempk.peice() == "k":
                                img.paste(resize(bk), (boardPoi2Coords(i, j, 0)[0], boardPoi2Coords(i, j, 0)[1]))
                            elif tempk.peice() == "q":
                                img.paste(resize(bq), (boardPoi2Coords(i, j, 0)[0], boardPoi2Coords(i, j, 0)[1]))
                            elif tempk.peice() == "h":
                                img.paste(resize(bh), (boardPoi2Coords(i, j, 0)[0], boardPoi2Coords(i, j, 0)[1]))
                            elif tempk.peice() == "r":
                                img.paste(resize(br), (boardPoi2Coords(i, j, 0)[0], boardPoi2Coords(i, j, 0)[1]))
                            elif tempk.peice() == "c":
                                img.paste(resize(bc), (boardPoi2Coords(i, j, 0)[0], boardPoi2Coords(i, j, 0)[1]))
                            elif tempk.peice() == "p":
                                img.paste(resize(bp), (boardPoi2Coords(i, j, 0)[0], boardPoi2Coords(i, j, 0)[1]))
                            #~~~~

                        #If the peice is part of the white team
                        elif tempk.getTeam() == "w":

                            #Print the image corresponding to the peice that the object is
                            if tempk.peice() == "k":
                                img.paste(resize(wk), (boardPoi2Coords(i, j, 0)[0], boardPoi2Coords(i, j, 0)[1]))
                            elif tempk.peice() == "q":
                                img.paste(resize(wq), (boardPoi2Coords(i, j, 0)[0], boardPoi2Coords(i, j, 0)[1]))
                            elif tempk.peice() == "h":
                                img.paste(resize(wh), (boardPoi2Coords(i, j, 0)[0], boardPoi2Coords(i, j, 0)[1]))
                            elif tempk.peice() == "r":
                                img.paste(resize(wr), (boardPoi2Coords(i, j, 0)[0], boardPoi2Coords(i, j, 0)[1]))
                            elif tempk.peice() == "c":
                                img.paste(resize(wc), (boardPoi2Coords(i, j, 0)[0], boardPoi2Coords(i, j, 0)[1]))
                            elif tempk.peice() == "p":
                                img.paste(resize(wp), (boardPoi2Coords(i, j, 0)[0], boardPoi2Coords(i, j, 0)[1]))
                            #~~~~

        #Checks overlay if there is something it needs to be printed over the top of everything
        if overlay != None:

            #Iterates over the array and draws corresponding pictures too array entrys
            for i in overlay:
                if i[0] == "R":
                    img.paste(dngr, (boardPoi2Coords(i[1], i[2], i[3])[0], boardPoi2Coords(i[1], i[2], i[3])[1]))
                elif i[0] == "A":
                    img.paste(takable, (boardPoi2Coords(i[1], i[2], i[3])[0], boardPoi2Coords(i[1], i[2], i[3])[1]))
                elif i[0] == "T":
                    img.paste(resize(check), (boardPoi2Coords(i[1], i[2], i[3])[0], boardPoi2Coords(i[1], i[2], i[3])[1]))
            #~~~~

    #Error checking
    except IOError:
        pass
    #~~~~

    #Displaying of final image
    img.show()


#Converts gamecoords too image coords for the draw function
#Inputs (int x, int y, int z) ~~~ Outputs [int x, int y]
def boardPoi2Coords(x,y,z):

    coord = [0,0]

    #Converts x,z into image coord
    if x == 0:
        coord[1] = 0
    if x == 1:
        coord[1] = 63
    if x == 2:
        coord[1] = 63*2
    if x == 3 and z == 1:
        coord[1] = 63*3
    if x == 4 and z == 1:
        coord[1] = 63*4
    if x == 3 and z == 0:
        coord[1] = 345
    if x == 4 and z == 0:
        coord[1] = 345 + 63
    if x == 5 and z == 1:
        coord[1] = 345 + 63*2
    if x == 6 and z == 1:
        coord[1] = 345 + 63*3
    if x == 5 and z == 0:
        coord[1] = 620
    if x == 6 and z == 0:
        coord[1] = 620 + 63
    if x == 7:
        coord[1] = 620 + 63*2
    if x == 8:
        coord[1] = 620 + 63*3
    if x == 9:
        coord[1] = 620 + 63*4
    #~~~~

    #Converts y,z into image coord
    if y == 0:
        coord[0] = 0
    if y == 1:
        if x == 0 or x == 9 or ((x == 1 or x == 8) and z == 1):
            coord[0] = 63
        else:
            coord[0] = 150
    if y == 2:
        coord[0] = 150 + 63
    if y == 3:
        coord[0] = 150 + 63*2
    if y == 4:
        if x == 0 or x == 9 or ((x == 1 or x == 8) and z == 1):
            coord[0] = 420
        else:
            coord[0] = 150 + 63*3
    if y == 5:
        coord[0] = 420 + 63
    #~~~~

    return coord


#Resizes images to be the size of a square
#Inputs (Class Image) ~~~~ Outputs Class Image
def resize(img):
    img = img.resize((62,62), Image.ANTIALIAS)
    return img

#~~~~~~~~~~~~~~~~~~~~~

#Closes all images that are open
#Inputs () ~~~~ Outputs None
def close():
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()
