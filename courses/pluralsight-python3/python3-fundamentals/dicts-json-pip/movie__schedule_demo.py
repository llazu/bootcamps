# Create a movie showtime
current_movies = {
    "The Grinch": "11:00am",
    "Rudolph": "1:00pm",
    'Frosty the Snowman': "3:00pm",
    'Christmas Vacation': "5:00pm"
}

print("We're showing the following movies:")

for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

# prints non if movie key doesn't exist
showtime = current_movies.get(movie)

if showtime:
    print(movie, "is playing at showtime", showtime)
else:
    print("The requested moview isn't playing today")

'''
if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, "is playing at", showtime)
'''