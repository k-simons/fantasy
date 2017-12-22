
from playerRecord import PlayerRecord
from team import Team
from simpleResult import SimpleResult

import json


league_id = 1278861
years = [2013, 2014, 2015, 2016, 2017]

def generateTeamsByYear():
    teamsByYears = []
    for year in years:
        path = "data/main-" + str(year) + ".json"
        data = json.load(open(path))
        leagueSettings = data["leaguesettings"]
        teamsByYears.append(leagueSettings["teams"])
    return teamsByYears

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
            if seenKey not in seenResults:
                seenResults[seenKey] = True
                simpleResultMap[player1Id].append(SimpleResult(player1Score, player2Score, player2Id))
                simpleResultMap[player2Id].append(SimpleResult(player2Score, player1Score, player1Id))

def generateSimpleResultMap(teamIdMap):
    simpleResultMap = {}
    for teamId in teamIdMap:
        simpleResultMap[teamId] = []
    for i, teamsInAYear in enumerate(generateTeamsByYear()):
        appendResultsForSingleYear(years[i], teamsInAYear, simpleResultMap)
    return simpleResultMap

def createTeamMap():
    teamIdMap = {}
    for teamsInAYear in generateTeamsByYear():
        # teams is map from int to team. int is team id
        for teamId in teamsInAYear:
            team = teamsInAYear[teamId]
            owners = [owner for owner in team["owners"] if owner["primaryOwner"] == True] # WTF multi owner Alistair
            if (len(owners) != 1):
                raise Exception('Owners are not 1')
            owner = owners[0]
            name = owner["firstName"] + " " + owner["lastName"]
            intTeamId = int(teamId)
            team = Team(intTeamId, name)
            teamIdMap[intTeamId] = team
    return teamIdMap


teamIdMap = createTeamMap()

simpleResultMap = generateSimpleResultMap(teamIdMap)

playerRecords = []

for teamId in simpleResultMap:
    print(len(simpleResultMap[teamId]))
    playerRecords.append(PlayerRecord(teamIdMap[teamId], simpleResultMap[teamId]))

for playerRecord in playerRecords:
    print(playerRecord.team.name)                    # Kevin Simons
    print(playerRecord.team.id)                      # 2
    print(playerRecord.getWinsPercent())             # 0.5733333333333334
    print(playerRecord.getWinsPercentAgainstDerek()) # 0.16666666666666666
    ## team is finally intresting
'''
    owners ->
        [{
            'lastName': 'Zhou',
            'primaryOwner': True,
            'leagueManager': True,
            'joined': True,
            'inviteId': 0,
            'ownerId': 55363970,
            'userProfileId': 55363970,
            'photoUrl': 'http://f.espncdn.com/avatars/dzindahouse/medium',
            'firstName': 'Derek'
        }]

	record -> {
		'awayPercentage': 0,
		'divisionStanding': 4,
		'overallStanding': 7,
		'divisionLosses': 4,
		'homePercentage': 0,
		'awayTies': 0,
		'divisionWins': 3,
		'streakType': 1,
		'overallTies': 0,
		'homeTies': 0,
		'homeWins': 3,
		'divisionTies': 0,
		'overallPercentage': 0.38462,
		'overallWins': 5,
		'overallLosses': 8,
		'streakLength': 1,
		'pointsAgainst': 1585.78,
		'awayWins': 2,
		'divisionPercentage': 0.42857,
		'homeLosses': 4,
		'pointsFor': 1548.3,
		'awayLosses': 4
	}

	division -> {
		'divisionName': 'East',
		'divisionId': 0,
		'size': 5
	},

    scheduleItems -> list for each week played
        matchups = scheduleItem["matchups"]
        matchup = matchups[0]
        {
            "matchupTypeId": 0,
            "awayTeamScores": [109.58], => is an array for playoff match ups, can just take the last value for now
            "awayTeam": {
                "waiverRank": 10,
                "division": {
                    "divisionName": "SWAG",
                    "divisionId": 0,
                    "size": 5
                },
                "teamAbbrev": "(Y)",
                "teamNickname": "Tiny Tits",
                "logoUrl": "http://i.imgur.com/5T112kt.png",
                "teamLocation": "Yings",
                "teamId": 2,
                "logoType": "customValid"
            },
            "awayTeamAdjustment": 0,
            "awayTeamId": 2,
            "isBye": false,
            "homeTeamId": 1,
            "homeTeamAdjustment": 0,
            "homeTeamScores": [119.38],
            "homeTeamBonus": 0,
            "outcome": 1,
            "homeTeam": {
                "waiverRank": 2,
                "division": {
                    "divisionName": "SWAG",
                    "divisionId": 0,
                    "size": 5
                },
                "teamAbbrev": "KZ",
                "teamNickname": "Zhou",
                "logoUrl": "http://i.imgur.com/SrjgHIc.png",
                "teamLocation": "Kelly",
                "teamId": 1,
                "logoType": "customValid"
            }
        }

    print(matchup)
        eve
        matchups

    '''

    # one for each week played
    #scheduleItems = team["scheduleItems"]
#
    #scheduleItem = team["scheduleItems"][13]
#
    #matchups = scheduleItem["matchups"]
#
    #matchup = matchups[0]
#
    #print(matchup)



# print(data["leaguesettings"]["teams"]["1"])

#x = Test(3.0, -4.5)
#
#print(x.r)
#x.add_trick(1)
#print(x.tricks)

##for year in years:
##    params = {
##        'leagueId': league_id,
##        'seasonId': year
##    }
##    print("Hi")
##    print(year)
##    ## league = League(league_id, year)
##    r = requests.get('%sleagueSettings' % (ENDPOINT, ), params=params,)
##    data = r.json()
##    path = "main-" + str(year) + ".json"
##    print(path)
##    with open(path, 'xt') as f:
##        r = json.dumps(data)
##        print(r)
##        f.write(r)
##        f.close()
##    print("Bye")