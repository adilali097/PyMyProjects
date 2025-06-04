def main():
    while True:
        print("\nTo-Do List Options:\n1. Add Task\n2. View Tasks\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a task: ")
            with open("tasks.txt", "a") as f:
                f.write(task + "\n")
        elif choice == '2':
            try:
                with open("tasks.txt", "r") as f:
                    tasks = f.readlines()
                    if not tasks:
                        print("No tasks found.")
                    for i, task in enumerate(tasks):
                        print(f"{i + 1}. {task.strip()}")
            except FileNotFoundError:
                print("No tasks file found.")
        elif choice == '3':
            break
        else:
            print("Invalid option")

if __name__ == '__main__':
    main()
