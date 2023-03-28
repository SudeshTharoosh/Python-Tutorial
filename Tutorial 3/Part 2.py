#Part 2: if-else
#a)
x = int(input("Give me a number: "))
if x < 0:
    print(x,"is negative")
else:
    print(x,"is positive")


#b)
mark = int(input("Enter mark: "))
if mark < 40:
    print("Fail")
else:
    print("Pass")

#Test Results
# 39 FAIL
# 40 PASS
# 41 PASS


#c)
num = int(input("Enter number: "))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")
