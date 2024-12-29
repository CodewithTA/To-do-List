tasks = []
file_name = "ToDoList.txt"

menu_list = ["View", "Delete", "Add", "Edit", "Exit"]

while True:
    print("\nMenu:")
    for index, menu_item in enumerate(menu_list):
        print(f"{index + 1}. {menu_item}")
    
    menu = input("\nWhat do you want to do today? Select from the list: ").capitalize()

    if menu == "View":
        try:
            with open(file_name, "r") as tdl:
                tasks = [line.strip() for line in tdl]

            if not tasks:
                print("No tasks found in your To-Do list.")
            else:
                print("\nTasks which need to be done today are:\n")
                for index, task in enumerate(tasks):
                    print(f"Task {index + 1}: {task}")

        except FileNotFoundError:
            answer = input("You haven't added any tasks! Do you want to add some? (yes/no): ").lower()
            if answer == "yes":
                while True:
                    input_tasks = input("Enter your task (type \"done\" to finish): ").strip()
                    if input_tasks.capitalize() == "Done":
                        break
                    tasks.append(input_tasks)

                with open(file_name, "w") as tdl:
                    for task in tasks:
                        tdl.write(task + "\n")
                print("Your tasks are added. Thank you!")
            else:
                print("Returning to the main menu.")

    elif menu == "Delete":
        try:
            with open(file_name, "r") as tdl:
                tasks = [line.strip() for line in tdl]

            if not tasks:
                print("\nNo tasks to delete. Your To-Do list is empty.")
            else:
                print("\nTasks which need to be done today are:\n")
                for index, task in enumerate(tasks):
                    print(f"Task {index + 1}: {task}")

                while True:
                    indices = input(
                        "Enter the task numbers to be deleted (e.g., 1,2,3 or type 'done' to exit): "
                    ).strip()
                    if indices.lower() == "done":
                        print("Thank you! Returning to the main menu.\n")
                        break

                    try:
                        indices = [int(i) for i in indices.split(",")]
                        if all(1 <= idx <= len(tasks) for idx in indices):
                            for idx in sorted(indices, reverse=True):
                                deleted_task = tasks.pop(idx - 1)
                                print(f"Task '{deleted_task}' has been deleted.")

                            print("\nUpdated list of tasks:")
                            for index, task in enumerate(tasks):
                                print(f"Task {index + 1}: {task}")

                            with open(file_name, "w") as tdl:
                                for task in tasks:
                                    tdl.write(task + "\n")
                            break
                        else:
                            print("\nInvalid task numbers. Please enter numbers within the valid range.")
                    except ValueError:
                        print("\nInvalid input. Please enter valid task numbers separated by commas.")

        except FileNotFoundError:
            print("\nThe To-Do list file does not exist. Add tasks first before trying to delete.")

    elif menu == "Add":
        while True:
            input_tasks = input("Enter your task (type \"done\" to finish): ").strip()
            if input_tasks.capitalize() == "Done":
                break
            tasks.append(input_tasks)

        with open(file_name, "w") as tdl:
            for task in tasks:
                tdl.write(task + "\n")
        
        print("\nCurrent tasks:")
        for index, task in enumerate(tasks):
            print(f"Task {index + 1}: {task}")

    elif menu == "Edit":
        try:
            with open(file_name, "r") as tdl:
                tasks = [line.strip() for line in tdl]

            if not tasks:
                print("\nNo tasks found to edit. Your To-Do list is empty.")
            else:
                print("\nTasks which need to be done today are:\n")
                for index, task in enumerate(tasks):
                    print(f"Task {index + 1}: {task}")

                task_number = input("Enter the task number you want to edit: ").strip()
                try:
                    task_number = int(task_number)
                    if 1 <= task_number <= len(tasks):
                        new_task = input("Enter the new task: ").strip()
                        tasks[task_number - 1] = new_task
                        print(f"Task {task_number} has been updated to: {new_task}")

                        with open(file_name, "w") as tdl:
                            for task in tasks:
                                tdl.write(task + "\n")
                    else:
                        print("\nInvalid task number. Please try again.")
                except ValueError:
                    print("\nInvalid input. Please enter a valid task number.")

        except FileNotFoundError:
            print("\nThe To-Do list file does not exist. Add tasks first before trying to edit.")

    elif menu == "Exit":
        print("Thank you for using the To-Do List App. Have a great day!")
        break

    else:
        print("Invalid choice! Please select a valid option from the menu.")
