import random
import time

#decides random integers for room and inventory making.
roomRandom = random.randint(1,5)
invRandom = random.randint(1,10)

#decides random inventory

if(invRandom == 1):
        invDecisionLL = "knife"
        invDecisionCL = "Knife"
if(invRandom == 2):
        invDecisionLL = "shoe lace"
        invDecisionCL = "Shoe lace"
if(invRandom == 3):
        invDecisionLL = "birthday card"
        invDecisionCL = "Birthday card"
if(invRandom == 4):
        invDecisionLL = "shard of glass"
        invDecisionCL = "Shard of glass"
if(invRandom == 5):
        invDecisionLL = "watch"
        invDecisionCL = "Watch"
if(invRandom == 6):
        invDecisionLL = "pen and paper"
        invDecisionCL = "Pen and paper"
if(invRandom == 7):
        invDecisionLL = "toy car"
        invDecisionCL = "Toy car"
if(invRandom == 8):
        invDecisionLL = "book"
        invDecisionCL = "Book"
if(invRandom == 9):
        invDecisionLL = "match"
        invDecisionCL = "Match"
elif(invRandom == 10):
        invDecisionLL = "key"
        invDecisionCL = "Key"
else:
        filler = "filler"

if(roomRandom == 1):
        roomDecisionLL = "basement"
        roomDecisionCL = "Basement"
elif(roomRandom == 2):
        roomDecisionLL = "kitchen"
        roomDecisionCL = "Kitchen"
elif(roomRandom == 3):
        roomDecisionLL = "bathroom"
        roomDecisionCL = "Bathroom"
elif(roomRandom == 4):
        roomDecisionLL = "bedroom"
        roomDecisionCL = "Bedroom"
else:
        roomDecisionLL = "driveway"
        roomDecisionCL = "Driveway"

print("You have awoken to a bright light. You awake only to find yourself lying on the", roomDecisionLL, "floor.")

if(roomDecisionCL == "Driveway"):
        print("The driveway door is open. You venture inside.")

print("In your pocket, you have a", invDecisionLL)
print()
print("Do you need a tutorial? Y/N")
print()
tutorialQuery = input("TAG > ")


if(tutorialQuery == "Y" or tutorialQuery == "y"):
        print("To view your inventory type I")
        print("To look around type L")
        print("To interact with others press E")
        print("To speak to people type T")
        print("To view this type h")
elif(tutorialQuery == "N"):
        filler = "filler"
else:
        filler = "filler"

#mission 1
#checks if user already has keys

objectiveOpenDoor = "false"
objectiveKey = "false"
if(invDecisionCL == "Key"):
        print("You have some keys. Maybe you should look around and find the door.")
        objectiveKey = "true"

#starts the loop until objcetive (opening door) is complete.

while(objectiveOpenDoor == "false"):

        inputBox = input("TAG > ")

        #runs through possible answers

        if(inputBox == "H" or inputBox == "h"): 
                print("To view your inventory type I")
                print("To look around type L")
                print("To interact with others press E")
                print("To speak to people type T")
                print("To view this type h")
        elif(inputBox == "I" or inputBox == "i"):
                print("Your inventory includes the following:")
                print(invDecisionCL)
        elif(inputBox == "L" or inputBox == "l"):
                if(objectiveKey != "true"):
                        print("You look around and see a open box. There appears to be something inside it.")
                        print("Maybe you should take a look. Press E") 
                        findKeysAvailable = "true"
                elif(objectiveKey == "true"):
                        print("You are standing infront of a wooden door.")
        elif(inputBox == "E" or inputBox == "e"):
                if(objectiveKey == "true"):
                                print("You opened the door!")
                                objectiveKey = "false"
                                objectiveOpenDoor = "true"
                elif(invDecisionCL != "Keys"):
                        if(findKeysAvailable != "true"):
                                print("There isn't anything here to interact with. Try looking around.")
                        elif(findKeysAvailable == "true"):
                                print("Keys have now been added to your inventory.")
                                print("Your inventory now consists of:")
                                print(invDecisionCL, "and keys.")
                                objectiveKey = "true"
                                print("You walk to the door.")
                        else:
                                filler = "filler"
        elif(inputBox == "T" or inputBox == "t"):
                print("There is no one in the room. Try looking around.")
        else:
                filler = "filler"

        #adds spacing
        print()

#starts the loop until objcetive (writing an essay or reading a story, which ever the user does not currently have) is complete. If the user does not have either of these, then they will have to read.

objectiveHaveFun = "false"
whatActivityToDo = "read"
whatItemToUse = "book"
itemUnlockable = "false"
itemInInventory = "false"
spokenToJordan = "false"
obtainedItem = "false"

if(invDecisionCL == "book"):
        whatActivityToDo = "write"
        whatItemToUse = "pen and paper"
elif(invDecisionCL == "Pen and paper"):
        whatActivityToDo = "read"
        whatItemToUse = "book"

#mission 2  

print("You leave the room, to find a hallway of doors. You know that only one can lead you to what you need. To", whatActivityToDo, "with a", whatItemToUse)

#new command announcement

print("You have unlocked a command for this level!")
print("Type U to use an item in your inventory.")

#starts a if statement to check if the user had the keys to start with.

ownKeyQuery = ""
if(invDecisionCL == "Key"):
        ownKeyQuery = ""
elif(invDecisionCL != "Key"):
        ownKeyQuery = "a key"        

while(objectiveHaveFun == "false"):

        inputBox = input("TAG > ")

        #runs through possible answers

        if(inputBox == "H" or inputBox == "h"): 
                print("To view your inventory type I")
                print("To look around type L")
                print("To interact with others press E")
                print("To speak to people type T")
                print("To view this type h")
                print("Level Specific Command: To use an item in your inventory, press U.")
        elif(inputBox == "I" or inputBox == "i"):
                print("Your inventory consists of:")
                print(invDecisionCL)
                if(ownKeyQuery == ""):
                        filler = "filler"
                elif(ownKeyQuery != ""):
                        print(ownKeyQuery)
                else:
                        filler = "filler"
                
                if(itemInInventory == "true"):
                        print(whatItemToUse)
                elif(itemInInventory == "false"):
                        filler = "filler"
                else:
                        filler = "filler"
        elif(inputBox == "L" or inputBox == "l"):  
                print("There is a strange man walking back and forth. Maybe, you should speak to him.")
                print("Besides the man, you notice a drawer, with a", whatItemToUse, "inside of it.")
                itemUnlockable = "true"
        elif(inputBox == "E" or inputBox == "e"):
                if(itemUnlockable == "false" or spokenToJordan == "false"):
                        print("There isn't anything visible right now. Maybe you should have a look around.")
                elif(spokenToJordan  == "true"):
                        print("You pick up the", whatItemToUse, ".")
                        itemInInventory = "true"
        elif(inputBox == "T" or inputBox == "t"):
                if(itemUnlockable == "true" and itemInInventory == "false"):
                        print("Walking Man: Hello, there.")
                        print("Walking Man: My name is Jordan. You seem to be, hazy.")
                        filler = input("Press Enter to continue dialogue.")
                        print("Jordan: Well, what do you want?")
                        print("You: Can I take that", whatItemToUse)
                        filler = input("Press Enter to continue dialogue.")
                        print("Jordan: Sure, I guess.")
                        obtainedItem = "true"
                        spokenToJordan = "true"
                        print("Jordan: Type E")
                elif(itemUnlockable == "false" and spokenToJordan == "false"):
                        print("There isn't anyone in sight.")
                elif(itemInInventory == "true" and spokenToJordan == "true"):
                        print("Jordan: What do you want?")
                elif(spokenToJordan == "false" and itemInInventory == "true"):
                        print("Walking Man: I assume you want whats in this box.")
                        print("Walking Man: Well, it will be no use to you. You already have what you need.")
                        print("Walking Man: By the way, my name is Jordan.")
                        spokenToJordan == "true"
                else:
                        filler = "filler"
        elif(inputBox == "U" or inputBox == "u"):
                if(obtainedItem != "true"):
                        print("You don't have anything to use.")
                        print("Have a look around the room!")
                elif(obtainedItem == "true"):
                        objectiveHaveFun = "true"
                        print("You", whatActivityToDo,". You are now no longer bored.")

        else:
                filler = "filler"

        #adds spacing
        print()

print("You have done what you needed to do to have fun.")
print("Well, at least keep your brain active.")
print()
print("You feel good. Like you could do anything.")
print("But, you still need to escape.")
print("You don't even know where you are.")

#variables defaults
objectiveEscapeHouse = "false"
infrontOfDoor = "false"

#while loop

while(objectiveEscapeHouse == "false"):

        inputBox = input("TAG > ")

        #runs through possible answers

        if(inputBox == "H" or inputBox == "h"): 
                print("To view your inventory type I")
                print("To look around type L")
                print("To interact with others press E")
                print("To speak to people type T")
                print("To view this type h")
        elif(inputBox == "I" or inputBox == "i"):
                print("Your inventory consists of the following:")
                print(invDecisionCL)
                if(invDecisionCL == "Key"):
                        filler = "filler"
                elif(invDecisionCL != "Key"):
                        print("A key")

                if(invDecisionCL != "Book" and invDecisionCL != "Pen and paper"):
                        print("Book")
                elif(invDecisionCL != "Book"):
                        if(invDecisionCL != "Pen and paper"):
                                print("Pen and paper")
                elif(invDecisionCL != "Pen and paper"):
                        if(invDecisionCL != "Book"):
                                print("Book")
                else:
                        filler = "filler"
        elif(inputBox == "L" or inputBox == "l"):
                if(infrontOfDoor == "false"):
                        print("You are in the hallway. There appears to be one specific")
                        print("door that is calling your name.")
                        print("You walk towards the door.")
                        infrontOfDoor = "true"
                elif(infrontOfDoor == "true"):
                        print("The door is locked, but you know it is the door for you")
                        print("There is a poster on the door. It says that the room is")
                        print("'Liable to radiation posioning'")
                        print("And, the door appears to be open just a bit.")
                else:
                        filler = "filler"
        elif(inputBox == "E" or inputBox == "e"):
                if(infrontOfDoor != "true"):
                        print("There is nothing to interact with.")
                elif(infrontOfDoor == "true"):
                        print("You open the door.")
                        objectiveEscapeHouse = "true"
        elif(inputBox == "T" or inputBox == "t"):
                print("There is no one, except for Jordan, in the hallway.")
        
        #adds spacing
        print()

print("You step inside the room and the door slams shut behind you.")
print("You feel cold.")
print("You are hungry.")
print("You are thirsty.")
print("You are tired...")
time.sleep(3.2)
print()
print("You are...")
time.sleep(4.2)
print("it.")
print()
time.sleep(1000000000000000000000)
