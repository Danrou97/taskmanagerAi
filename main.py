#aqui vamos a trabajar la interface de usuario por CLI

from task_manager import TaskManager

def print_menu():
    print("\n--- Gestor de tareas Inteligente --- ")
    print("1. Add task")
    print("2. List task")
    print("3. Complite taks")
    print("4. Delete task")
    print("5. Get out")




def main():

    manager =  TaskManager()

    try:
        while True:      
            print_menu()
            choise = int (input("Take one option: "))

            match choise:
                case 1:
                    description = input("Discribe your task: ")
                    manager.add_task(description)
                case 2:
                    manager.list_tasks()
                    
                case 3:
                    id = int(input("write the target id: "))
                    manager.complete_task(id)
                    
                    
                case 4:
                    id = int(input("write the target id: "))
                    manager.delete_task(id)
                    
                case 5:
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid option")
    except ValueError as e:
        print(f"Error: {e}, choose other option")
               

if __name__ == "__main__":
    main()
        