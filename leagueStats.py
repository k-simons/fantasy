class LeagueStats:

    def __init__(self, playerRecords):
        self.playerRecords = playerRecords

    def sortByAveragePoints(self):
        playerPointsTuples = self.sortField(lambda playerRecord: playerRecord.getAveragePointsScored())
        print("Players sorted by average points:")
        for playerPointsTuple in playerPointsTuples:
            print(playerPointsTuple[1].firstName + " " + str(playerPointsTuple[0]))
        print("---------------------------------")

    def sortByAveragePointsByOpponent(self):
        playerPointsTuples = self.sortField(lambda playerRecord: playerRecord.getAveragePointsScoredByOpponent())
        print("Player's opponent sorted by average points:")
        for playerPointsTuple in playerPointsTuples:
            print(playerPointsTuple[1].firstName + " " + str(playerPointsTuple[0]))
        print("---------------------------------")

    def sortByTotalWins(self):
        playerPointsTuples = self.sortField(lambda playerRecord: playerRecord.getTotalWins())
        print("Players sorted by total wins:")
        for playerPointsTuple in playerPointsTuples:
            print(playerPointsTuple[1].firstName + " " + str(playerPointsTuple[0]))
        print("---------------------------------")

    def sortWinsPercent(self):
        playerPointsTuples = self.sortField(lambda playerRecord: playerRecord.getWinsPercent())
        print("Players sorted by winning percentage:")
        for playerPointsTuple in playerPointsTuples:
            print(playerPointsTuple[1].firstName + " " + str(playerPointsTuple[0]))
        print("---------------------------------")


    def sortField(self, lambdaFunc):
        playerPointsTuple = []
        for playerRecord in self.playerRecords:
            playerPointsTuple.append([lambdaFunc(playerRecord), playerRecord.team])
        playerPointsTuple.sort(key=lambda tup: tup[0], reverse=True)
        return playerPointsTuple
