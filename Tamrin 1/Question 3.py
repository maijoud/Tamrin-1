def calculator ():
    print ("Welcome to the Simple Calculator")
    print ("Available operations:")
    print ("sum - Addition")
    print ("difference - Subtraction")
    print ("multiple - Multiplication")
    print ("divide - Division")

    operation = input ("Enter operation: ").strip ().lower ()


    try:
        num1 = float (input ("Enter first number: "))
        num2 = float (input ("Enter second number: "))
    except ValueError:
        print ("Invalid input. Please enter numeric values.")
        return

    if operation == "sum":
        result = num1 + num2
        print ("Result:", result)
    elif operation == "difference":
        result = num1 - num2
        print ("Result:", result)
    elif operation == "multiple":
        result = num1 * num2
        print ("Result:", result)
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
            print ("Result:", result)
        else:
            print ("Error: Cannot divide by zero.")
    else:
        print ("Invalid operation. Please choose one of the available operations.")

calculator ()
