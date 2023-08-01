def validate_number(msg, max):
    flag = True
    number = 0
    while flag:
        try:
            number = int(input(msg))
            if number < 0:
                print("Number must be greater than 0")
            elif number >= max:
                print("Number must be less than ", max)
            else:
                flag = False
        except:
            print("Please enter a number")
    return number

def validate_number_input(number):
    message = ''
    number = int(number)
    if number < 1:
        message = "number less must be greater than 0"
    elif number > 10:
        message = "number must be less than 10"
    return message