tasks = []

def show_menu():
    print("=======TO DO LIST APP=======")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Delete Tasks")
    print("4. Exit")

def view_tasks():
    if not tasks:
      print("\nYour to do list is empty")
      return

    print("\nYour Tasks: ")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def add_task():
    new_task = input("\nEnter the task you want to add: ").strip()
    if new_task:
        tasks.append(new_task)
        print(f"'{new_task}'has been added to the list")

    else:
         print("Task cannot be empty")

def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
      task_num = int(input("\nEnter the task number you want to delete: "))
      if 1<=task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"{removed} removed form list")

      else:
          print("Invalid task number")

    except ValueError:
      print("Enter a valid number")

def main():
    print("Welcome to your to do list app")

    while True:
        show_menu()
        choice = input("Choose an option 1-4: ").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!! Have a great day")
            break
        else:
             print("Enter a valid number from 1-4")

if __name__ == "__main__":
    main()












