# print("Hello, World!") # this will print "Hello, World!" to the console

# x, y, z = "Samuel", "Ochygole", "Jireh" # this will assign the values "Samuel", "Ochygole", and "Jireh" to the variables x, y, and z respectively
# my_age = 20 # this will assign the value 20 to the variable my_age
# Car_Name = "BMW" # this will assign the value "BMW" to the variable Car_Name
# print("SurName:", x) # this will print the value of x with the label "SurName:"
# print("First Name:", z) # this will print the value of z with the label "First Name:"
# print("Full Name:", x, y, z) # this will print the values of x, y, and z with the label "Full Name:"
# print(type(my_age)) # this will print the type of the variable my_age
# print(Car_Name) # this will print the value of Car_Name

# q = "awesome" # this will assign the value "awesome" to the variable q
# def myfunc(): # this will define a function called myfunc that will print "Python is awesome" when called
#     print("Python is " + q) # this will print the value of q with the label "Python is "
# myfunc() # this will call the function myfunc and print "Python is awesome"


# print(10 + 5) # + add the two values together and get an int as an answer
# print(20 - 5)# - subtracte the two values and get an int as an answer
# print(5 * 5) # * mutiplare the two values and int as an answer
# print(7 / 2) # / divide the two values and get a float as an answer
# print(7 // 2) # // divide the two values and get an int as an answer
# print(7 % 2) # % divide the two values and get the remainder as an answer
# print(10 ** 2) # ** raise the first value to the power of the second value and get an int as an answer


# print(type(10)) # this will print <class 'int'> because 10 is an integer
# print(type(10.5)) # this will print <class 'float'> because 10.5 is a float
# print(type("10")) # this will print <class 'str'> because "10" is a string
# print(int("10")) # this will print 10 because "10" is a string that can be converted to an integer
# print(float("10.5")) # this will print 10.5 because "10.5" is a string that can be converted to a float
# print(str(10)) # this will print "10" because 10 is an integer that can be converted to a string

# print(10 > 5) # this will print True because 10 is greater than 5
# print(10 < 5) # this will print False because 10 is not less than 5
# print(10 == 5) # this will print False because 10 is not equal to 5
# print(10 != 5) # this will print True because 10 is not equal to 5
# print(10 >= 5) # this will print True because 10 is greater than or equal to 5
# print(10 <= 5) # this will print False because 10 is not less than or equal to 5

# # Note: You can not converte an alphbet(abc) in a str "" into a number(123) But you can converte a number(123) in a str "" into an actual number.

# nice_name = input("Enter your name: ")
# print(f"Your name is {nice_name}")
# number1 = input("Enter first number: ")
# number2 = input("Enter second number: ")

# if type(int(number1)) == int and type(int(number2)) == int:
#     print(f"The total sum of your number is: {int(number1) + int(number2)}")
# else:
#     print("Cannot add them")

# def job(age):

#     if age >= 65:
#         return "You cannot do this job"
#     elif age >= 20:     # order matters
#         return "You have the job"
#     return "Wait till you get to the age"

# def main():
#     age = 30
#     return(job(age))
    
# if __name__ == "__main__":
#     main()


# # List

names = ["Jireh", "Janet", "John", "Joy", 656, 88, 1, True]
# print(name)

# name_one = names.pop(0)
# print(name_one)
# print(names)

# names.remove(88)
# print(names)

# name.insert(5, "ok")
# print(names)

for name in names:
    print(name)

for name in range(1,3):
    print(name)

for name in names:
    print(name)