def movie_organizer(*movies):
    owned_movie_db = {}
    for movie in movies:    # movie = (movie_name, genre)
        movie_name, genre = movie[0], movie[1]
        if genre in owned_movie_db:
            owned_movie_db[genre].append(movie_name)
        else:
            owned_movie_db[genre] = []
            owned_movie_db[genre].append(movie_name)

    owned_movie_db = sorted(owned_movie_db.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for genre, movie_name in owned_movie_db:
        sorted_movies = sorted(movie_name)
        result += f'{genre} - {len(sorted_movies)}\n'
        for name in sorted_movies:
            result += f'* {name}\n'
    return result

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))