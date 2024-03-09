tasks = []

def add_task(task):
  tasks.append(task)

def remove_task(task):
  if task in tasks:
    tasks.remove(task)
  else:
    print("Task not found.")

def delete_all_tasks():
  tasks.clear()

def view_all_tasks():
  if not tasks:
    print("No tasks to display.")
  else:
    for i, task in enumerate(tasks, start=1):
      print(f"{i}. {task}")

while True:
  print("ToDo List Menu(Made by suhail):")
  print("1. Add Task")
  print("2. Remove Task")
  print("3. Delete All Tasks")
  print("4. View All Tasks")
  print("5. Exit")

  choice = input("\nEnter your choice: ")

  if choice == "1":
    task = input("\nEnter task: ")
    add_task(task)
  elif choice == "2":
    task = input("\nEnter task to remove: ")
    remove_task(task)
  elif choice == "3":
    delete_all_tasks()
  elif choice == "4":
    view_all_tasks()
  elif choice == "5":
    print("Exiting ToDo List.")
    break
  else:
    print("Invalid choice. Please try again.")
