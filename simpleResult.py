class SimpleResult:

    def __init__(self, myPoints, opponentPoints, opponentId):
        self.myPoints = myPoints
        self.opponentPoints = opponentPoints
        self.opponentId = opponentId

    def __str__(self):
        return "myPoints: " + str(self.myPoints) + ", opponentPoints: " + str(self.opponentPoints) + ", opponentId: " + str(self.opponentId)