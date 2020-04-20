import random


class Movie:
    def __init__(self, title, nation):
        self.title = title
        self.nation = nation
        self.audiences = []

    def __repr__(self):
        return f'Movie(title={self.title}, nation={self.nation})'


class MovieDatabase:
    def __init__(self):
        self.database = []

    def find_movie(self, title):
        for movie in self.database:
            if title == movie.title:
                return movie
        else:
            return None

    def add_audiences(self, title, num):
        movie = self.find_movie(title)
        movie.audiences.append(num)

    def find_movies_by_nation(self, nation):
        return [movie for movie in self.database
                if nation == movie.nation]

    def get_cum_audiences(self, title):
        movie = self.find_movie(title)
        return sum(movie.audiences)

    def sort_by_audiences(self):
        self.database.sort(key=lambda x: sum(x.audiences), reverse=True)


if __name__ == '__main__':
    movie_list = MovieDatabase()
    movie_list.database.append(Movie('1917', 'other'))
    movie_list.database.append(Movie('지푸라기라도잡고싶은짐승들', 'kor'))
    movie_list.database.append(Movie('주디', 'other'))
    movie_list.database.append(Movie('사냥의시간', 'kor'))
    movie_list.database.append(Movie('인비저블맨', 'other'))

    kor_movies = movie_list.find_movies_by_nation('other')
    print(kor_movies)

    for _ in range(5):
        movie_list.add_audiences('1917', random.randint(1, 10))
        movie_list.add_audiences('사냥의시간', random.randint(1, 10))

    print(movie_list.find_movie('1917').audiences)
    print(movie_list.get_cum_audiences('1917'))
    print(movie_list.find_movie('사냥의시간').audiences)
    print(movie_list.get_cum_audiences('사냥의시간'))

    movie_list.sort_by_audiences()
    print(movie_list.database)



