if __name__ == '__main__':

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

    height = float(input("Height: "))
    weight = int(input("Weight: "))

    if height > 3:
        raise ValueError("Human height should not be over 3 meters.")

    bmi = weight / height**2
    print(bmi)

    # # IndexError
    # fruit_list = ["Apple", "Banana", "Pear"]
    # fruit = fruit_list[3]

    # # TypeError
    # text = "abc"
    # print(text + 3)
