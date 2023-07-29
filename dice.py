import random

x=input("press y to roll dice")

x = "y"
  
while x == "y":
     

    no = random.randint(1,6)
     
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    input("press y to roll again and n to exit:")
    print("\n")
    if no == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    input("press y to roll again and n to exit:")
    print("\n")
    if no == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    input("press y to roll again and n to exit:")
    print("\n")
    if no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    input("press y to roll again and n to exit:")
    print("\n")
    if no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    input("press y to roll again and n to exit:")
    print("\n")
    if no == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
    input("press y to roll again and n to exit:")
    print("\n")
         
   

