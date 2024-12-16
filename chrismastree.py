import random

rows = 12
for i in range(rows):
    
    spaces = rows - i - 1
    stars = 2 * i + 1

    
    for j in range(spaces):
        print(" ", end=" ")
    

    
    for j in range(stars):
        if random.randint(1,6) == 1:
            print("-",end=" ")
        else:
            print("*",end=" ")

    print("")

log_heigth = 3

for i in range(log_heigth):
    log_spaces = rows - 1
    for k in range(log_spaces):
        print(" ",end=" ")
    print("|")

