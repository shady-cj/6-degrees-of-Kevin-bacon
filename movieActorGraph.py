from getMovieActors import get_movie_actors
from getMovies import get_movies
from getActors import get_actors


actors = get_actors()
movies = get_movies()
movieActors = get_movie_actors()
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

