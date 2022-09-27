import random

new_set = set()

again = "y"
while (again.lower() == "y"):
    ingredient = input('Enter the ingredient: ')

    if (random.randint(0, 1) == True):
        print('Ingredient is available')
        new_set.add(ingredient)
        if (ingredient.lower() == 'salt'):
            print('Taste')
        elif (ingredient.lower() == 'butter' or ingredient.lower() == 'grain'):
            print('Mix\nTaste')
    else:
        print('Ingredient is unavailable')

    again = input("Next ingredient (yes/no): ")

print(*new_set)
