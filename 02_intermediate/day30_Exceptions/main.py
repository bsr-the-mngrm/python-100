
if __name__ == '__main__':
    # FileNotFound
    try:
        file = open(".data/b_file.txt", mode="r")

        # KeyError
        a_dictionary = {"key": "value"}
        value = a_dictionary["key"]
    except FileNotFoundError:
        with open(".data/b_file.txt", mode="a") as file:
            file.write("Something")
    except KeyError as error_message:
        print(f"The key {error_message} key does not exist.")
    else:
        content = file.read()
        print(content)
    finally:
        file.close()

    # # IndexError
    # fruit_list = ["Apple", "Banana", "Pear"]
    # fruit = fruit_list[3]

    # # TypeError
    # text = "abc"
    # print(text + 3)
