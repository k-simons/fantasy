class Team:

    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.name = firstName + " " + lastName

    def __str__(self):
        return "id: " + str(self.id) + ", name: " + self.name