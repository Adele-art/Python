# DATA STRUCTURES IN PYTHON
# 1.Lists
# 2.Tuples
# 3. Dictionaries

# 1.Lists
# mutable-can add or remove items anytime
# can have lengths
# can be of different data types

list1 = [1,2,3,4,5,6]
print(list1)


# indexing in lists
# retrieving an item by referring to its offset

list1 = [1,2,3,4,5,6]
print(list1[3])
print(list1[1])
print(list1[0])
print(list1[5])
print(list1[4])

# negative indexing-right to left
print(list1[-1])
print(list1[-2])

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(days)
print(days[-1])
weekend = ["Saturday","Sunday"]
print(weekend)

print(days[5:7])
print(days[5:6])
print(days[5:1])
print(days[0:3])
print(days[:3])

print(type(list1))

# Functions
# 1. .append
list1.append(7)
print(list1)
print(list1.index(7))
list1.pop()
print(list1)
list1[5]=2020
print(list1)
list1[3]=[]
print(list1)
print(list1[3])

# Nesting-having something within itself
list2=[1,2,[3,4[5,6,[7,8]]]]
print(len(list2))
print(list2[2][2][0])



# 2. TUPLES
#immutable

months=("Jan","Feb","Mar","Apr")
print(months[2])
# months.append("Jul")
print(months)
print(len(months))

test = (1,2,3,[4,5,6])
print(test[3])
test[3][1]=7
print(test)
print(test[3])
print(test[3])
