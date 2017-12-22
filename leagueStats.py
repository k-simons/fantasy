class LeagueStats:

    def __init__(self, playerRecords):
        self.playerRecords = playerRecords

    def sortByAveragePoints(self):
        playerPointsTuples = self.sortField(lambda playerRecord: playerRecord.getAveragePointsScored())
        for playerPointsTuple in playerPointsTuples:
            print(playerPointsTuple[1].firstName + " " + str(playerPointsTuple[0]))

    def sortField(self, lambdaFunc):
        playerPointsTuple = []
        for playerRecord in self.playerRecords:
            playerPointsTuple.append([lambdaFunc(playerRecord), playerRecord.team])
        playerPointsTuple.sort(key=lambda tup: tup[0], reverse=True)
        return playerPointsTuple
