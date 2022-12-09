"""
This module loads the actors from the corresponding files
based on whether it's in test mode or not
"""

def get_actors(testMode=False):
    filename = "actors.txt"
    if testMode:
        filename = "actorsTest.txt"
    actors = {}

    with open(filename, "r", encoding="latin-1") as f:
        for entry in f:
            id, actorName = entry.split("|")
            actors[id.strip()] = actorName.strip()
    return actors

