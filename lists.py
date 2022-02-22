lenght = int(input("Enter length: "))

drinks = ["coffe", "soda", "tea", "juice", "lemonade"]
dinner = ["pizza", "roll", "hotdog", "hamburger", "sandwich"]
dessert = ["cake", "biscuit", "ice cream", "fruit"]
food = []

i = 0
for n in range(3):
    while i < lenght:
        if n == 0:
            food.append(drinks[i])
        elif n == 1:
            food.append(dinner[i])
        else:
            food.append(dessert[i])

        i += 1
    i = 0

print(food)
