def Binary_guesser(l,u):
    first_pos = l
    last_pos = u
    i = 0
    while(True):
        print("Is your Number greater than, less than or equal to ",(first_pos + last_pos)//2,"?(>/</=)")
        status = input()
        if status == "<":
            last_pos = (first_pos + last_pos)//2

        elif status == ">":
            first_pos = (first_pos + last_pos)//2
            
        elif status == "=":
            print("The number is ",(first_pos + last_pos)//2)
            print("Found in Iteration",i)
            break
        else:
            print("Invalid Entry!")
            break   
        i+=1 

l = int(input("Enter Lower limit:"))
u = int(input("Enter Upper limit:"))

Binary_guesser(l,u)        