x = (raw_input("What do you choose? Rock? Paper? Or the mighty Scissors?"))
if x == ("Rock" or "rock"):
    print ("You selected Rock")
elif x == ("Scissors" or "scissors"):
    print ("You selected Scissors")
else:
    x == ("Paper" or "paper")
    print ("You selected Paper")

import random
cpu = ["Scissors", "Rock", "Paper"]
print ("Computer selects") 
print (random.choice(cpu))

if x == (("Rock" or "rock") and cpu == ("Rock" or "rock")):
    print ("Draw! Go again!")
elif x == (("Rock" or "rock") and cpu == ("Paper" or "paper")):
    print ("Down your bevvy")
elif x == (("Rock" or "rock") and cpu == ("Scissors" or "scissors")):
    print ("One minute")
elif x == (("Paper" or "paper") and cpu == ("Paper" or "paper")):
    print ("Draw! Go again!")
elif x == (("Paper" or "paper") and cpu == ("Scissors" or "scissors")):
    print ("Down your bevvy")
elif x == (("Paper" or "paper") and cpu == ("Rock" or "rock")):
    print ("One minute")
elif x == (("Scissors" or "scissors") and cpu == ("Scissors" or "scissors")):
    print ("Draw! Go again!")
elif x == (("Scissors" or "scissors") and cpu == ("Rock" or "rock")):
    print ("Down your bevvy")
else: 
	x == (("Scissors" or "scissors") and cpu == ("Paper" or "paper")):
    print ("One minute")