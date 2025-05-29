from typing import Optional

class Movie:
    def __init__(
        self,
        title: str,
        genre: str,
        release_date: str,
        overview: Optional[str] = None,
        poster_path: Optional[str] = None,
        tmdb_id: Optional[int] = None
    ):
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.overview = overview
        self.poster_path = poster_path
        self.tmdb_id = tmdb_id

    def __str__(self):
        return f"Title: {self.title} | Genre: {self.genre} | Release Date: {self.release_date}"