from datetime import datetime, time


def title(text):
    print(text)
    print()

def get_command(prompt,command_list,error = "Invalid Command") -> str:
    return get_from_list_lower_case(prompt,command_list,error)

def get_from_list_lower_case(prompt,input_list,error)  -> str:
    while (user_input := input(prompt).lower()) not in input_list:
        print(error)
    return user_input

def get_from_list_upper_case(prompt,input_list,error)  -> str:
    while (user_input := input(prompt).upper()) not in input_list:
        print(error)
    return user_input

def get_from_list_title_case(prompt,input_list,error)  -> str:
    while (user_input := input(prompt).title()) not in input_list:
        print(error)
    return user_input

def get_from_list(prompt,input_list,error)  -> str:
    while (user_input := input(prompt)) not in input_list:
        print(error)
    return user_input

def command_menu(command_list,command_descriptions):
    command_num = 0
    for command in command_list:
        print(command+" - "+command_descriptions[command_num])
        command_num += 1

def command_menu_val(command_list,command_descriptions) -> str:
    command_num = 0
    val = ""
    for command in command_list:
        val+= (command + " - " + command_descriptions[command_num] + "\n")
        command_num += 1
    return val

def get_float_in_range(prompt,low_validity,high_validity) -> float:
    while True:
        try:
            while (floatInput := float(input(prompt))) <= low_validity or floatInput > high_validity:
                print("Input must be between " + str(low_validity) + " and " + str(high_validity))
            return floatInput
        except:
            print("Input must be a number")
   

def get_int_in_range(prompt,low_validity,high_validity,accept_low_validity = True,accept_high_validity = True) -> int:
    while True:
        try:
            while ((intInput := int(input(prompt))) < low_validity and accept_low_validity) or (
                    not accept_low_validity and intInput <= low_validity) or (
                    accept_high_validity and intInput > high_validity) or (
                    not accept_high_validity and intInput >= high_validity):
                print("Input must be between " + str(low_validity) + " and " + str(high_validity))
            return intInput
        except:
            print("Input must be an integer")

def get_float_min(prompt,low_validity,accept_equal_low_validity = False) -> float:
    while True:
        try:
            if accept_equal_low_validity:
                while (floatInput := float(input(prompt))) <= low_validity:
                    print("Input must be greater than " + str(low_validity))
            else:
                while (floatInput := float(input(prompt))) < low_validity:
                    print("Input must be greater than or equal to " + str(low_validity))
            return floatInput
        except:
            print("Input must be a number")
    

def get_int_min(prompt,low_validity,accept_low_validity = True) -> int:
    while True:
        try:
            if accept_low_validity:
                while (intInput := int(input(prompt))) < low_validity:
                    print("Input must be greater or equal to " + str(low_validity))
            else:
                while (intInput := int(input(prompt))) <= low_validity:
                    print("Input must be greater than " + str(low_validity))
            return intInput
        except:
            print("Input must be an integer")

def get_float(prompt) -> float:
    while (True):
        try: 
            return float(input(prompt))
        except:
            print("Input must be a number")

def get_int(prompt) -> int:
    while (True):
        try:  
            return int(input(prompt))
        except:
            print("Input must be a integer")

"""def main():
    get_float_in_range("Number from 1-10:",1,10)
    get_int_in_range("Integer from 1-10:",1,10)
    
if __name__ == "__main__":
    main()"""


def get_day_in_month(prompt, month) -> int:
    """Sets a default for most months"""
    max_day = 31
    """Sets the number of days for the other months"""
    match month:
        case 2:
            max_day = 28
        case 4,6,9,11:
            max_day = 30
    """Prompts the user for the correct value"""
    return get_int_in_range(prompt, 1, max_day)

def get_date(prompt,format) -> datetime:
    while True:
        try:
            return datetime.strptime(input(prompt),format).date()
        except:
            print("Invalid date")

def get_time(prompt,format) -> time:
    while True:
        try:
            return datetime.strptime(input(prompt),format).time()
        except:
            print("Invalid time")



"""def get_csv_file(prompt, excluded_files=None):
    if excluded_files is None:
        excluded_files = []
    while True:
        try:
            if (file_input := input(prompt)) not in excluded_files:
                return file_input, file_io.read_csv(file_input)
            else:
                "File already imported"
        except:
            print("Input must be a csv file present in the source directory")"""