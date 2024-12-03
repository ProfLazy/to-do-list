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
        completedTask = userInfo.pop(taskKey)
        userInfo["completedTasks"].append(completedTask)
        userInfo["numberCompleted"] += 1
        print(f"Task {taskInput} marked as completed.\n")
    else:
        print(f"Task {taskInput} not found.\n")
    time.sleep(1)

def editTask():
    print("\n")
    print("Enter the task number you want to edit: ")
    taskInput = input()
    taskKey = f"Task {taskInput}"

    if taskKey in userInfo:
        editTask = userInfo.pop(taskKey)
        print("Task found. Please type in the rewritted task or type EXIT to stop:")
        userEdit = input()
        if userEdit == "EXIT":
            userInfo[taskKey] = editTask
        else:
            userInfo[taskKey] = userEdit
    else:
        print(f"Task {taskInput} not found.\n")

    for i in range(1, userInfo["taskCounter"] + 1):
        reorderTask = userInfo.pop(f"Task {i}")
        userInfo[f"Task {i}"] = reorderTask
    
    time.sleep(1)
    print("\n")

def deleteTask():
    print("\n")
    print("Enter the task number you want to delete: ")
    taskInput = input()
    taskKey = f"Task {taskInput}"

    if taskKey in userInfo:
        deleteTask = userInfo.pop(taskKey)
        print( f"Task found. Are you sure you want to delete task \"{userInfo[taskKey]}\"? Y for yes, others for no")
        userEdit = input()
        if userEdit == "Y":
            del deleteTask
        else:
            userInfo[taskKey] = deleteTask
    else:
        print(f"Task {taskInput} not found.\n")
    time.sleep(1)
    print("\n")


if __name__ == "__main__":
    main()
    print(userInfo)
