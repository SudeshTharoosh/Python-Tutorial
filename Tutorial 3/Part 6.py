#Part 6: Extended Exercises - Adding exception handling

n = input("Give me a number over 100: ")
try:
    n = int(n)
    if n <= 100:
        print(n, "is not over 100")
except ValueError:
    print("Input numerical values only")


age = input("Enter your age: ")
try:
    age = int(age)
    if age >= 18:
        print("You can vote")
except ValueError:
    print("Input numerical values only")
    


#Part 4)d)
#Try and except
num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
if num2 == 0:
    try:
        div = num1 / num2
        print(num1, "/", num2, "=", div)
    except ZeroDivisionError:
        print("Error")


#Nestedif
        
    
