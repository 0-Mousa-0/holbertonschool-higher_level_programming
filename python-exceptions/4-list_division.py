#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divList = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by {} ".format(my_list_2[i]))
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0

        finally:
            divList.append(result)
    return divList
