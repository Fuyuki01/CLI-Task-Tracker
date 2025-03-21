# CLI Task Manager

A simple interactive command-line task manager to **add, delete, update, and manage tasks** stored in a **JSON file**. This tool helps users organize their to-do lists efficiently using basic commands.

---

## Features

Add new tasks  
Delete tasks by **ID** or **name**  
Update task descriptions  
Mark tasks as **done** or **in progress**  
List tasks by status: **all, done, in progress, to-do**  
Persistent storage using a **JSON file**  

---
### Clone the repository
```bash
git clone https://github.com/Fuyuki01/CLI-Task-Tracker.git
cd CLI-Task-Tracker
```
---

## Running the Program
Once inside the project folder, run:
```
python Taskeditor.py
```

## Usage

### 📌 Adding a Task
```
add Buy groceries
```
**Output:**
```
Task added successfully (ID: 1)
```

### 📌 Listing All Tasks
```
list
```
**Output:**
```
ID: 1, Task: Buy groceries, Status: todo
```

### 📌 Marking a Task as Done
```
mark-done 1
```
**Output:**
```
Task 1 updated to 'done'
```

### 📌 Updating a Task
```
update 1 Buy groceries and cook dinner
```
or
```
update task name Buy groceries and cook dinner
```
**Output:**
```
Task 1 updated successfully.
```

### 📌 Deleting a Task
```
delete Buy groceries
```
or
```
delete 1
```
**Output:**
```
Task 'Buy groceries' removed successfully.
```

### 📌 Exiting the CLI
```
quit
clear
leave
```

---

---
## Project URLs
https://github.com/Fuyuki01/CLI-Task-Tracker
https://roadmap.sh/projects/task-tracker
