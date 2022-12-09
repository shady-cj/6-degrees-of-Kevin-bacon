"""
This module loads the movies from the corresponding files
based on whether it's in test mode or not
and represents them in a dictionary format..
with keys being the movie id and
values being the movie name
"""


def get_movies(testMode=False):
    filename = "movies.txt"
    if testMode:
        filename = "moviesTest.txt"
    movies = {}

    with open(filename, "r", encoding="latin-1") as f:
        for entry in f:
            id, movieName = entry.split("|")
            movies[id.strip()] = movieName.strip()
    return movies

