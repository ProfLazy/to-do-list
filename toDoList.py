import os
import time

userInfo = {
    "Name": "",
}

def main():
    print("Please enter your name:")
    userInfo["Name"] = input()
    print(f"Hello {userInfo['Name']}")

    whileControl = 0


    while whileControl != 1:
        userInput = userInputHandler()

        if type(userInput) == str:
            invalidInput()
        elif userInput == 1:
            type(userInput)
        elif userInput == 2:
            type(userInput)
        elif userInput == 3:
            type(userInput)
        elif userInput == 4:
            type(userInput)
        elif userInput == 5:
            type(userInput)
        elif userInput == 6:
            whileControl = 1
        else:
            invalidInput()

def invalidInput():
    print("Please select a valid input")
    time.sleep(1)

def addTask():
    
    


def userInputHandler():

    # -1 to make sure there is no remnant of the old input
    userInput = -1

    print("1. Add a Tast")
    print("2. View Tasks")
    print("3. Mark task as completed")
    print("4. Edit a task")
    print("5. Delete a task")
    print("6. Exit \n")

    userInput = input()

    return userInput

if __name__ == "__main__":
    main()
