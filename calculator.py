"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )                               # imports arithmetic functions


calc_dict = {"+": add, "-": subtract, "*": multiply, "/": divide, "square": square, "cube": cube, "pow": power, "mod": mod}
# defines a dictionary linking calculator commands to arithmetic function calls 

def operation(user_string):
    """ takes user string, executes calculation, and prints result """
    input_list = user_string.split()                                # splits user string into separate strings
    command = input_list[0]                                         # identifies first string as command
        
    if command in calc_dict:                                        # checks to see if commands are valid
        if len(input_list) == 2:                                    # separately handles squares and cubes, which take one value
            try:
                num1 = float(input_list[1])                         # converts first value to a float, vs string
                print(calc_dict[command].__call__(num1))            # uses dictionary to call function based on command, passing value num1 as an argument
            except:
                print("Entry not expected. Please try again.")      # in case of unexpected value, i.e. cube with two values
        elif len(input_list) == 3:                                  # for remainder of commands besides squares and cubes                
            try:
                num1 = float(input_list[1])                         # establishes values as floats
                num2 = float(input_list[2])
                print(calc_dict[command].__call__(num1, num2))      # then uses dictionary to call function based on command, passing values num1 and num2 as arguments
            except:
                print("Entry not expected. Please try again.")      # error message in case of unexpected value
    else:
        print("Error: Command is beyond the scope of this calculator's humble abilities.")          # if user enters anything besides valid command

while (True):                                                       # sets up infinite loop
    user_math = input("> ")                                         # prints > and takes in user's input
    if user_math.startswith("q") == True:                           # checks if entry is q
        break                                                       # if so, quits
    else:
        operation(user_math)                                        # if not, perform calculator operation
    
