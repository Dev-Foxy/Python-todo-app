# first we need to create a variable that will store our todo

todoList = []

# function for adding todos

def addTodo(item):
    todoList.append(item)
    print("Item added to the list")

# function for removing todos

def removeTodo(item):
    todoList.remove(item)
    print("Item removed from the list")

# function for displaying item

def displayTodo():
    print("Here are the lists")
    for item in todoList:
        print(item)


# Now the main part

while True:
    print("What you want to do?")
    print("1. Add an item to the list")
    print("2. Remove an item from the list")
    print("3. Display all item in the list")
    print("4. Quit from the program")
    choice = input("Enter your choice (1-4): ")

    # conditions
    if choice == "1":
        item = input("Enter an item to add to the list: ")
        addTodo(item)
    elif choice == "2":
        item = input("Enter an item to remove from the list: ")
        removeTodo(item)
    elif choice == "3":
        displayTodo()
    else:
        break