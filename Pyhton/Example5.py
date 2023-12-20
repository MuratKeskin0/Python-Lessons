# Creating an empty To-Do list
to_do_list = []

# Function to add user input to the list
def add_task(to_do_list):
    task = input("Enter a task: ")
    to_do_list.append(task)
    print("Task added successfully.")

# Function to show tasks in the list
def show_tasks(to_do_list):
    print("Tasks to do: ")
    for task in to_do_list:
        print("- " + task)

# Function to delete a task from the list
def delete_task(to_do_list):
    task = input("Enter the task to delete: ")
    if task in to_do_list:
        to_do_list.remove(task)
        print("Task deleted successfully.")
    else:
        print("Task not found.")
        
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Your choice (1/2/3/4): ")
    
    if choice == "1":
        add_task(to_do_list)
    elif choice == "2":
        show_tasks(to_do_list)
    elif choice == "3":
        delete_task(to_do_list)
    elif choice == "4":
        print("Exiting the application...")
        break
    else:
        print("Invalid choice. Please try again.")
