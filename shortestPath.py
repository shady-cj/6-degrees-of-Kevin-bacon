from movieActorGraph import build_graph

class State:
    """
    The State class helps to keep track of each nodes and
    its parent during a bfs traversal, This helps to maintain
    the relationship of movie-actors and also ensure shortest path
    """
    def __init__(self, node, parent=None):
        self.node = node
        self.movie_connection = None
        self.parent = parent

graph = build_graph()
dst = 'Kevin Bacon'

def shortest_path(src):
    """
    This function Implements the bfs traversal to determine the shortest path
    of an actor to Kevin Bacon
    """
    rootVertex = graph.getVertex(src)
    if rootVertex is None:
        raise KeyError
    root = State(rootVertex)
    queue = [root]

    visited = set([])

    while len(queue) > 0:
        currentActor = queue.pop(0)
        if currentActor.node.getName() == dst:
            return currentActor
        for actor in currentActor.node.getConnections():
            movieName = actor.get("label")
            actorName = actor.get("name")
            if ((actorName, movieName) not in visited):
                visited.add((actorName, movieName))
                getV = graph.getVertex(actorName)
                new_node = State(getV)
                new_node.parent = currentActor
                new_node.movie_connection = movieName
                queue.append(new_node)
    return None


def get_bacon_number(name):
    """
    Gets the bacon number and formats the output on the screen
    and the returns a dictionary which is then used by plotGraph
    """
    try:
        root = shortest_path(name)
        if root:
            relationship_table = {}
            l = []
            nodes = []
            while root:
                nodes.append(root.node.getName())
                if root.parent:
                    l.append((root.parent.node, root.node, root.movie_connection))
                else:
                    l.append((None, root.node, root.movie_connection))
                root = root.parent

            l.reverse()
            print(f"{l[0][1].getName()}'s number is {len(l[1:])}")

            for entry in l:
                if all([entry[0], entry[1]]):
                    firstPerson = entry[0].getName()
                    secondPerson = entry[1].getName()
                    movie_connection = entry[2]
                    print(f"{firstPerson} appeared in {movie_connection} with {secondPerson}")

            relationship_table["edges"] = l
            relationship_table["nodes"] = nodes
            return relationship_table

        else:
            print('Not present')
    
    except KeyError:
        print('No Such Person on Record')
    return None

