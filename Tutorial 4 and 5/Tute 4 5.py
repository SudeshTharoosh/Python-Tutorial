#Author Name: Sudesh Tharoosh
#Date: 8 Nov 2022
#Purpose: Enhancing the lap time recorder

laptimes = list()
count = 1

while True:
    laptime = input("Enter the lap time: " + str(count) + "(x to end)" + ":")
    if laptime == "x":
        break
    laps = float(laptime)
    laptimes.append(laps)
    count += 1
print("Fastest lap time is: ", min(laptimes))
print("Slowest lap time is: ", max(laptimes))
print("Average laptime is: ", round(sum(laptimes)/len(laptimes), 2))

    
