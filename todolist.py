to_do_list = []


# Function to add tasks to the list
def add(task):
    to_do_list.append(task)
    print("Task Added!!!")


# Function to remove task from list
def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print("Task Removed!!!")
    else:
        print("Task not found")


# Function to display list
def display():
    if len(to_do_list) == 0:
        print("Your tto-do list is empty.")
    else:
        print("Your to do list:")
        for task in to_do_list:
            print("-" + task)


# Test the FUnction
print("Enter you to do list")
add_task = input("-")
add(add_task)
display()

remove = input("Enter your task name to remove from to-do list")
remove_task(remove)

