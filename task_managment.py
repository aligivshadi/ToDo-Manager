from colorama import Fore, Style, init
import os

dir_path = os.path.join(os.path.expanduser("~"), ".task_manager")
os.makedirs(dir_path, exist_ok=True)
file_path = os.path.join(dir_path, "tasks_manager.txt")

init(autoreset=True)

manager_tasks = {}
# ----------------------------------------
def loadin_file():
    if not os.path.exists(file_path):
        return
    
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.split("|")
            num = line[0]
            task = line[1]
            manager_tasks[num] = task
    return None
# ----------------------------------------

def adding_to_dic():
    user_new_task = input("please enter a task : ")
    if manager_tasks:
        final_key = set()
        for key in manager_tasks.keys():
            key = str(key)
            key = key.strip()
            key = int(key)
            final_key.add(key)
        final_num = max(final_key) + 1
        final_num = str(final_num)
        manager_tasks[final_num] = user_new_task
        print(f"Task {Fore.GREEN}{user_new_task}{Style.RESET_ALL} was successfully added.")
        save_task()

    else:
        manager_tasks['1'] = user_new_task
        print(f"Task {user_new_task} was successfully added.")
        save_task()
    
# ----------------------------------------

def save_task():
    if not os.path.exists(file_path):
        return
    sorted_list()
    with open(file_path, "w") as file:
        for key, value in manager_tasks.items():
            file.write(f"{key}|{value}\n")


# ----------------------------------------

def view_all_task():
    print()
    print(f" - - - > you All tasks < - - - ")
    print(" -------------------------------")
    for key,value in manager_tasks.items():
        print(f" {key} : {value}")

# ----------------------------------------
def delete_tesks():
    try:
        user_delete_tasking = input("please enter number task for delete : ")
        user_delete_tasking = str(user_delete_tasking)
        user_delete_tasking = user_delete_tasking.strip()
        value = manager_tasks[user_delete_tasking]
        manager_tasks.pop(user_delete_tasking, None)
        print(f"Task {Fore.RED}{value}{Style.RESET_ALL} has been successfully{Fore.RED} deleted {Style.RESET_ALL}.")

    except TypeError:
        (print("please enter a number"))
    except KeyError:
        (print(f"{Fore.RED}please enter a number - (1 ... 5){Style.RESET_ALL}"))
    save_task()
# ----------------------------------------
    
def cleare_tasks():
    manager_tasks.clear()
    save_task()
# ----------------------------------------

def sorted_list():
    global manager_tasks
    new_manager_tasks = {}
    counter = 1
    for valu in manager_tasks.values():
        new_manager_tasks[str(counter)] = valu
        counter += 1
    manager_tasks = new_manager_tasks.copy()

