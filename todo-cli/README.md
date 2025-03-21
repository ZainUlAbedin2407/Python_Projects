# 📝 Todo List CLI  

A simple command-line-based Todo List application built using **Click** for CLI functionality and **UV** for efficiency. Manage your daily tasks with ease!  

## 🚀 Features  
- Add new tasks ✅  
- List all tasks 📋  
- Mark tasks as completed 🔄  
- Delete tasks ❌  
- Tasks persist in a JSON file 💾  

## 📦 Installation  
Ensure you have Python installed, then install dependencies:  
```sh
pip install click uv
```  

## 🛠 Usage  
Run the application using the following commands:  

### Add a Task  
```sh
python todo.py add "Your Task Here"
```  
**Example:**  
```sh
python todo.py add "Complete Python project"
python todo.py add "Buy groceries"
python todo.py add "Read a book"
```  

### List All Tasks  
```sh
python todo.py list
```  
**Example Output:**  
```sh
1. Complete Python project [❌]  
2. Buy groceries [❌]  
3. Read a book [❌]  
```  

### Mark a Task as Completed  
```sh
python todo.py complete <task_number>
```  
**Example:**  
```sh
python todo.py complete 1
```  
**Example Output:**  
```sh
Task 1 marked as completed.  
```  

### Delete a Task  
```sh
python todo.py delete <task_number>
```  
**Example:**  
```sh
python todo.py delete 2
```  
**Example Output:**  
```sh
Task Buy groceries has been deleted.  
```  

## 📂 Data Storage  
Tasks are stored in `todo.json`, ensuring persistence across sessions.  

Happy Task Management! 🎯  