#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    r_list = []
    for i in range(list_length):
        try:
            r = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            r = 0
            print("division by 0")
        except IndexError:
            r = 0
            print("out of range")
        except TypeError:
            r = 0
            print("wrong type")
        finally:
            r_list.append(r)
    return r_list
