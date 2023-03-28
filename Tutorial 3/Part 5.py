#Part 5 - Create a program using if, elif, else

response = input("Do you like Python? ")
if response.lower() == "yes" or response.lower()=="y":
    print("You are on the right course")
elif response.lower() == "no" or response.lower()=="n":
    print("You might change your mind")
else:
    print("I did not understand")

    
    
