import os

TASK_FILE = 'tasks.txt'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    
    with open(TASK_FILE, 'r') as file:
        return file.readlines()
    
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        return file.writelines(tasks)
    
def add_task(task):
    tasks = load_tasks()
    tasks.append(task + '\n')
    save_tasks(tasks)
    print(f'Task added: {task}')

def remove_task(task_number):
    tasks = load_tasks()
    if 0 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Task removed: {removed.strip()}')
    else:
        print(f'Invalid task number!')

def list_tasks():
    tasks = load_tasks()
    if tasks:
        print('\n To-Do Lists:')
        for i, task in enumerate(tasks, start=1):
            print(f'{i}. {task.strip()}')
    else:
        print('\n No tasks found')

def main():
    while True:
        print('\n Choose an option:')
        print('1. Add Task')
        print('2. Remove Task')
        print('3. List Tasks')
        print('4. Exit')
        choice = input('Enter your choice: ')
        
        if choice == '1':
            task = input('Enter the task: ')
            add_task(task)
        elif choice == '2':
            list_tasks()
            task_number = int(input('Enter task number to remove: '))
            remove_task(task_number)
        elif choice == '3':
            list_tasks()
        elif choice == '4':
            print('Exiting... Have a productive day!')
            break
        else:
            print('Invalid choice! Please try again.')

if __name__ == '__main__':
    main()