from random import *

def random_color():
    b = ""
    for i in range(6):
        a = choice(["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        b += a
    return f"#{b}"

