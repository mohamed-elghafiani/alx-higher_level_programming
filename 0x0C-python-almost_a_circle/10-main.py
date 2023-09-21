#!/usr/bin/python3
""" 10-main """
from models.square import Square


def get_writeable_properties(cls):
    return [attr for attr, value in vars(cls).items()
                 if isinstance(value, property) and value.fset is not None]

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)
    
    print(get_writeable_properties(s1))

    
    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
