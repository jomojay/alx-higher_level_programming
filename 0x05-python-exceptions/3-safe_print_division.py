#!/usr/bin/python3
def safe_print_division(a, b):
    result = None 
    try:
        try:
            result = a / b
        except Exception:
            return (None)
        else:
            return (result)
    finally:
        print("Inside result: {}".format(result))
