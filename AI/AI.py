import AIUtil

class AI:

    #Initilisation
    def setup(self, deterministic, training, team):
        self.deterministic = deterministic
        self.training = training
        self.team = team
    #~~~~

    #Getters

    #~~~~

    #Setters

    #~~~~

    #Funcs
    def mainDT(self, game):
        AIUtil.test()
    def mainTF(self, game):
        print("Unfinished") ## TODO: Create
    def mainTT(self, game):
        print("Unfinished") ## TODO: Create
    #~~~~

    #Interface
    def main(self, game):
        if self.deterministic == True:
            self.mainDT(game)
        elif self.training == False:
            self.mainTF(game)
        else:
            self.mainTT(game)
    #~~~~

tom = AI()
tom.setup(True, False, "b")
