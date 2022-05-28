"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:
    user_input = input("Enter Your Equation >") #makes this able to take input from user
    token = user_input.split(" ") 

    if "q" in tokens:
        print("you will exit") #check to see if they want to quit
        break 

    if len(token) < 2: #need to have at least 2 inputs. this is not explicit in directions. had to run calc 1 to see function
        print("you do not have enough inputs")
        continue

    operator = token[0]   #since we split the input to a list, we can now access the list
    num1= token[1]

    if len(token) < 3:  #the calc assumes if you only insert the operator and a number, you want to do that to the number 0
        num2= 0

    else:
        num2 = token[2] #if a number present, it needs to be assigned

#the above are the rules to the calculator. this can be set up different, 
#for example you want to tell someone to add operator first then to nums etc

    if not num1.isdigit() or not num2.isdigit():
        print("Those aren't numbers!")
        continue   #this is important to verify if they are digits!! cant do math on letters! 
        elif operator == "+":
        result = add(float(num1), float(num2))



    elif operator == "-":   #checks for operator which was set on line 21
        result = subtract(float(num1), float(num2)) #sets result

    elif operator == "*":
        result = multiply(float(num1), float(num2))

    elif operator == "/":
        result = divide(float(num1), float(num2))

    elif operator == "square":
        result = square(float(num1))

    elif operator == "cube":
        result = cube(float(num1))

    elif operator == "pow":
        result = power(float(num1), float(num2))

    elif operator == "mod":
        result = mod(float(num1), float(num2))

    elif operator == "x+":
        result = add_mult(float(num1), float(num2), float(num3))

    elif operator == "cubes+":
        result = add_cubes(float(num1), float(num2))

    else:
        result = "Please enter an operator followed by two integers."

    print(result) #returns result
    #you can see thats why at the top the arithmetics were imported for the calcualtion part
    #that we had done in the other py file
    
