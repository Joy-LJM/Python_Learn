import art

def add(n1, n2):
    return n1 + n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def subtract(n1, n2):
    return n1 - n2

operation_dictionary={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}


# method 1 two while
# new_conversation=True

# while new_conversation:
#   print(art.logo)
#   continue_conversation=True
#   first_num= float(input("What is the first number?:"))
#   while continue_conversation:
#     for symbol in operation_dictionary:
#         print(symbol)
#     operation=input ("Pick an operation:")
#     second_num= float(input("What is the next number?:"))
#     res=operation_dictionary[operation](first_num,second_num)
#     print(f"{first_num} {operation} {second_num} = {res}")
#     continue_or_not=input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ").lower()
#     if(continue_or_not=='y'):
#         first_num=res
#     else:
#         continue_conversation=False

# method 2 recursion
def calculator():
  print(art.logo)
  continue_conversation=True
  first_num= float(input("What is the first number?:"))
  while continue_conversation:
    for symbol in operation_dictionary:
        print(symbol)
    operation=input ("Pick an operation:")
    second_num= float(input("What is the next number?:"))
    res=operation_dictionary[operation](first_num,second_num)
    print(f"{first_num} {operation} {second_num} = {res}")
    continue_or_not=input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ").lower()
    if(continue_or_not=='y'):
        first_num=res
    else:
        print("\n"*20)
        continue_conversation=False
        calculator()

calculator()