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
