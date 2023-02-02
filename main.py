import json

### Classes
class Team:
    def __init__(self, name, hthDict):
        self.name = name
        self.headToHeadDict = hthDict

    def teamPrint(self):
        print(self.name)
        print(self.headToHeadDict)
        print()

class League:
    def __init__(self, teams):
        self.teams = teams
        self.matrix = Matrix(self.getTeamNamesList())
    
    def printAll(self):
        for team in teams:
            team.teamPrint()

    def getTeamNamesList(self):
        names = []
        for team in self.teams:
            names.append(team.name)

        return names

    def populateMatrix(self):
        for i in range(len(self.teams)):
            self.matrix.populateRow(self.teams[i])

    def printMatrix(self):
        self.populateMatrix()
        self.matrix.printMatrix()
        
            

class Matrix:
    def __init__(self, labels):
        self.labels = labels
        self.size = len(labels)
        self.data = [["--" for i in range(self.size)] for j in range(self.size)]

    def populateRow(self, data):
        ## Find index of team, take in dict, search for corresponding column, place data
        index = -1

        for i in range(self.size):
            if self.labels[i] == data.name:
                index = i
        
        if index < 0:
            return -1
        
        keys = list(data.headToHeadDict.keys())
        values = list(data.headToHeadDict.values())

        for i in range(len(keys)):
            for j in range(self.size):
                if keys[i] == self.labels[j]:
                    self.data[index][j] = values[i]['W'] #No need to put in the losses since those are just other teams' wins
                    #self.data[j][index] = values[i]['L']

    def printMatrix(self):
        print("Tm", end="\t")
        for i in range(len(self.labels)):
            
            print(self.labels[i], end="\t")

        print()
        
        for i in range(len(self.labels)):
            print(self.labels[i], end="\t")

            #print row of matrix
            for j in range(len(self.labels)):
                print(self.data[i][j], end="\t")
            
            print()


### Main body
file = open('data.json')

jsonData = json.load(file)

teams = []

for team in jsonData.keys():
    teamObj = Team(team, jsonData.get(team))
    teams.append(teamObj)
    del teamObj

leagueObj = League(teams)

leagueObj.printMatrix()