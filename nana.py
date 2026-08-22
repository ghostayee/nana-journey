calculator_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return (
            f"{num_of_days} days are {num_of_days * calculator_to_units} {name_of_unit}"
        )
    elif num_of_days == 0:
        return "you have entered zero enter a valid number"
    else:
        return "you have entered a negative value no calculation for you"


my_var = days_to_units(56)
print(my_var)

user_input = input(
    "Hey user Enter the number of days and i will convert it to hours: \n"
)
user_input_number = int(user_input)
calculated_value = days_to_units(user_input_number)
print(calculated_value)
