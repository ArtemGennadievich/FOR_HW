def decorator_for_user(text):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f'{text}'.center(50, '='))
            out = func(*args, **kwargs)
            print('=' * 50)
            return out

        return wrap

    return wrapper


class UserMovieShow:
    @decorator_for_user("Ввод пользовательских данных")
    def return_answer_at_user(self):
        print('Действия с фильмами:')
        print('1 - добавление фильма'
              '\n2 - каталог фильмов'
              '\n3 - просмотр определенного фильма'
              '\n4 - удаление фильма'
              '\nq - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        return user_answer

    @decorator_for_user('Добавление фильма')
    def user_add_movie(self):
        movie_dict = {
            "название": None,
            "жанр": None,
            "режисера": None,
            "год выпуска": None,
            "длительность": None,
            "студию": None,
            "актеров": None,
        }
        for keys in movie_dict:
            movie_dict[keys] = input(f'Введите {keys} фильма')
        return movie_dict

    @decorator_for_user('Каталог фильмов')
    def show_catalog_movies_user(self, dict_movie):
        for num, value in enumerate(dict_movie, 1):
            print(f'{num}: {value}')

    @decorator_for_user('Ввод названия фильма')
    def search_movie_user(self):
        movie = input('Введите название фильма ')
        return movie

    @decorator_for_user('Данные о фильме')
    def show_search_user(self, movie):
        for key in movie:
            print(f'{key} фильма - {movie[key]}')

    @decorator_for_user("Ошибка")
    def show_error_for_user(self, movie):
        print(f'{movie} не найден')

    @decorator_for_user("Удаление фильма")
    def remove_movie_user(self, movie):
        print(f'Фильм {movie} был удален')

    @decorator_for_user('Ошибка')
    def error_num(self, num):
        print(f'Варианта {num} не существует.')




