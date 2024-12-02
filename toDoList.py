import os
import time

userInfo = {
    "taskCounter" : 0,
    "Name" : "wasd",
    "completedTasks": [],
    "numberCompleted": 0
}

def main():
    print("Please enter your name:")
    userInfo["Name"] = input()
    print(f"Hello {userInfo['Name']}")

    whileControl = 0


    while whileControl != 1:
        userInput = userInputHandler()

        if userInput == "1":
            addTask()
        elif userInput == '2':
            viewTask()
        elif userInput == '3':
            taskCompleted()
        elif userInput == '4':
            type(userInput)
        elif userInput == '5':
            type(userInput)
        elif userInput == '6':
            whileControl = 1
        else:
            invalidInput()

def userInputHandler():

    # -1 to make sure there is no remnant of the old input
    userInput = -1

    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark task as completed")
    print("4. Edit a task")
    print("5. Delete a task")
    print("6. Exit \n")

    userInput = input()

    return userInput

def invalidInput():
    print("Please select a valid input \n")
    time.sleep(1)

def addTask():
    print("Okay, enter your task")
    userInfo["taskCounter"] += 1
    userInfo[f"Task {userInfo['taskCounter']}"] = input()
    print("\n")
    time.sleep(1)

def viewTask():
    print("\n")
    print("User: " + userInfo["Name"])
    print("Tasks:")
    for key,value in userInfo.items():
        if key.startswith("Task"):
            print(key + ": " + value)
    print("\n")
    print("Completed Tasks:")
    if not userInfo["completedTasks"]:
        print("NONE\n")
    else:
        for i in range(0 , len(userInfo["completedTasks"])):
            print(userInfo["completedTasks"][i] + "\n")
    time.sleep(2)

def taskCompleted():
    print("\n")
    print("Enter Task Number Completed: ")
    taskInput = input()
    taskKey = f"Task {taskInput}"

    if taskKey in userInfo:
        completed_task = userInfo.pop(taskKey)
        userInfo["completedTasks"].append(completed_task)
        userInfo["numberCompleted"] += 1
        print(f"Task {taskInput} marked as completed.\n")
    else:
        print(f"Task {taskInput} not found.\n")
    time.sleep(1)



if __name__ == "__main__":
    main()
    print(userInfo)
