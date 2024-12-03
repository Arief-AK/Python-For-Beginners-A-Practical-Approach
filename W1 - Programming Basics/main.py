# Our first ever command, woohoo!
print("Hello World!")

# Variables help us contain data
number = 1                              # Numbers (Integers)
decimal = 1.0                           # Decimals (Float)
text = "hello"                          # String
true_condition = True                   # Booleans
false_condition = False                 # Booleans

# We can name our own variables
my_first_variable = 1
my_second_variable = 2

# It is good practice to name variables appropriately

# Some bad examples
this_is_not_a_good_variable_name = 1    # Too long
text = "example text"                   # What is text?
#1_variable = ""                        # Cannot START with a number
variable_1 = ""                         # This is OK

# Better suggestions
name = "Arief"                          # Name is always text
age = 27                                # Age is always a number
is_student = True                       # Usually store yes/no data

# Use Python to introduce yourself
name = input("What is your name? ")
age = input("How old are you? ")
print(f"Hello, my name is {name} and I am {age} years old.")

# Moving on, we can work with numbers too. Let's do some addition
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
print(f"The sum is: {first_number + second_number}")

# Moving on, some more simple calculations
print(f"Subtraction :{first_number - second_number}")
print(f"Multiplication :{first_number * second_number}")
print(f"Division :{first_number / second_number}")

# This is all very nice, let us now introduce conditions, the concept is simple

# IF something happens THEN do something, in Python we use if and else statements
age = int(input("What was your age again? "))

if age > 20:
    print("Man you are old!")
elif age >= 18:
    print("You are getting old!")
else:
    print("skibidii")

# Great, we have all the knowledge needed to program a simple calculator
