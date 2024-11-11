#count the number of list until an element is a tuple
import trace

# Create a tracer that will print trace information
tracer = trace.Trace(count=False, trace=True)

# Define the function you want to trace
def count(li):
    counter = 0
    for num in li:
        if isinstance(num, tuple):
            break
        counter += 1
    return counter

li = [4, 5, 6, 10, (1, 2, 3), 11, 2, 4]

# Use the tracer to run the function
tracer.run('print(count(li))')


# initializing native types
test_int = 5
test_list = [1, 2, 3]

# testing with isinstance
print(isinstance(test_int, int))
print(isinstance(test_int, str))


