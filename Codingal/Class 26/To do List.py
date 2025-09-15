#To Do List
todoList = []

def addTask(taskName):
    todoList.append(taskName)
    print(f"{taskName} is added to the list")
def removeTask(taskName):
    todoList.remove(taskName)
    print(f"{taskName} is removed from the list")
def displayAllTask():
    print("Displaying all Task",todoList)
def modifyTask(oldTask):
    newTask = input("Enter the new task:")
    index = todolist.index(oldTask)
    todoList[index] = newTask
    print(f"'{oldTask}' has been modified to '{newTask}'")

menu = """
    ------Task Application------
    1. Add a Task
    2. Remove a Task
    3. Display a Task
    4. Modify a Task
    5. Exit
    ------------------------------
    """

while True:
    print(menu)
    choice = int(input("Enter your choice:"))
    if choice == 1:
        taskName = input("Enter the task:")
        addTask(taskName)
    elif choice ==2:
        taskName = input("Enter the task:")
        removeTask(taskName)
    elif choice == 3:
        displayAllTask()
    elif choice == 4:
        taskName = input("Enter the task name:")
        modifyTask()
    elif choice == 5:
        print("Thank you for using our Application")
        break