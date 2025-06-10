import mysql.connector # type: ignore

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bhavika@sql12",
    database="todo_db"
)
cursor = conn.cursor()


def add_task(title):
    if title.strip():
        cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
        conn.commit()
        print("Task added successfully!")
    else:
        print("Title cannot be empty.")

def view_tasks():
    cursor.execute("SELECT id, title, status FROM tasks")
    tasks = cursor.fetchall()
    if tasks:
        for row in tasks:
            print(f"{row[0]}. {row[1]} - {row[2]}")
    else:
        print("No tasks found.")

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    print("Task deleted successfully!")

def complete_task(task_id):
    cursor.execute("UPDATE tasks SET status = 'Completed' WHERE id = %s", (task_id,))
    conn.commit()
    print("Task marked as completed!")

def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '3':
            task_id = input("Enter task ID to mark as completed: ")
            complete_task(task_id)
        elif choice == '4':
            task_id = input("Enter task ID to delete: ")
            delete_task(task_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()
    print("Goodbye!")

if __name__ == "__main__":
    main()