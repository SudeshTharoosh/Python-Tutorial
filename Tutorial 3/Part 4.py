#Part 4: Boolean Operators
#a) Completed in shell

#b)
m = int(input("Give me number between 1 and 10: "))
if m >=1 and m <=10:
    print("Well done! You gave me: ", m)

#c) Completed in shell

#d)
mark = int(input("Enter mark: "))
if mark < 0 or mark >100:
    print("Invalid")
elif mark >= 70:
    print("Exceptional result!")
elif mark >= 40:
    print("Satisfactory result!")
else:
    print("You have failed.")


#e) Completed in shell

#f)
x = 10
if not x>10:
    print("Not returned True")
else:
    print("Not returned False")
