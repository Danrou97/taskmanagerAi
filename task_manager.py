#en este archivo se encuentra la clase TaskManager, que se encarga de gestionar las tareas del sistema, incluyendo la creación, eliminación y actualización de tareas.
import json


class Task:
    def __init__(self, id, description, completed = False):
        self.id = id
        self.description = description
        self.completed = completed

    # Redefinimos la funcion __str__

    def __str__(self):
        status = "✔ " if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"
    

class TaskManager :
    FILENAME = "task.json" # En el futuro la persistencia debe venier de una DB SQL o NoneSQL
    def __init__(self):
        self._tasks = [] #en el futuro deberiamos usar dics 
        self._next_id = 1
        self.load_tasks()



    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id +=1
        self.save_tasks()
        print(f"Task has been added: {description} with id: {task.id}") # en el futuro deberian ser logs 

    def list_tasks(self):
        if not self._tasks:
            print("You don't have any pending task ")

        else:
            for tsk in self._tasks:
                print(tsk)
    
    def complete_task(self, id):
        for tsk in self._tasks:
            if tsk.id == id:
                tsk.completed = True 
                self.save_tasks()
                print(f"Task finished: {tsk}")
                return
        print (f"Task don't find: #{id}")


    def delete_task(self, id):
        for tsk in self._tasks:
            if tsk.id == id:
                description = tsk.description
                self._tasks.remove(tsk) 
                self.save_tasks()
                print(f"Task has been deleted: #{id}: {description}")
                return
        print (f"Task don't find:#{id}")

    # crearemos la persistencia de el programa

    def load_tasks(self):
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
                self._tasks = [Task(item["id"], item["description"], item["completed"]) for item in data]
                if self._tasks:
                    self._next_id = self._tasks[-1].id + 1
        except FileNotFoundError:
            self._tasks = []

    def save_tasks(self):
        try:
            with open(self.FILENAME, "w") as file:
                json.dump([{"id": task.id , "description" : task.description, "completed" : task.completed  } for task in self._tasks], file, indent= 4 )
                
        except FileNotFoundError as e :
            print("Error as : {e} ")