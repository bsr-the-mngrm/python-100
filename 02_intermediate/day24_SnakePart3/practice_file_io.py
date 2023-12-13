# # TASK 1
# file = open("my_text.txt")
# contents = file.read()
# print(contents)
# file.close()

# # TASK 2
# with open("my_text.txt") as file:
#     contents = file.read()
#     print(contents)

# # TASK 3
# with open("my_text.txt", mode="w") as file:
#     new_content = "Next text."
#     file.write(new_content)

# # TASK 4 - Append
# with open("my_text.txt", mode="a") as file:
#     new_content = "\nNext text."
#     file.write(new_content)

# TASK 5
with open("new_text.txt", mode="w") as file:
    new_content = "New text."
    file.write(new_content)

