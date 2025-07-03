def print_till_9(num):
    if num >= 9:
        return num + 1
    # recursion
    print(num + 1)
    return print_till_9(num + 1)

next_val = print_till_9(5)
print(next_val)

def print_till_9_loop(num = 0):
    while(num < 9):
        num += 1
        print(num)
    else:
        return num + 1

next_val = print_till_9_loop(5)
print(next_val)