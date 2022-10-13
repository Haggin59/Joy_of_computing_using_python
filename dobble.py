import string
import random
c1 = [0 for i in range(5)]
c2 = [0 for i in range(5)]
symbols = []
symbols = list(string.ascii_letters)

pos1 = random.randrange(0,5)
pos2 = random.randrange(0,5)

common = random.choice(symbols)
symbols.remove(common)

if pos1 == pos2:
    c1[pos1] = common
    c2[pos1] = common
else:
    c1[pos1] = common
    c2[pos2] = common

    c1[pos2] = random.choice(symbols)
    symbols.remove(c1[pos2])
    c2[pos1] = random.choice(symbols)
    symbols.remove(c2[pos1])
for i in range(0,5):
    if i!= pos1 and i!= pos2:
        c1[i] = random.choice(symbols)
        symbols.remove(c1[i])
        c2[i] = random.choice(symbols)
        symbols.remove(c2[i])
       
print(c1,"\n",c2)  
ans = input("Find the repeated value: ")      
if ans == common:
    print(":)")
else:
    print(":(")    




