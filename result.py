class Result:

    def __init__(self, player1Id, player1Score, player2Id, player2Score, year):
        self.player1Id = player1Id
        self.player1Score = player1Score
        self.player2Id = player2Id
        self.player2Score = player2Score
        self.year = year

    def __str__(self):
        return "player1Id: " + str(self.player1Id) + ", player1Score: " + str(self.player1Score) + ", player2Id: " + str(self.player2Id) + ", player2Score: " + str(self.player2Score) + ", year: " + str(self.year)