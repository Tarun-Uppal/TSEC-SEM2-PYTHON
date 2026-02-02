tasks = []

print("1-Add Task")
print("2-Remove Task")
print("3-Update Task")
print("4-Sort Tasks")
print("5-View All Tasks")
print("6-Exit")

while True:
    print("Enter your choice (1-6): ", end="")
    choice = int(input())
    
    if choice == 1:
        task_name = input("Enter task name: ")
        priority = input("Enter priority (High/Medium/Low): ")
        task = (task_name, priority)
        tasks.append(task)
        print(f"Task '{task_name}' added!")
    
    elif choice == 2:
        if not tasks:
            print("No tasks to remove!")
        else:
            for i in range(len(tasks)):
                print(f"{i}. {tasks[i][0]} - {tasks[i][1]}")
            print("Enter task number to remove: ", end="")
            idx = int(input())
            if 0 <= idx < len(tasks):
                removed = tasks.pop(idx)
                print(f"Task '{removed[0]}' removed!")
            else:
                print("Invalid task number!")
    
    elif choice == 3:
        if not tasks:
            print("No tasks to update!")
        else:
            for i in range(len(tasks)):
                print(f"{i}. {tasks[i][0]} - {tasks[i][1]}")
            print("Enter task number to update: ", end="")
            idx = int(input())
            if 0 <= idx < len(tasks):
                new_name = input("Enter new task name: ")
                new_priority = input("Enter new priority: ")
                tasks[idx] = (new_name, new_priority)
                print("Task updated!")
            else:
                print("Invalid task number!")
    
    elif choice == 4:
        priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
        tasks.sort(key=lambda x: priority_order.get(x[1], 4))
        print("Tasks sorted by priority!")
    
    elif choice == 5:
        if not tasks:
            print("No tasks available!")
        else:
            print("\n--- All Tasks ---")
            for i in range(len(tasks)):
                print(f"{i}. {tasks[i][0]} - Priority: {tasks[i][1]}")
    
    elif choice == 6:
        print("Exit!")
        break
    
    else:
        print("Invalid choice! Try again.")