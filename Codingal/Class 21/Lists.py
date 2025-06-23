#Lists
todo = [] #Empty List

def addTask():
    task = input("Enter a new task to add:")
    todo.append(task)
    print("Task added successfully")

def viewTask():
    print("Viewing all tasks")
    count = 1
    for task in todo:
        print(count.task)
        count += 1

def deleteTask():
    task = input("Enter a task to delete:")
    if task in todo:
        todo.remove(task)
        print("Task deleted successfully")
    else:
        print("Task not found")
def searchTask():
    task = input("Enter a task to search:")
    if task in todo:
        print(f"{task} found")
    else:
        print("Task not found")

menu = """1. Add a new task
          2. View all task
          3. Delete a task
          4. Search for a task
          5. Exit""" #Formatted String

while True:
    print(menu)
    choice = int(input("Enter your choice:"))
    if choice == 1:
        addTask()
    elif choice == 2:
        viewTask()
    elif choice == 3:
        deleteTask()
    elif choice == 4:
        searchTask()
    elif choice == 5:
        print("Exiting the App")