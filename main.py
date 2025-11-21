import task_managment
import colorama 

introfuction = print(f"""{colorama.Fore.LIGHTGREEN_EX}-------------------------------------------
{colorama.Style.RESET_ALL}  Hello! Welcome to{colorama.Fore.LIGHTGREEN_EX} Ali Givshadi{colorama.Style.RESET_ALL}’s Task Manager.
    I hope you find it useful.
{colorama.Fore.LIGHTGREEN_EX}-------------------------------------------{colorama.Style.RESET_ALL} """)

intro = f"""{colorama.Fore.GREEN}--->{colorama.Style.RESET_ALL} 1. Add task
{colorama.Fore.GREEN}--->{colorama.Style.RESET_ALL} 2. Delete task
{colorama.Fore.GREEN}--->{colorama.Style.RESET_ALL} 3. View all tasks
{colorama.Fore.GREEN}--->{colorama.Style.RESET_ALL} 4. clean tasks list
{colorama.Fore.GREEN}--->{colorama.Style.RESET_ALL} 5. Exit"""

def main():
    introfuction
    while True:
        print(intro)
        user_command = input(f"{colorama.Fore.LIGHTBLUE_EX}-------------> {colorama.Style.RESET_ALL}{colorama.Fore.LIGHTBLUE_EX}please selecte a work{colorama.Style.RESET_ALL}{colorama.Fore.GREEN} : {colorama.Style.RESET_ALL}")
        user_command = str(user_command)
        user_command = user_command.strip()
        if user_command == "1":
            task_managment.loadin_file()
            task_managment.adding_to_dic()
        elif user_command == "2":
            task_managment.loadin_file()
            task_managment.delete_tesks()
        elif user_command == "3":
            task_managment.loadin_file()
            task_managment.view_all_task()
        elif user_command == "4":
            task_managment.loadin_file()
            task_managment.cleare_tasks()
        elif user_command == "exit":
            print(f"-> I’ll be waiting for you to {colorama.Fore.GREEN}come back. {colorama.Style.RESET_ALL}See you for now.")
            break
        elif user_command == "5":
            print(f"-> I’ll be waiting for you to {colorama.Fore.GREEN}come back. {colorama.Style.RESET_ALL}See you for now.")
            break
        print()


if __name__ == '__main__':
    
    main()