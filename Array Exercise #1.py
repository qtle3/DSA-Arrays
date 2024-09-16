# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list

# Solution:

exp = [2200, 2350, 2600, 2130, 2190]

# answer #1:
answer_1 = exp[1] - exp[0]
print("In Feb this much extra was spent comapared to Jan:", answer_1)

# answer #2:
answer_2 = exp[0] + exp[1] + exp[2]
print("Expense for first quarter:", answer_2)

# answer #3:
for i in range(len(exp)):
    if exp[i] == 2000:
        answer_3 = exp[i]
        print(answer_3)

print("Did I spend exactly $2000 this month?", 2000 in exp)

# answer #4:
exp.append(1980)
print("June expense added:", exp)
