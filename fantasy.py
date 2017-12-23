
from playerRecord import PlayerRecord
from simpleResult import SimpleResult
from teamLocators import TeamLocators
from dataReader import generateTeamsByYear
from dataReader import years
from leagueStats import LeagueStats

def appendResultsForSingleYear(year, teamsInAYear, simpleResultMap):
    ## we are doubling counting right now
    seenResults = {}
    for teamId in teamsInAYear:
        team = teamsInAYear[teamId]
        for i, scheduleItem in enumerate(team["scheduleItems"]): ## happens every week
            matchups = scheduleItem["matchups"]
            if (len(matchups) != 1):   # no idea why this is an array, error if its ever not 1
                raise Exception('Matchups are not 1')
            matchup = matchups[0]
            player1Id = matchup["homeTeamId"]
            player1Score = matchup["homeTeamScores"][len(matchup["homeTeamScores"]) - 1]
            player2Id = matchup["awayTeamId"]
            player2Score = matchup["awayTeamScores"][len(matchup["awayTeamScores"]) - 1]
            seenKey = str(i) + ":" + str(player1Id)
            # Only add games that have been played
            if (player1Score == 0) & (player2Score == 0):
                continue
            if seenKey not in seenResults:
                seenResults[seenKey] = True
                simpleResultMap[player1Id].append(SimpleResult(player1Score, player2Score, player2Id))
                simpleResultMap[player2Id].append(SimpleResult(player2Score, player1Score, player1Id))

def generateSimpleResultMap(teamLocators):
    simpleResultMap = {}
    for teamId in teamLocators.getAllTeamIds():
        simpleResultMap[teamId] = []
    for i, teamsInAYear in enumerate(generateTeamsByYear()):
        appendResultsForSingleYear(years[i], teamsInAYear, simpleResultMap)
    playerRecords = []
    for teamId in simpleResultMap:
        playerRecords.append(PlayerRecord(teamLocators.getTeamFromId(teamId), simpleResultMap[teamId]))
    return playerRecords


def main():
    teamLocators = TeamLocators(generateTeamsByYear())
    playerRecords = generateSimpleResultMap(teamLocators)
    playersToRunOn = {} #"Kevin": True, "Derek": True}
    for playerRecord in playerRecords:
        if playerRecord.team.firstName in playersToRunOn:
            playerRecord.printPlayerProfile(teamLocators)


    leagueStats = LeagueStats(playerRecords)
    leagueStats.sortByAveragePoints()
    leagueStats.sortWinsPercent()

if __name__ == "__main__": main()
