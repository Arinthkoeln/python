
movies = [
    ("The Room", "Tommy Wiseau", "2003", "$6,000,000")
]

title = input("enter the movie title name:")
director_name = input("enter the director name:")
release_year = input("enter release year:")
budget= input("enter the budget ammount:")

new_movie = title,director_name,release_year,budget

print(f"{(new_movie[0])} {(new_movie[2])}")
#append movie
movies.append(new_movie)
#delete movies
#del movies[0]
#movies.pop(0)
movies.remove(movies[0])
print(movies)






