import functools
from functools import total_ordering


@total_ordering
class GFG:
    print("inside class")

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, obj):
        return self.b < obj.b

    def __gt__(self, obj):
        return self.b > obj.b

    def __le__(self, obj):
        return self.b <= obj.b

    def __ge__(self, obj):
        return self.b >= obj.b

    def __eq__(self, obj):
        return self.b == obj.b

    def __repr__(self):
        return str((self.a, self.b))

    # list of objects


gfg = [GFG("geeks", 1),
       GFG("computer", 3),
       GFG("for", 2),
       GFG("geeks", 4),
       GFG("science", 3)]

# before sorting
print(gfg)

# sorting objects on the basis of value
# stored at variable b
# after sorting
print(sorted(gfg))