# # TASK1
# numbers = [1, 2, 3]
# new_list = [n+1 for n in numbers]
# print(new_list)

# # TASK2
# name = "Angela"
# new_list = [letter.capitalize() for letter in name]
# print(new_list)

# # TASK3
# new_list = [num*2 for num in range(1, 5)]
# print(new_list)

# # TASK4
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# # TASK5
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# # TASK6
# with open("csv/file1.txt") as file:
#     file1_list = [int(line.strip()) for line in file.readlines()]
#
# with open("csv/file2.txt") as file:
#     file2_list = [int(line.strip()) for line in file.readlines()]
#
# result = [num for num in file1_list if num in file2_list]
# print(result)
