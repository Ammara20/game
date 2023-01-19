
#level1
level1_done = False

while level1_done == False:
    print("what do you do?(LOOK/SHOOT/MOVE)")
    choice = input() #taking input from player
    if choice == "LOOK":
        print("You look around, but its too dark to see.")
        print("USE FLASHLIGHT? (Y/N)")
        sub_choice = input()
        if sub_choice == "Y":
            print("There is the exit, go!")
            level1_done = True
        else:
            print("Man your really cant see anything")
    elif choice == "SHOUT":
        print("No one replies")
    elif choice == "MOVE":
        print("You moved without seeing but your feel a door in front of you!")
        level1_done = True
    else:
        print("Invalid input. You better make a decision..")



#level2
print("level2")
level2_done = False
while level2_done == False:
     print("what is more possibilty to get out in from cave")   
     choice = input("") 
    if  choice == "Finding":
         print("searching bag to find mape or something more")
         print("using mape and compex ?(Y/N)")
        level2_done = True
    else:
         print("There is no way out,Die")
         sub_choice ==  input ("")
     if sub_choice == "Die":
        print("just watching yourself die")
        level2_done = True
     elif choice == "Life":
        print("Iphone helpline get help to out!")
        level2_done = True
