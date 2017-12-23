class Team:

    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName.strip()
        self.lastName = lastName.strip()
        self.name = self.firstName + " " + self.lastName

    def __str__(self):
        return "id: " + str(self.id) + ", name: " + self.name