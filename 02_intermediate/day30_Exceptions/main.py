if __name__ == '__main__':
    # # TASK1
    # try:
    #     # FileNotFound
    #     file = open(".data/b_file.txt", mode="r")
    #
    #     # KeyError
    #     a_dictionary = {"key": "value"}
    #     value = a_dictionary["key"]
    # except FileNotFoundError:
    #     with open(".data/b_file.txt", mode="a") as file:
    #         file.write("Something")
    # except KeyError as error_message:
    #     print(f"The key {error_message} key does not exist.")
    # else:
    #     content = file.read()
    #     print(content)
    # finally:
    #     file.close()
    #     raise TypeError("This is an error that I made up.")

    # # TASK 2
    # height = float(input("Height: "))
    # weight = int(input("Weight: "))
    #
    # if height > 3:
    #     raise ValueError("Human height should not be over 3 meters.")
    #
    # bmi = weight / height**2
    # print(bmi)

    # # TASK3 - IndexError
    # fruits = ["Apple", "Pear", "Orange"]
    #
    # # 🚨 Do not change the code above
    #
    # # TODO: Catch the exception and make sure the code runs without crashing.
    # def make_pie(index):
    #     try:
    #         fruit = fruits[index]
    #         print(fruit + " pie")
    #     except IndexError:
    #         print("Fruit pie")
    #
    #
    # # 🚨 Do not change the code below
    # make_pie(4)

    # # TypeError
    # text = "abc"
    # print(text + 3)
