from art import logo

# Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for op in operations:
        print(op)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))

        function = operations[operation_symbol]
        answer = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

    # my way worked, not quite as clean though.
    # while input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == 'y':
    #     operation_symbol = input("Pick an operation: ")
    #     next_num = int(input("What's the next number?: "))
    #     function = operations[operation_symbol]
    #     next_answer = function(answer, next_num)
    #     print(f"{answer} {operation_symbol} {next_num} = {next_answer}")
    #     answer = next_answer
calculator()