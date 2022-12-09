from movieActorGraph import graph


class Graph:
    def __init__(self, state, parent=None):
        self.node = state
        self.parent = parent


dst = 'Kevin Bacon'
def shortest_path(src):
    parent = Graph({'name':src, 'movie': None, 'Bacon': 0}) 
    queue = [parent]

    visited = set([])

    while len(queue) > 0:
        currentActor = queue.pop(0)
        if currentActor.node['name'] == dst:
            return currentActor
        for actor in graph[currentActor.node['name']]:
            if ((actor['name'], actor['movie']) not in visited):
                visited.add((actor['name'], actor['movie']))
                actor['Bacon'] = currentActor.node['Bacon'] + 1
                new_node = Graph(actor)
                new_node.parent = currentActor
                queue.append(new_node)
    return None


def get_bacon_number(name):
    try:
        root = shortest_path(name)
        if root:

            l = []
            while root:
                l.append(root.node)
                root = root.parent

            l.reverse()
            print(f"{l[0]['name']}'s number is {len(l[1:])}")

            for i, entry in enumerate(l):
                k = i + 1
                if (k < len(l)):
                    print(f"{entry['name']} appeared in {l[k]['movie']} with {l[k]['name']}")
            return l

        else:
            print('Not present')
    
    except KeyError:
        print('No Such Person on Record')
    return None

