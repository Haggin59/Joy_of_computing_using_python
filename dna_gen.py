import random
with open("dna_data.txt","w") as f:
    for i in range(0,100):
        ind = random.randint(0,100)
        if ind%2 == 0:
            f.write('1')
        else:
            f.write('0')
    

