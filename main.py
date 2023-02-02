import json

### Classes
## Team class
class Team:
    def __init__(self, name, hthDict):
        self.name = name
        self.headToHeadDict = hthDict

## League class (collection of teams)
class League:
    def __init__(self, teams):
        self.teams = teams
        self.matrix = Matrix(self.getTeamNamesList())
    
    # Returns list of all team names in the League
    def getTeamNamesList(self):
        names = []
        for team in self.teams:
            names.append(team.name)

        return names

    # Populates all rows of matrix object with data from teams in league
    def populateMatrix(self):
        for i in range(len(self.teams)):
            self.matrix.populateRow(self.teams[i])

    # Prints the matrix object from the league. Requires populate Matrix to be run before
    def printMatrix(self):
        self.matrix.printMatrix()
        
## Matrix class
class Matrix:
    def __init__(self, labels):
        self.labels = labels
        self.size = len(labels)
        self.data = [["--" for i in range(self.size)] for j in range(self.size)] # Initializes "--" for empty rows

    def populateRow(self, data):
        # Find index of team in labels list
        index = -1

        for i in range(self.size):
            if self.labels[i] == data.name:
                index = i
        
        if index < 0:
            return -1
        
        # Create lists form the given team's dictionary data
        keys = list(data.headToHeadDict.keys())
        values = list(data.headToHeadDict.values())

        # Add data to the matrix when the corresponding cell is found
        for i in range(len(keys)):
            for j in range(self.size):
                if keys[i] == self.labels[j]:
                    self.data[index][j] = values[i]['W'] # No need to put in the losses since those are just other teams' wins

    def printMatrix(self):
        # Print top row
        print("Tm", end="\t")
        for i in range(len(self.labels)):
            print(self.labels[i], end="\t")
        
        # New line
        print()
        
        # Print rows with data
        for i in range(len(self.labels)):
            # Team header
            print(self.labels[i], end="\t")

            # Print row of data
            for j in range(len(self.labels)):
                print(self.data[i][j], end="\t")
            
            # New line
            print()


### Main body
# Load file data
file = open('data.json')
jsonData = json.load(file)

# Create list for teams to give to League class
teams = []

# Add each team to the teams list
for team in jsonData.keys():
    teamObj = Team(team, jsonData.get(team))
    teams.append(teamObj)
    del teamObj

# Create League object
leagueObj = League(teams)

# Print matrix from League object
leagueObj.populateMatrix()
leagueObj.printMatrix()