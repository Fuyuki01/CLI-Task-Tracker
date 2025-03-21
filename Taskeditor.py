import json
import os

tasks_lists = "todolist.json"

def list_all_tasks(): 
    try:
        with open(tasks_lists) as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        return []


def list_tasks_done():
    tasks_done = []
    try:
        with open(tasks_lists) as file:
            tasks = json.load(file)
        for task in tasks:
            if task['status'] == "done":
                tasks_done.append(task)
        return tasks_done
    except FileNotFoundError:
        return []


def list_tasks_notdone():
    tasks_notdone = []
    try:
        with open(tasks_lists) as file:
            tasks = json.load(file)
        for task in tasks:
            if task['status'] == "todo":
                tasks_notdone.append(task)
        return tasks_notdone
    except FileNotFoundError:
        return []


def list_task_inprogress():
    tasks_inprogress = []
    try:
        with open(tasks_lists) as file:
            tasks = json.load(file)
        for task in tasks:
            if task['status'] == "in-progress":
                tasks_inprogress.append(task)
        return tasks_inprogress
    except FileNotFoundError:
        return []


def add_task(description):
    try:
        if description:
            tasks = list_all_tasks()

            new_task = {
                "id": len(tasks) + 1,
                "task": description,
                "status": "todo"
            }

            tasks.append(new_task)

            with open(tasks_lists, "w") as file:
                json.dump(tasks, file, indent=4)

            print(f"task added sucesfully {new_task['id']}")
    except:
        print(f"couldn't add {description} to do list")

def update_task(id, description):
    try:
        tasks = list_all_tasks()
        updated = False

        try:
            task_id = int(id)
        except ValueError:
            task_id = None

        for task in tasks:
            if (task_id is not None and task['id'] == task_id) or (task['task'] == id):
                task['task'] = description
                updated = True
        if updated:
            print("the task has updated")
            with open(tasks_lists, "w") as file:
                json.dump(tasks, file, indent=4)

    except Exception as e:
        print(f"Error updating task: {e}")


def delete_task(description):
    try:
        if description:
            tasks = list_all_tasks()
            tasks_length = len(tasks)
            for task in tasks:
                if task['task'].lower() == description.lower() or task['id'] == int(description):
                    tasks.remove(task)
                    print(f"removed the {description} from the list")
            if len(tasks) == tasks_length:
                print(f"couldn't found {description}")
    
            for index, task in enumerate(tasks, start=1):
                task['id'] = index

            with open(tasks_lists, "w") as file:
                json.dump(tasks, file, indent=4)
    except:
        print(f"couldn't remove {description} from the list")


def mark_tasks(status, id):
    try:
        if status in ["mark-done", "mark-in-progress"]:
            tasks = list_all_tasks()
            updated = False
            try:
                task_id = int(id)
            except ValueError:
                task_id = None

            for task in tasks:
                if (task_id is not None and task['id'] == task_id) or (task['task'] == id):
                    if status == "mark-done":
                        task['status'] = "done"
                    elif status == "mark-in-progress":
                        task['status'] = "in-progress"
                    updated = True
            if updated:
                print("status has updated")
                with open(tasks_lists, "w") as file:
                    json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error updating task: {e}")

def main():
    print("type h for help")
    commands = {
        "list": list_all_tasks,
        "list-done": list_tasks_done,
        "todo": list_tasks_notdone,
        "in-progress": list_task_inprogress
    }
    while True:
        command = input("% ").strip().split(" ", 2)
        action = command[0]
        argument = command[1] if len(command) > 1 else None
        extra_argument = command[2] if len(command) > 2 else None

        if not command:
            continue
        elif action in commands:
            tasks = commands[action]()
            for task in tasks:
                print(f"id: {task['id']}, task: {task['task']}, status: {task['status']}")  
        elif action == "add":
            add_task(" ".join(command[1:]))
        elif action == "remove":
            if argument:
                delete_task(" ".join(command[1:]))
        elif action in ["mark-done", "mark-in-progress"]:
                if argument:
                    mark_tasks(action, " ".join(command[1:]))
        elif action == "update":
            if argument and extra_argument:
                update_task(argument,extra_argument)
        elif action in ["leave", "quit", "clear"]:
            print("closing cli")
            break


if __name__ == "__main__":
    main()
