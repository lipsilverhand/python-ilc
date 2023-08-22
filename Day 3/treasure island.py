print("---Treasure Island Game---")

x = input("Do you want to turn right or left? ")

if x=="right":
    print("Turn right.")
    y = input("Do you want to swim or go around? ")
    if y=="swim":
        print("Swim.")
        print("You got rooted by lake monster and drown. Game over!")
    else:
        print("Go around.")
        print("You found a wall with three different color doors. ")
        z = input("Which door you are going to pick? (red, blue, green) ")
        if z==red:
            print("Red door.")
            print("You found traps and died. Game over!")
        elif z==blue:
            print("Blue door.")
            print("You met high level foes and killed. Game over!")
        else: 
            print("Green door.")
            print("You entered the door and found the treasure, congrats")

else:
    print("Turn left.")
    print("You got attacked and killed by pirates. Game Over!")