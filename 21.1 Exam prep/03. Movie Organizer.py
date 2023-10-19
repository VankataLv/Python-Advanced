def movie_organizer(*args):
    db = {}
    for el in args:
        name = el[0]
        genre = el[1]
        if genre in db.keys():
            db[genre].append(name)
        else:
            db[genre] = [name, ]
    db = dict(sorted(db.items(), key=lambda x: (-len(x[1]), x[0])))
    for movies in db.values():
        movies = movies.sort()

    result = ""
    for key, value in db.items():
        result += f"{key} - {len(value)}\n"
        for el in value:
            result += f"* {el}\n"

    return result



# print(movie_organizer(
#     ("The Godfather", "Drama"),
#     ("The Hangover", "Comedy"),
#     ("The Shawshank Redemption", "Drama"),
#     ("The Pursuit of Happiness", "Drama"),
#     ("The Hangover Part II", "Comedy")))

# print(movie_organizer(
#     ("Avatar: The Way of Water", "Action"),
#     ("House Of Gucci", "Drama"),
#     ("Top Gun", "Action"),
#     ("Ted", "Comedy"),
#     ("Duck Soup", "Comedy"),
#     ("The Dark Knight", "Action"),
#     ("A Star Is Born", "Musicals"),
#     ("The Warrior", "Action"),
#     ("Like A Boss", "Comedy"),
#     ("The Green Mile", "Drama"),
#     ("21 Jump Street", "Comedy")))

# print(movie_organizer(
#     ("The Matrix", "Sci-fi")))