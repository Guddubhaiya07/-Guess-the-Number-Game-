import random
num=random.randint(1,100)
Gussing=7
count=0

while Gussing>count:
    count +=1
    guess=int(input("you Gussing the number range (1,100)"))
  
    if guess==num:
        print(f'The number is {guess} and you found it right !! in the {count} attempt')
        break
    elif count >=Gussing and guess != num:
        print(f'Oops sorry, The number is {guess} better luck next time')
        
    elif guess >= num:
        print("You guess grater number ")
        
    elif guess <= num:
        print("you guess lower value ")
    else:
        print("You guess out of range ")
        

        
