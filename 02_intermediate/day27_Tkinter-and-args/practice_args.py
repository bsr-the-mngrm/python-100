
def add(*args):
    numbers = [num for num in args if isinstance(num, int)]
    return sum(numbers)


def calculate(n, **kwargs):
    print(kwargs, type(kwargs))
    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)


print(add(1, 2, 3, 4, "text"))
calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan" """, model="GT-R" """)
print(my_car.model)
