calculator_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculator_to_units} {name_of_unit}"


def validate_execute():
    try:

        if user_input.isdigit():
            user_input_number = int(user_input)
            if user_input_number > 0:
                calculated_value = days_to_units(user_input_number)
                print(calculated_value)
            elif user_input_number == 0:
                return "you have entered zero no calculation for you"
            else:
                print("you have entered a negative number no calculation for you ")
        else:
            return "invalid number do not ruin my programme"
    except ValueError:
        print("your number is not valid ")


user_input = input(
    "Hey user Enter the number of days and i will convert it to hours: \n"
)
validate_execute()
