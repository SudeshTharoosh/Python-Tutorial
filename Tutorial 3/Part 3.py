#Part 3: elif(chained conditional)
#a)
num = int(input("Enter number: "))
if num == 1:
    print("Convert Celsius to Fahrenheit")
    celsius = float(input("Enter celsius temperature: "))
    fahrenheit = (celsius * 1.8) + 32
    print(fahrenheit)
elif num == 2:
    print("Convert Fahrenheit to Celsius")
    fahrenheit = float(input("Enter fahrenheit temperature: "))
    celsius = (fahrenheit - 32) /1.8
    print(celsius)
else:
    print("Program Terminated")
    
    
#b)
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

add = num1 + num2
print(num1, "+", num2, "=", add)

sub = num1 - num2
print(num1, "-", num2, "=", sub)

mul = num1 * num2
print(num1, "*", num2, "=", mul)

try:
    div = num1 / num2
    print(num1, "/", num2, "=", div)
except ZeroDivisionError:
    print("Error")


num1 = int(input("Enter number 1: "))

    


#c)
satisfaction = float(input("Enter satisfaction number: "))
if satisfaction == 1:
    print("Totally satisfied")
    amount = float(input("Enter amount: "))
    tip = amount * 0.2
    print("The tip is", tip)
elif satisfaction == 2:
    print("Satisfied")
    amount = float(input("Enter amount: "))
    tip = amount * 0.15
    print("The tip is", tip)
elif satisfaction == 3:
    print("Dissatisfied")
    amount = float(input("Enter amount: "))
    tip = amount * 0.1
    print("The tip is",tip)
else:
    print("Program Terminated")





flag =0
cost = float(input("Enter the cost of the meal: "))
level = int(input("Ënter satifaction level: "))
if level == 1:
    tip = cost * 0.2
elif level == 2:
    tip = cos






    


