class Team:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "id: " + self.id + ", name: " + self.name