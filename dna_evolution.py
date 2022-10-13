import random
res=[]

def evolve(x):
    ind = random.randrange(0,len(x))
    c = random.randrange(0,100)
    if c == 1:
        res.append(ind)  
           

with open("dna_data.txt") as f:
    dat = f.read()
    dat = list(dat)
    print(dat) 
for i in range(0,10000):
    evolve(dat)

   

for j in res:
    if dat[j] == '0':
        dat[j] = '1'
    else:
        dat[j] = '0'
print(dat)      
print(res) 
print(len(res))

  