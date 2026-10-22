import random

while(True):
  rand=random.randint(1,3)

  if rand==1:
    computer="snake"
  elif rand==2:
    computer="water"
  else:
    computer="gun"

  user=input("Enter your choice: Snake, Gun or Water \n").lower()

  if computer=="snake" and user=="water":
      print("You lost !",computer)
    
  elif computer =="gun" and user  =="water":
    print("You won !!",computer)
    
  elif computer =="water" and user =="gun":
    print("You lost !",computer)
    
  elif computer =="water" and user =="snake":
    print("You won !!",computer)
    
  elif computer =="water" and user =="water":
    print("Tie",computer)
    
  elif computer =="gun" and user =="gun":
    print("Tie",computer)
    
  elif computer =="snake" and user =="snake":
    print("Tie",computer)
    
  elif computer =="snake" and user =="gun":
    print("You won!!",computer)
  elif computer =="gun" and user =="snake":
    print("You lost !",computer)
  
