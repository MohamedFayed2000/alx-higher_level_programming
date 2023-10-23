#!/usr/bin/python3
def safe_print_list(my_list=[1, 2, 3, 4, 5], x=0):
    total = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            total += 1
        except IndexError:
            break
    print()
    return(total)
