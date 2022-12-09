"""
The module contains classes and function
that helps build a bfs graph
"""

from getMovieActors import get_movie_actors
from getMovies import get_movies
from getActors import get_actors




class Vertex:
    """
    The vertex class creates a vertex and creates a relationship
    for each nodes connected to the vertex, using movie name as the label
    connecting the 2 edges together
    """
    def __init__(self, key):
        self.name = key
        self.connected_to = []
    
    def addNeighbor(self, nbr, label):
        self.connected_to.append({"name": nbr, "label": label})

    def getConnections(self):
        return self.connected_to

    def getName(self):
        return self.name
    

class Graph:
    """
    A graph class that creates a bfs tree and maps movies and the actors
    connected to them
    """
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        if key not in self.vertList:
            self.numVertices += 1
            newVertex = Vertex(key)
            self.vertList[key] = newVertex
            return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, fromVertex, toVertex, label):
        if fromVertex not in self.vertList:
            self.addVertex(fromVertex)
        if toVertex not in self.vertList:
            self.addVertex(toVertex)
        
        self.vertList[fromVertex].addNeighbor(toVertex, label)

    def getVertices(self):
        return list(self.vertList.keys())



def build_graph():
    """
    This function builds an bfs graph with the Graph class
    using actors, movies, and movieActors to map the relationships
    """
    actors = get_actors()
    movies = get_movies()
    movieActors = get_movie_actors()
    graph = Graph()

    for k, v in movieActors.items():
        movieName = movies[k]
        for actor_id in v:
            actor_name = actors[actor_id]
            graph.addVertex(actor_name)
            for rel_actor_id in v:
                if rel_actor_id == actor_id:
                    continue
                rel_actor_name = actors[rel_actor_id]
                graph.addEdge(actor_name, rel_actor_name, movieName)
    return graph

