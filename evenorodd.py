num = int(input("enter a whole number"))

#if (num % 2) == 0:
#    print("The number is even") 
#else:
#   print("The number is odd")

shape = int(input("enter the amount of sides your shape has"))
shapelist = ["Triangle", "Square", "Pentagon", "Hexagon", "Heptagon", "Octagon", "Nonagon", "Decagon"]

if shape < 3 or shape > 9:
    print("please enter a number higher than 2, but lower than 10")
elif shape == 3:
    print(shapelist[0])
elif shape == 4:
    print(shapelist[1])
elif shape == 5:
    print(shapelist[2])
elif shape == 6:
    print(shapelist[3])
elif shape == 7:
    print(shapelist[4])
elif shape == 8:
    print(shapelist[5])
elif shape == 9:
    print(shapelist[6])
elif shape == 10:
    print(shapelist[7])