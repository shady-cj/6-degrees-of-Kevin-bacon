from movieActorGraph import graph


class Graph:
    def __init__(self, state, parent=None):
        self.node = state
        self.parent = parent

class Queue:
    def __init__(self):
        self.queue = []

    def add(self, node):
        self.queue.add(node)

dst = 'Kevin Bacon'
def shortest_path(src):
    parent = Graph({'name':src, 'movie': None, 'Bacon': 0}) 
    queue = [parent]

    visited = set([])

    path = []
    while len(queue) > 0:
        currentActor = queue.pop(0)
        if currentActor.node['movie']:
            path.append(currentActor)
        if currentActor.node['name'] == dst:
            return path
        for actor in graph[currentActor.node['name']]:
            if ((actor['name'], actor['movie']) not in visited):
                visited.add((actor['name'], actor['movie']))
                actor['Bacon'] = currentActor.node['Bacon'] + 1
                new_node = Graph(actor)
                new_node.parent = currentActor
                queue.append(new_node)
    return None



ret = shortest_path('Diane Keaton')
if ret:
    root = ret[-1]

    l = []
    while root:
        l.append(root.node)
        root = root.parent

    l.reverse()
    print(f"{l[0]['name']}'s number is {len(l[1:])}")

    for i, entry in enumerate(l):
        k = i + 1
        if (k < len(l)):
            print(f"{entry['name']} appeared in {l[k]['movie']} \
with {l[k]['name']}")

else:
    print('Not present')
