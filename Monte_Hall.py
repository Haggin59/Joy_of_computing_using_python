import random
doors = [0 for i in range(3)]
goat_door = []
gift = random.randint(0,2)
doors[gift] = "🎁"
for i in range(0,3):
    if i == gift:
        continue
    else:
        doors[i] = "🐐"
        goat_door.append(i)
for i in range(0,3):
    print("🚪",end="")

choice = int(input("\nChoose a door(0/1/2):"))

for i in range(0,3):
    if i == choice:
        print("X",end="")
    else:
        print("🚪",end="")
      
bluff = random.choice(goat_door)
while bluff == choice:
    bluff = random.choice(goat_door)
print("\n")    

for i in range(0,3):
    if i == choice:
        print("X",end="")
    elif i == bluff:
        print("🐐",end="")
    else:
        print("🚪",end="")      

print("\nYou choose door",choice)  
swap = input("Do you wanna swap(y/n)?")

for i in range(0,3):
    print(doors[i],end="")

if swap == 'y':
    if doors[choice] == "🐐":
        print("\nYou Win:)")
    else:
        print("\nYou loose:(")
if swap == 'n':
    if doors[choice] == "🎁":
        print("\nYou Win:)")
    else:
        print("\nYou loose:(")              

       


            

