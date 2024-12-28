#count the number  of list untile find the tuple
def count(lst):
    counter = 0
    for num in lst:
        if isinstance(num, tuple):
            break
        counter = counter + 1
    return counter


lst = [1, 2, 3, 4, 5, (2, 3, 4), 5, 6]
print(count(lst))














