# You have a list of your favorite marvel super heroes.
# spider man, thor, hulk, iron man, captain america
# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heroes list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

# Solution:
heroes = ["spider man", "thor", "hulk", "iron man", "captain america"]

# answer #1:
answer_1 = len(heroes)
print("length of list:", answer_1)

# answer #2:
heroes.append("black panther")
print("Add 'black panther' at the end of this list:", heroes)

# answer #3:
heroes.remove("black panther")
heroes.insert(3, "black panther")
print("remove black panther and add 'black panther' after 'hulk':", heroes)

# answer #4:
heroes[1:3] = ["dr strange"]
print("remove thor and hulk from list and replace them with doctor strange:", heroes)

# answer #5:
heroes.sort()
print("Sort the heroes list in alphabetical order:", heroes)
