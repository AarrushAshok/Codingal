#To Do List
todoList = []

def addTask(taskName):
    print("Adding a Task")
def removeTask(taskName):
    print("Removing a Task")
def displayAllTask():
    print("Displaying all Task")
def modifyTask():
    print("Modifying a Task")

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
        addTask("")
    elif choice ==2:
        removeTask("")
    elif choice == 3:
        displayAllTask()
    elif choice == 4:
        modifyTask()
    elif choice == 5:
        print("Thank you for using our Application")
        break