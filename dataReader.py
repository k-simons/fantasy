import json

years = [2013, 2014, 2015, 2016, 2017]

def generateTeamsByYear():
    teamsByYears = []
    for year in years:
        path = "data/main-" + str(year) + ".json"
        data = json.load(open(path))
        leagueSettings = data["leaguesettings"]
        teamsByYears.append(leagueSettings["teams"])
    return teamsByYears