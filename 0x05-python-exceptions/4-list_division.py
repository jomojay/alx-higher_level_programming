#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            res = (my_list_1[i] / my_list_2[i])
            new.append(res)
        except TypeError:
            new.append(0)
            print("wrong type")
        except ZeroDivisionError:
            new.append(0)
            print("division by 0")
        except IndexError:
            new.append(0)
            print("out of range")
        finally:
            continue
    return new
