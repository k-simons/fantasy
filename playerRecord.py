class PlayerRecord:

    def __init__(self, team, simpleResults):
        self.team = team
        self.simpleResults = simpleResults

    def __str__(self):
        a = self.team.__str__()
        for simpleResult in self.simpleResults:
            a = a + " " + simpleResult.__str__()
        return a

    def getTotalPointsScored(self):
        total = 0
        for simpleResult in self.simpleResults:
            total = total + simpleResult.myPoints
        return total

    def getTotalWins(self):
        wins = 0
        for simpleResult in self.simpleResults:
            if simpleResult.myPoints > simpleResult.opponentPoints:
                wins = wins + 1
        return wins

    def getWinsAgainstPlayerId(self, opponentId):
        wins = 0
        for simpleResult in self.simpleResults:
            if (simpleResult.myPoints > simpleResult.opponentPoints) & (opponentId == simpleResult.opponentId):
                wins = wins + 1
        return wins

    def getGamesAgainstPlayerId(self, opponentId):
        games = 0
        for simpleResult in self.simpleResults:
            if opponentId == simpleResult.opponentId:
                games = games + 1
        return games

    def getWinsPercent(self):
        return self.getTotalWins() / len(self.simpleResults)

    def getWinsPercentAgainstDerek(self):
        return self.getWinsPercentAgainstId(1)

    def getWinsPercentAgainstId(self, id):
        gamesAgainstPlayer = self.getGamesAgainstPlayerId(id)
        if gamesAgainstPlayer == 0:
            return 1
        winsAgainstPlayerId = self.getWinsAgainstPlayerId(id)
        return winsAgainstPlayerId / gamesAgainstPlayer
