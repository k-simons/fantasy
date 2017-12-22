from team import Team

class TeamLocators:

    def __init__(self, teamsInYears):
        self.teamIdMap = {}
        for teamsInAYear in teamsInYears:
            # teams is map from int to team. int is team id
            for teamId in teamsInAYear:
                team = teamsInAYear[teamId]
                owners = [owner for owner in team["owners"] if owner["primaryOwner"] == True] # WTF multi owner Alistair
                if (len(owners) != 1):
                    raise Exception('Owners are not 1')
                owner = owners[0]
                intTeamId = int(teamId)
                team = Team(intTeamId, owner["firstName"], owner["lastName"])
                self.teamIdMap[intTeamId] = team

    def getAllTeamIds(self):
        teamIds = []
        for teamId in self.teamIdMap:
            teamIds.append(teamId)
        return teamIds

    def getTeamFromId(self, teamId):
        return self.teamIdMap[teamId]
