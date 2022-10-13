import random

def rand_word():
    words = ['computer','science','python','JOCP','machine','learning']
    word = random.choice(words)
    return word

def jumbled_word(s1):
    jw = "".join(random.sample(s1,len(s1)))
    return jw

def point(n1,n2,s1,s2):
    print("Thanks for playing :)\nThe points are: ")
    print(n1,":",s1)
    print(n2,":",s2)
    
def play():
    pname1 = input("Enter Player 1 Name:")
    pname2 = input("Enter Player 2 Name:")
    pscore1 = 0
    pscore2 = 0
    turn = 0
    while(1):
        ans = rand_word()
        qn = jumbled_word(ans)
        if turn%2 == 0:
            print("What is on my mind,",pname1,"?")
            print(qn)
            an1 = input()
            if an1 == ans:
                pscore1 += 1
                print(pname1,",Your score is",pscore1)
            else:
                print(pname1,",Better Luck next time!")

        if turn%2 != 0:
            print("What is on my mind,",pname2,"?")
            print(qn)
            an2 = input()
            if an2 == ans:
                pscore2 += 1
                print(pname2,",Your score is",pscore2)
            else:
                print(pname2,",Better Luck next time!")        
        turn += 1
        ch = int(input("Enter 0-To Exit & 1-To Continue "))
        if ch == 0:
            point(pname1,pname2,pscore1,pscore2)
            break
play()        







