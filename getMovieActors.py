import os


movieActors = {}

with open("movie-actorsTest.txt", "r", encoding="latin-1") as f:
    for entry in f:
        movieId, actorId = entry.split("|")
        if movieId.strip() in movieActors:
            movieActors[movieId.strip()] += [actorId.strip()]
        else:
            movieActors[movieId.strip()] = [actorId.strip()]
"""
movieActorsEdges = {}
for k, v  in movieActors.items():
    for k_entry in v:
        for v
"""
