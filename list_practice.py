us_cities = [ 
    "oakland, ",
    "Atlanta, ", 
    "New York, ", 
    "Seattle, ", 
    "Memphis, ", 
    "Miami, ", 
    "Boston, ", 
    "Los Angles, ", 
    "Denver, ", 
    "New Orleans."]
print(us_cities[0])
print(us_cities[-2])
print(us_cities[6])
print(us_cities[2:5])

us_cities[0] = "San Francisco, "
us_cities[2] = "Brooklyn, "
us_cities[-3] = "Hollywood, "
us_cities[5] = "Tampa, "
print(us_cities)

us_cities.append("Oakland")
us_cities.extend(["New York City", "Los Angeles",])
us_cities.insert(0, "Miami")
print(us_cities)

del us_cities[4]
us_cities.remove("Tampa, ")
us_cities.pop(6)
print(us_cities)

animes =[
    "One Piece, ",
    "Naruto, ",
    "Bleach, ",
    "Neon Genesis Evangelion, ",
    "My Hero Acadamia, ",
    "Fire Force, ",
    "Seven Deadly Sins, ",
    "One Punch Man, ",
    "Demon Slayer, ",
    "Black Clover, ",
    "Attack on Titan."]

