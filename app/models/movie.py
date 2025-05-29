class Movie:
    def __init__(self, title: str, genre: str, release_date: str):
        self.title = title
        self.genre = genre
        self.release_date = release_date

    def __str__(self):
        return f"Title: {self.title} | Genre: {self.genre} | Release Date: {self.release_date}"