
"""
This module loads the movie-actors relationship from the corresponding files
based on whether it's in test mode or not
and creates a dictionary forn each entry
"""

def get_movie_actors(testMode=False):
    filename = "movie-actors.txt"
    if testMode:
        filename = "movie-actorsTest.txt"
    movieActors = {}

    with open(filename, "r", encoding="latin-1") as f:
        for entry in f:
            movieId, actorId = entry.split("|")
            if movieId.strip() in movieActors:
                movieActors[movieId.strip()] += [actorId.strip()]
            else:
                movieActors[movieId.strip()] = [actorId.strip()]
    return movieActors

