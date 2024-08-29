import os
import argparse

workspace_dir = os.path.join(os.getcwd(), 'task_records')
os.makedirs(workspace_dir, exist_ok=True)
TASK_FILE_PATH = os.path.join(workspace_dir, 'task_list.txt')

def fetch_tasks():
    if not os.path.exists(TASK_FILE_PATH) or os.path.getsize(TASK_FILE_PATH) == 0:
        return []
    with open(TASK_FILE_PATH, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    with open(TASK_FILE_PATH, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def insert_task(description):
    tasks = fetch_tasks()
    tasks.append(description)
    save_tasks(tasks)
    print(f'Task added successfully: "{description}"')

def show_tasks():
    tasks = fetch_tasks()
    if not tasks:
        print('No tasks available.')
        return
    for i, task in enumerate(tasks, 1):
        print(f'{i}. {task}')

def finalize_task(task_num):
    tasks = fetch_tasks()
    if 0 < task_num <= len(tasks):
        finished_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f'Task completed: "{finished_task}"')
    else:
        print(f'Invalid task number: {task_num}')

def remove_task(task_num):
    tasks = fetch_tasks()
    if 0 < task_num <= len(tasks):
        deleted_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f'Task removed: "{deleted_task}"')
    else:
        print(f'Invalid task number: {task_num}')

parser = argparse.ArgumentParser(description='Task Management Tool')
parser.add_argument('--insert', help='Insert a new task')
parser.add_argument('--show', action='store_true', help='Display all tasks')
parser.add_argument('--finalize', type=int, help='Mark a task as completed by number')
parser.add_argument('--remove', type=int, help='Delete a task by number')

args = parser.parse_args()

if args.insert:
    insert_task(args.insert)
elif args.show:
    show_tasks()
elif args.finalize:
    finalize_task(args.finalize)
elif args.remove:
    remove_task(args.remove)
else:
    parser.print_help()
