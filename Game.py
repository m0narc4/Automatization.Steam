class Game:
    def __init__(self, title, release_date, price):
        self.title = title
        self.release_date = release_date
        self.price = price

    def getTitle(self):
        return self.title

    def getReleaseDate(self):
        return self.release_date

    def getPrice(self):
        return self.price