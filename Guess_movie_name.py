import random
movies = ['titanic','speed','matrix','commuter','taken']
movie_name = random.choice(movies)
movie_name = list(movie_name)

def guess_movie_name(mname):
    guess = []
    for i in range(len(mname)):
        guess.append("_")
    print(guess)    
    while(True):
        flag = 0
        char = input("Enter a letter:")
        for i in range(len(mname)):
            if char == mname[i]:
                guess[i] = char
                flag = 1   
        if flag == 0:
            print("Letter not present")      
        print(guess)
        if guess == mname:
            print("Good Job")
            break        
                
guess_movie_name(movie_name)