import math

while True:
    print("\n----Python Calculator ----")
    print(" Operators: +  -  *  /  **  %  sqrt ")

    number1 = float(input("Enter first number: "))
    operator = input("Enter operator: ")

    if operator.lower() == "sqrt":
        if number1 < 0:
            result = "Error! Cannot take sqrt of a negative number."
        else:
            result = math.sqrt(number1)
    else:
        number2 = float(input("Enter second number: "))

        if operator == "+":
            result = number1 + number2
        elif operator == "-":
            result = number1 - number2
        elif operator == "*":
            result = number1 * number2
        elif operator == "/":
            if number2 == 0:
                result = "Error! Cannot divide by zero."
            else:
                result = number1 / number2
        elif operator == "**":
            result = number1 ** number2
        elif operator == "%":
            result = number1 % number2
        else:
            result = "Invalid operator!"

    print("Answer:", result)

    choice = input("Would you like to perform a new calculation ?  (yes/no): " )
    if choice.lower() == "no":
        print(" Bye! See you next time.... ")
        break