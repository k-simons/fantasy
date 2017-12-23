class PlayerRecord:

    def __init__(self, team, simpleResults):
        self.team = team
        self.simpleResults = simpleResults

    def __str__(self):
        return self.team.__str__() + " with results: " + str(len(self.simpleResults))

    def getTotalPointsScored(self):
        return self.getPointsScoredFromResultList(self.simpleResults)

    def getPointsScoredFromResultList(self, results):
        myPoints = map(lambda simpleResult: simpleResult.myPoints, results)
        return sum(myPoints)

    def getTotalOpponentPointsScored(self):
        return self.getTotalOpponentPointsScoredFromResultList(self.simpleResults)

    def getTotalOpponentPointsScoredFromResultList(self, results):
        theirPoints = map(lambda simpleResult: simpleResult.opponentPoints, results)
        return sum(theirPoints)

    def getAveragePointsScored(self):
        return self.getTotalPointsScored() / len(self.simpleResults)

    def getAveragePointsScoredByOpponent(self):
        return self.getTotalOpponentPointsScored() / len(self.simpleResults)

    def getTotalWins(self):
        return len(self.getWinResultsFromResultList(self.simpleResults))

    def getWinResultsFromResultList(self, results):
        return list(filter(lambda simpleResult: simpleResult.myPoints > simpleResult.opponentPoints, results))

    def getResultsAgainstPlayerId(self, opponentId):
        return self.getResultsWithFilter(lambda simpleResult: opponentId == simpleResult.opponentId)

    def getResultsWithFilter(self, filter):
        return [simpleResult for simpleResult in self.simpleResults if filter(simpleResult)]

    def getWinsPercent(self):
        return self.getTotalWins() / len(self.simpleResults)

    def getWinsPercentAgainstId(self, id):
        resultsAgainstPlayerId = self.getResultsAgainstPlayerId(id)
        numberOfGamesAgainstPlayer = len(resultsAgainstPlayerId)
        if numberOfGamesAgainstPlayer == 0:
            return 1
        winResultsAgainstPlayerId = self.getWinResultsFromResultList(resultsAgainstPlayerId)
        return len(winResultsAgainstPlayerId) / numberOfGamesAgainstPlayer

    def printPlayerProfile(self, teamLocators):
        ## A breakdown of how each player has done
        print("Profile for " + self.team.__str__())
        for teamId in teamLocators.getAllTeamIds():
            if teamId == self.team.id:
                continue
            opponentTeam = teamLocators.getTeamFromId(teamId)
            print(" ")
            print("Stats against: " + opponentTeam.firstName + "  (" + self.team.firstName + "->" + opponentTeam.firstName + ")")
            resultsAgainstOpponent = self.getResultsAgainstPlayerId(teamId)
            numberOfResults = len(resultsAgainstOpponent)
            print("You have played " + str(numberOfResults) + " games against " + opponentTeam.firstName)
            winsAgainstOpponent = self.getWinResultsFromResultList(resultsAgainstOpponent)
            print("You have won: " + str(len(winsAgainstOpponent)) + " games")
            print("You have lost: " + str(numberOfResults - len(winsAgainstOpponent)) + " games")
            pointsAgainstOpponent = self.getPointsScoredFromResultList(resultsAgainstOpponent)
            print("You score an average of " + str(pointsAgainstOpponent / numberOfResults))
            print("Compared to your total average of " + str(self.getAveragePointsScored()))
            averageAgainstNonOpponent = (self.getTotalPointsScored() - pointsAgainstOpponent) / (len(self.simpleResults) - numberOfResults)
            print("Compared to you average against others:  " + str(averageAgainstNonOpponent))
            # print("Compared to your average of " + str(self.getTotalOpponentPointsScoredFromResultList() / numberOfResults))
            #print(self.getPointsScoredFromResultList(resultsAgainstOpponent))
            #print(self.getTotalOpponentPointsScoredFromResultList(resultsAgainstOpponent))
            print(" ")
            break