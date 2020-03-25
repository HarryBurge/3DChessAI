#Infomation~~~~~~~~~~~

#This is basically the start up script which will direct the program to what needs to be done.
#Creates a user interface menu to be able to choose from a few options to what they want to do.

#~~~~~~~~~~~~~~~~~~~~~


#External imports
import subprocess as sp

#Internal imports
import gamestate
import mainStarTrek


#Menu~~~~~~~~~~~~~~~~~

yn = True

while yn: #Basic menu loop

	tmp = sp.call('clear',shell=True) #Clears screen

	print("""
 ___________  _____ _                     ___  _____
|____ |  _  \/  __ \ |                   / _ \|_   _|
    / / | | || /  \/ |__   ___  ___ ___ / /_\ \ | |
    \ \ | | || |   | '_ \ / _ \/ __/ __||  _  | | |
.___/ / |/ / | \__/\ | | |  __/\__ \__ \| | | |_| |_
\____/|___/   \____/_| |_|\___||___/___/\_| |_/\___/
	\n
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{1} New StarTrek Game
{10} Load Game
{99} Exit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

	input = raw_input(">> ")

	if input == "1": #Starts a new StarTrek game
		mainStarTrek.main()

	elif input == "10": #Loads a game from a save file
		print("Not Made Yet")

	elif input == "99": #Exits
		yn = False

	else: #Basic error checking
		print("Not a valid option")

	raw_input()

#~~~~~~~~~~~~~~~~~~~~~
