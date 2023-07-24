from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def get_rating(movie: dict) -> float:
            # print(len(movie.get('country', [])) >= 2)
            if movie['rating_kinopoisk'] != '0' and movie['rating_kinopoisk'] != ''\
                    and len(movie.get('country', [])) > 1 \
                    and (movie['rating_kinopoisk'] != ''):
                return float(movie['rating_kinopoisk'])

        ratings = list(filter(lambda x: x is not None, map(get_rating, list_of_movies)))
        # ratings = list(map(lambda x: x is not None, map(get_rating, list_of_movies)))
        if ratings:
            return sum(ratings) / len(ratings)
        else:
            return 0

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """
        movie_list = list(filter(lambda movie: movie["rating_kinopoisk"]
                                               and float(movie["rating_kinopoisk"]) >= rating, list_of_movies))
        filtered_list = list(map(lambda movie: movie["name"], movie_list))
        count = 0
        for movie in filtered_list:
            count += movie.count("и")

        return count
