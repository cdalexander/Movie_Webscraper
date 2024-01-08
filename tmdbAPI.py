import tmdbsimple as tmdb
tmdb.API_KEY = "5a330ea7587262d2dc96af73e6ce3d8e"
tmdb.REQUESTS_TIMEOUT = 5  # seconds, for both connect and read


class MovieData:
    def __init__(self) -> None:
        pass

    def getMovie(self, title) -> int:
        myMovie = title
        search = tmdb.Search()
        response = search.movie(query = myMovie)
        for s in search.results:
            title = s['title']
            id = s['id']
            print("Title: " + title)
            print('Movie id: ' + str(id))
            return id


    def getMovieBudget(self, id):
        movie_id = id
        movie = tmdb.Movies(movie_id)
        response = movie.info()
        movie_budget = movie.budget
        print("Budget: $" + str(movie_budget))
        return movie_budget


    # def printStuff(self, id, budget):
    #     print(str(id))
    #     print(str(budget))

# movieSelection = getMovie()
# returnID, returnBudget = getMovieBudget(movieSelection)
# printStuff(returnID, returnBudget)





