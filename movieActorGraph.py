from getMovieActors import movieActors
from getMovies import movies
from getActors import actors

print(movies)
print()
print(actors)
print()
print(movieActors)

graph = {}
for k, v in movieActors.items():
    movieName = movies[k]
    for actor_id in v:
        actor_name = actors[actor_id]
        for rel_actor_id in v:
            if rel_actor_id == actor_id:
                continue
            rel_actor_name = actors[rel_actor_id]
            graph[actor_name] = graph.get(actor_name, []) +\
                    [{"name": rel_actor_name, "movie": movieName}]
print("\n")
print("GRAPH\n")

for k, v in graph.items():
    print(f"{k}: {v}")
    print() 
