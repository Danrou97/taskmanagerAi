#aqui vamos a trabajar la interface de usuario por CLI

def main ():

    print("\n--- Gestor de tareas Inteligente --- ")
    print("1. Add task")
    print("2. List task")
    print("3. End taks")
    print("4. Delete task")
    print("5. Get out")

    choise = input("Take one option")

    match choise:
        case "1":
            print("Add a new task")
        case "2":
            print("List all tasks")
        case "3":
            print("End task")
        case "4":
            print("Delete task")
        case "5":
            print("Goodbye!")
        case _:
            print("Invalid option")
        



        