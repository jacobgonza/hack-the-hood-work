food_price = {
    "chicken" :1.59, 
    "beef" :1.99, 
    "cheese" :1.00,
    "milk" :2.50}
print(food_price)
hth_age = {
    "jacob" :17,
    "victor" :23,
    "kevin" :18,
    "leyan" :18} 
print(hth_age)


chicken = food_price["chicken"]
beef = food_price["beef"]
cheese = food_price["cheese"]
milk = food_price["milk"]


jacob = hth_age["jacob"]
victor = hth_age["victor"]
kevin = hth_age["kevin"]
leyan = hth_age["leyan"]
hth_age["jacob"] = 18 

print(hth_age)

shoes_stock = {
    "Jordan 13" :1,
    "Yeezy" :8,
    "Foamposite" :10,
    "Air Max" :5,
    "SB Dunk" :20}
print(shoes_stock)

shoes_stock["SB Dunk"] -= 2
shoes_stock["Yeezy"] += 1
shoes_stock["Air Max"] += 7
shoes_stock["SB Dunk"] += 7
shoes_stock["Jordan 13"] += 7
shoes_stock["Foamposite"] += 7
shoes_stock["Yeezy"] += 7
shoes_stock["Air Max"] -= 3
shoes_stock["SB Dunk"] -= 3
shoes_stock["Jordan 13"] -= 3
shoes_stock["Foamposite"] -= 3
shoes_stock["Yeezy"] -= 3
print(shoes_stock)

shoes_stock["Air Forces"] = 12
shoes_stock["Vans"] = 30
shoes_stock["Convers"] = 16
print(shoes_stock)

del shoes_stock["Foamposite"]
del shoes_stock["Convers"]
del hth_age["jacob"]
del hth_age["kevin"]
print(hth_age)
print(shoes_stock)