x = input("What do you choose? Rock? Paper? Or the mighty Scissors?")
if x == ("Rock" or "rock"):
    print ("You selected Rock")
elif x == ("Scissors" or "scissors"):
    print ("You selected Scissors")
else:
    x == ("Paper" or "paper")
    print ("You selected Paper")

    #Randomise computer input

import random
cpu = ["Scissors", "Rock", "Paper"]
print ("Computer selects")
cpu2 = (random.choice(cpu)) #For random selection generation 
print ("Computer selects", cpu2) 

#sort results 

if x == ("Rock" or "rock") and cpu2 == ("Rock" or "rock"):
    print("Draw! Go again!")
elif x == ("Rock" or "rock") and cpu2 == ("Paper" or "paper"):
    print("Down your bevvy")
elif x == ("Rock" or "rock") and cpu2 == ("Scissors" or "scissors"):
    print("One minute")
elif x == ("Paper" or "paper") and cpu2 == ("Paper" or "paper"):
    print("Draw! Go again!")
elif x == ("Paper" or "paper") and cpu2 == ("Scissors" or "scissors"):
    print("Down your bevvy")
elif x == ("Paper" or "paper") and cpu2 == ("Rock" or "rock"):
    print("One minute")
elif x == ("Scissors" or "scissors") and cpu2 == ("Scissors" or "scissors"):
    print("Draw! Go again!")
elif x == ("Scissors" or "scissors") and cpu2 == ("Rock" or "rock"):
    print("Down your bevvy")
else:
    x == ("Scissors" or "scissors") and cpu2 == ("Paper" or "paper")
    print("One minute")
