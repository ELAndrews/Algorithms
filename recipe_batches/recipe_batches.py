#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    count = math.inf
    if set(recipe.keys()) == set(ingredients.keys()):
        r = list(recipe.values())
        m = list(ingredients.values())
        if len(r) == 1 and len(m) == 1:
            count = math.floor(m[0] / r[0])
        else:
            for i in range(len(r) - 1):
                if m[i] / r[i] < count:
                    count = math.floor(m[i] / r[i])
    else:
        count = 0
    return count


# print(recipe_batches({'milk': 2, 'sugar': 40, 'butter': 20}, {
#       'milk': 5, 'sugar': 120, 'butter': 500}))

# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
