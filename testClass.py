class Test:

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)