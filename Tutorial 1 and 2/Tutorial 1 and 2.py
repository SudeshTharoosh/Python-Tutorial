###check Tutorial 2 SD1 Programming
###a)
##num = 5
##print(num)
##num = num + 2
##print(num)
##num = num // 3 * 6
##print(num)
##print(7 + 15 % 4)
##num = 24 // 3 // 4
##print(num)

###b)i)
##a="Hello out there."
##print(a)
##b= 'Hello again'
##print(b)

###b)ii)
##total = 10
##greet = "Hello"
##both = str("10 ") + greet
##print(both)

###b)iii)
##print('A', end = ' ')
##print('B', end = ' ')
##print('C', end = ' ')
##print('D')

###b)iv)
##a = 10
##b = 99
##c = a + b
##print(c)

###4)i)
##name = input('Please enter your name: ')
##print('Hello', name)
##name = input('Please enter your name: \n')
##print('Hello', name)

###4)ii)
###4)iii)
###4)iv)
##the_text = input('Enter some text. \n')
##
###print - version 1
##print('This is what you entered: ')
##print(the_text)
##
###print - version 2
##print('This is what you entered: ')

###4)v)Lecture 2 self check questions
###a)
##num1=int(input("Enter number 1: "))
##num2=int(input("Enter number 2: "))
##total = num1 + num2
##print("The total is: ",total)
##
###b)
##cost = int(input("Enter cost of item: "))
##paid = int(input("Enter cash paid: "))
##change = paid - cost
##print("Change is: ", change)
##
###c)
##num1=int(input("Enter number 1: "))
##num2=int(input("Enter number 2: "))
##num3=int(input("Enter number 3: "))
##average = (num1+num2+num3)/3
##print("The average is: ",round(average,2))




###5)# shopping program with 4 bugs
##a=3 # number of apples
##o=0.0 # number of oranges
##print('you have: ',a,'oranges and',o,'apples')
##buy_a=4 # apples you buy
##buy_o=6 # oranges you buy
##print('you buy: ',buy_a,'apples and',buy_o,'oranges')
##a=a+buy_a
##o=o+buy_o
##print('you now have:',a,'apples and',o,'oranges')
##
##
##
###Additional Exercise
###Temperature Program (part 1) – To extend in a later tutorial. Write a program that will 
###convert an input Centigrade temperature (c) into Fahrenheit (f). Formula: f = (c * 1.8) 
###+ 32
##
##centigrade = float(input("Enter Temperature: "))
##fahrenheit = (c*1.8)+32
##print(centigrade,"centigrade equals to",round(fahrenheit,2),"fahrenheit")
##
##
###5)h)
##length = int(input("Enter the length: "))
##height = int(input("Enter the height: "))
##width = int(input("Enter the width: "))
##volume = width * length * width
##print("The volume is: ",volume)



###6)a)
##n = input("Please enter an integer: ")
##try:
##    n = int(n)
##    print(n)
##except ValueError:
##    print("Requires a valid integer!")
##
###6)b)Zero Division Error
##n = input("Please enter an integer: ")
##a = input("Enter another int: ")
##try:
##    z = int(n)/int(a)
##    print(z)
##except ZeroDivisionError:
##    print("Cannot divide by 0!!!!")
##except ValueError:
##    print("Should be int!!!!")
    













