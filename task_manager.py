#en este archivo se encuentra la clase TaskManager, que se encarga de gestionar las tareas del sistema, incluyendo la creación, eliminación y actualización de tareas.

class Task:
    def __init__(self, id, description, completed = False):
        self.id = id
        self.description = description
        self.completed = completed

    # Redefinimos la funcion __str__

    def __str__(self):
        status = "✔" if self.comppleted else " "
        return f"[{status}] #{self.id}: {self.description}"
    

class TaskManager :

    def __init__(self):
        self._tasks = [] #en el futuro deberiamos usar dics 
        self._next_id = 1
    
    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id +=1
        print(f"Task has been added: {description} with id: {task.id}") # en el futuro deberian ser logs 

    def list_tareas(self):
        if not self._tasks:
            print("You don't have any pending task ")

        else:
            for tsk in self._tasks:
                print(tsk)
    
    def complete_task(self, id):
        for tsk in self._tasks:
            if tsk.id == id:
                tsk.completed = True 
                print(f"Task finished: {tsk}")
                return
        print (f"Task don't find: #{id}")
    def delete_task(self, id):
        for tsk in self._tasks:
            if tsk.id == id:
                description = tsk.description
                self._tasks.remove(tsk) 
                print(f"Task has been deleted: #{id}: {description}")
                return
        print (f"Task don't find:#{id}")