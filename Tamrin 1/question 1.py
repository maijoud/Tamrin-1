def determine_type(user_input):

    if user_input.isdigit():
        return int(user_input)

    try:
        float_val = float(user_input)
        return float_val
    except ValueError:
        pass

    if ',' in user_input:
        return user_input.split(',')
    elif ' ' in user_input:
        return user_input.split()

    return user_input

def main():
    user_input = input("Enter something: ")
    result = determine_type(user_input)

    if isinstance(result, int):
        print(f"The input is an integer: {result}")
    elif isinstance(result, float):
        print(f"The input is a float: {result}")
    elif isinstance(result, list):
        print(f"The input is a list: {result}")
        print("List elements:")
        for element in result:
            print(element)
    else:
        print(f"The input is a string: {result}")

if __name__ == "__main__":
    main()
