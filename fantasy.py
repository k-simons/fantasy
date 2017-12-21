from espnff import League

from testClass import Test

import requests
import json




league_id = 1278861
years = [2013, 2014, 2015, 2016, 2017]

syears = [2017]

ENDPOINT = "http://games.espn.com/ffl/api/v2/"

for year in syears:
    path = "main-" + str(year) + ".json"
    data = json.load(open(path))

    leagueSettings = data["leaguesettings"]

    teams = leagueSettings["teams"]
    # teams is map from int to team. int is not useful
    keys = list(teams.keys())
    aTeamKey = keys[0]
    print(aTeamKey)

    team = teams[aTeamKey]

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
            "awayTeamScores": [109.58],
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
    scheduleItems = team["scheduleItems"]

    scheduleItem = team["scheduleItems"][0]

    matchups = scheduleItem["matchups"]

    matchup = matchups[0]

    print(matchup)



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