# friends = ["Francis", "Evans", "Ferdinand"]

# # print(friends[0])
# # print(friends[1])   REDUNDANCY!!!
# # print(friends[2])
# # print(friends[3])
# # print(friends[4])

# for name in friends:
#     print(name + " is my friend.")
#     print(name + " cannot be my friend.")


# fav_numbers = [2, 7, 10, 11, 9]

# for num in fav_numbers:
#     print(num * 2)

local_govt = ["Awka South", "Awka North", "Anaocha", "Aguata", "Abagana"]

for govt in local_govt:
    print(govt + ", Anambra state")

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square_of_num = []
# square_of_num_reversed = []

# for n in num:
#     square = n ** 2
#     square_of_num.append(square)

# for n in num:
#     square = n ** 2
#     square_of_num_reversed.insert(0, square)

# print("num:", num)
# print("Square of num:", square_of_num)
# print("Square of num inversed:", square_of_num_reversed)

numbers = []
square_numbers = []
square_numbers_reverse = []

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
numbers.append(6)
numbers.append(7)
numbers.append(8)
numbers.append(9)
numbers.append(10)

for n in numbers:
    square_numbers.append(n ** 2)

for n in numbers:
    square_numbers_reverse.insert(0, n ** 2)

print(numbers)
print(square_numbers)
print(square_numbers_reverse)

print(str(numbers[7]) + " is an integer")