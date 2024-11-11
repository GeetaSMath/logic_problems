stack = []


def push_element():
    if len(stack) == n:
        print("stack limit is full")
    else:
        element = input("enter the input")
        stack.append(element)
        print(stack)


def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e = stack.pop()
        print("remove the stack", e)
        print(stack)


def quite():
    print("end the operation")


n = int(input("enter the stack limit"))
while True:
    print("enter the operation you want to perform 1.push 2.pop 3.quite")
    choice = int(input())
    if choice == 1:
        push_element()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break;
    else:
        print("enter the correct choice")

stack = []
#
#
# def push():
#     element = input("Enter the element to push: ")
#     stack.append(element)
#     print("Stack after push:", stack)
#
#
# def pop():
#     if stack:
#         e = stack.pop()
#         print("Popped element:", e)
#         print("Stack after pop:", stack)
#     else:
#         print("Stack is empty, nothing to pop.")
#
#
# def quit():
#     print("Ending the operation.")
#
#
# while True:
#     print("\nChoose the operation you want to perform:")
#     print("1. Push")
#     print("2. Pop")
#     print("3. Quit")
#
#     try:
#         choice = int(input("Enter your choice (1/2/3): "))
#
#         if choice == 1:
#             push()
#         elif choice == 2:
#             pop()
#         elif choice == 3:
#             quit()
#             break  # Exit the loop
#         else:
#             print("Please enter a valid choice (1, 2, or 3).")
#     except ValueError:
#         print("Invalid input. Please enter a number (1, 2, or 3).")

# import requests
#
# url="https://www.hyrtutorials.com/p/add-padding-to-containers.html"
# get_data=requests.get(url)
# print(get_data.text)
# xpath_email_text="//label[text()='Email']/following-sibling::input[1]"
# xpath="//label[text()='Email']/following-sibling::input[1]"
