import os

userInfo = {
    "Name": "",
}

def main():
    print("Please enter your name:")
    userInfo["Name"] = input()
    print(f"Hello {userInfo['Name']}")

    print(userInputHandler())


def userInputHandler():

    # -1 to make sure there is no remnant of the old input
    userInput = -1

    print("1. Add a Tast")
    print("2. View Tasks")
    print("3. Mark task as completed")
    print("4. Edit a task")
    print("5. Delete a task")
    print("6. Exit \n")

    userInput = int(input())

    return userInput

if __name__ == "__main__":
    main()
