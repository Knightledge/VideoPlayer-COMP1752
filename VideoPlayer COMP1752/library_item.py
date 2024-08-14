class LibraryItem:
    def __init__(self, name = None, director= None, rating=0 ,url= None):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = 0
        self.url = url
    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars