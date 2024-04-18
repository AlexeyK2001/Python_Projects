def add(n1,n2): 
    return n1+n2 
 
def subtract(n1,n2): 
    return n1-n2 
 
def multiply(n1,n2): 
    return n1*n2 
 
def divide(n1,n2): 
    return n1/n2 
 
operations = { 
        "+": add, 
        "-": subtract, 
        "*": multiply, 
        "/": divide 
        } 
  
num1 = int(input("What is the first number? ")) 
 
for symbol in operations: 
    print(symbol) 
operation_symbol = input("Pick an operation symbol from the lines above ") 
 
num2 = int(input("What is the second number? ")) 
calculation_function = operations[operation_symbol] 
answer = calculation_function(num1, num2) 
print(f"{num1} {operation_symbol} {num2} = {answer}") 
 
next = True 
while next == True: 
    more = input(f"Type 'y' to continue calculation with {answer}, or 'n' to exit: ").lower() 
    if more != "y": 
        next = False 

    operation_symbol = input("Pick an operation: ") 
    num3 = int(input("What's the next number? ")) 
    calculation_function = operations[operation_symbol] 
    next_answer = calculation_function(answer, num3) 
    print(f"{answer} {operation_symbol} {num3} = {next_answer}") 
    answer = next_answer

# Гайз, підкажіть, чому при введенні more != "y" без else програма продовжувала виконуватися і запрошувала Pick an operation:. Я ж наче присвоюю змінній next значення False, і очікую, що цикл while зупиниться, а він не зупинявся. Лише додавши else, все запрацювало
