class PlayerRecord:

    def __init__(self, team, simpleResults):
        self.team = team
        self.simpleResults = simpleResults

    def __str__(self):
        return self.team.__str__() + " with results: " + str(len(self.simpleResults))

    def getTotalPointsScored(self):
        myPoints = map(lambda simpleResult: simpleResult.myPoints, self.simpleResults)
        return sum(myPoints)

    def getAveragePointsScored(self):
        return self.getTotalPointsScored() / len(self.simpleResults)

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

    def getWinsPercentAgainstDerek(self):
        return self.getWinsPercentAgainstId(1)

    def getWinsPercentAgainstId(self, id):
        resultsAgainstPlayerId = self.getResultsAgainstPlayerId(id)
        numberOfGamesAgainstPlayer = len(resultsAgainstPlayerId)
        if numberOfGamesAgainstPlayer == 0:
            return 1
        winResultsAgainstPlayerId = self.getWinResultsFromResultList(resultsAgainstPlayerId)
        return len(winResultsAgainstPlayerId) / numberOfGamesAgainstPlayer
