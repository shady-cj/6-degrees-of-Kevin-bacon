import os


actors = {}

with open("actors.txt", "r", encoding="latin-1") as f:
    for entry in f:
        id, actorName = entry.split("|")
        actors[id.strip()] = actorName.strip()

