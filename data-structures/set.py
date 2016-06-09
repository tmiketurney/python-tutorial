#!/usr/bin/env python3
#
#  @file    queue.py
#
#  COPYRIGHT:
#
#     Copyright: Tools Made Tough, 2016:
#
#     License:  GPL v2.1
#
#  @author   T.Michael Turney
#  @date     8.June.2016
#  @version  1.01
#

people = set(['John', 'Sue', 'Bill'])
if 'John' in people:
    print("Yes!")
else:
    print("No!")

work_friends = {'Sue', 'Eric', 'Fred'}
work_friends2 = work_friends

print(work_friends)
work_friends.add('Kathy')
print(work_friends)
work_friends.remove('Fred')
print(work_friends)

neighborhood_friends = set(['John', 'Sue', 'Bill'])

print(neighborhood_friends - work_friends2)     # elements in neighborhood but not work (difference)
print(neighborhood_friends | work_friends2)     # all elements in either set (union)
print(neighborhood_friends & work_friends2)     # elements in both sets (intersection)
print(neighborhood_friends ^ work_friends2)     # elements in either, but not both (symmetric_difference)

class recipe:
    name=''
    ingredients = []

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

dish1 = recipe("Omlette", ['Eggs', 'Tomatoes', 'Onions', 'Peppers'])
dish2 = recipe("Bread", ['Flour', 'Yeast'])
dish3 = recipe("Cake", ['Eggs', 'Flour', 'Sugar', 'Butter'])
dishes_to_fix = [dish1, dish2, dish3]

shopping_list = set()
for dish in dishes_to_fix:
    ingredients = set(dish.ingredients)
    shopping_list = shopping_list | ingredients

ingredients_on_hand = {'Onions', 'Butter', 'Milk', 'Honey', 'Oatmeal', 'Sugar', 'Tomatoes'}
shopping_list -= ingredients_on_hand

print("Here is the set of items you need to buy:")
print(shopping_list)
