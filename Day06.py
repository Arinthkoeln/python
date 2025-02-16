#FOR LOOPS
movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]
"""movie = movies[0]
print(f"movie {movie[0]} ({movie[2]})  directed by ({movie[1]})")

movie = movies[1]
print(f"movie {movie[0]} ({movie[2]})  directed by ({movie[1]})")

movie = movies[2]
print(f"movie {movie[0]} ({movie[2]})  directed by ({movie[1]})")

for movie in movies:
    print(f"{movie[0]} ({movie[2]})  directed by ({movie[1]})")
    #The break statement
    if movie [1]== "Christopher Nolan":
        print(" I found Christopher Nolan")
        break"""

#The range function        
range(10)   #1,.....9
range(3,10) #3...9
range(0,10,2)  #2, 4,6,8
range(0,10,3)#3,6,9
range(10, 0, -1)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

#print(range(0, 10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

number =list(range(10)) # list in range
print(number)

number1 = tuple(range(10)) #list in tuble
print(number1)

#list in for loop
#Style note
for _ in range(5): 
    print("Welcome")
    
    



    
    