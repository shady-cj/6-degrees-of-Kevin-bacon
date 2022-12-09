import os


movies = {}

with open("movies.txt", "r", encoding="latin-1") as f:
    for entry in f:
        id, movieName = entry.split("|")
        movies[id.strip()] = movieName.strip()

