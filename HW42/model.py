import os.path
import pickle


class MovieData:
    def __init__(self, name_movie, genre, producer, issue, duration, studio, actor):
        self.name_movie = name_movie
        self.genre = genre
        self.producer = producer
        self.issue = issue
        self.duration = duration
        self.studio = studio
        self.actor = actor

    def __str__(self):
        return f'Название фильма: {self.name_movie}. Жанр: {self.genre}. Режисер: {self.producer}'


class MovieModel:
    def __init__(self):
        self.text = 'text.csv'
        self.dict_model = self.load_data()

    def model_add_movie(self, keys):
        movie = MovieData(*keys.values())
        self.dict_model[movie.name_movie] = movie

    def show_catalog_movies_model(self):
        return self.dict_model.values()

    def search_movie_model(self, movie_user):
        movie = self.dict_model[movie_user]
        movie_dict = {
            "название": movie.name_movie,
            "жанр": movie.genre,
            "режисера": movie.producer,
            "год выпуска": movie.issue,
            "длительность": movie.duration,
            "студию": movie.studio,
            "актеров": movie.actor,
        }
        return movie_dict

    def remove_movie_model(self, movie):
        return self.dict_model.pop(movie)

    def save_data(self):
        with open(self.text,'wb') as f:
            pickle.dump(self.dict_model, f)

    def load_data(self):
        if os.path.exists(self.text):
            with open(self.text, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()
