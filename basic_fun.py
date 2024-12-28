#python function is user to organize the code and reuse code
def odd_even(num):
    if num % 2 == 0:
        print("number is even")
    else:
        print("number is odd")


odd_even(25)


#function multiple params

def add_num(a, b):
    return a + b


add_result = add_num(2, 4)
print(add_result)


def greeting_card(name="guest"):
    print(f"hi good morning {name}")


greeting_card("geeta")

#args for positional arguments
#kwargs for key and value arguments

#positional arguments

def print_val(*args):
    for val in args:
        print(f"{val}")


print_val(1,3,4,5,6,7,8,"geeta")

def print_val_key(**kargs):
    for key,value in kargs.items():
        print(f"{key}:{value}")


print_val_key(name="geeta")


def print_positional_keyval(*args,**kwargs):
    for num in args:
        print(f"positional items {num}")
    for key,val in kwargs.items():
        print(f"key value data are {key}:{val}")


print_positional_keyval(2,4,5,6,7,'geeta',name="geeta",age="25")



