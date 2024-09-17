# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

# method 1 list comprehension
x = int(input("Enter the max number for this list:"))
x_list = [num for num in range(1, x + 1) if num % 2 != 0]
print(x_list)

# method 2 for loop
y = int(input("Enter the max number for this list:"))
y_list = []

for i in range(1, y + 1):
    if i % 2 == 1:
        y_list.append(i)
print(y_list)
