from view import UserMovieShow
from model import MovieModel


class Controller:
    def __init__(self):
        self.user_movie = UserMovieShow()
        self.movie_model = MovieModel()

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_movie.return_answer_at_user()
            self.check_user_answer(answer)

    def check_user_answer(self, num):
        if num == '1':
            movie = self.user_movie.user_add_movie()
            self.movie_model.model_add_movie(movie)

        elif num == '2':
            movie = self.movie_model.show_catalog_movies_model()
            self.user_movie.show_catalog_movies_user(movie)

        elif num == '3':
            movie = self.user_movie.search_movie_user()
            try:
                movie_user = self.movie_model.search_movie_model(movie)
            except KeyError:
                self.user_movie.show_error_for_user(movie)
            else:
                self.user_movie.show_search_user(movie_user)

        elif num == '4':
            movie = self.user_movie.search_movie_user()
            try:
                movie_user = self.movie_model.remove_movie_model(movie)
            except KeyError:
                self.user_movie.show_error_for_user(movie)
            else:
                self.user_movie.remove_movie_user(movie_user)

        elif num == 'q':
            self.movie_model.save_data()
        else:
            self.user_movie.error_num(num)

