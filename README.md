# TaskManager AI

## Description

TaskManager AI is a command-line interface (CLI) application for intelligently managing tasks. It allows adding, listing, completing, and deleting tasks, with persistence in a JSON file. Additionally, it integrates artificial intelligence (using OpenAI) to break down complex tasks into simple and actionable subtasks.

This project is ideal for learning about task management, data persistence, and integration with AI APIs.

## Features

- **Add tasks**: Create new tasks with a description.
- **List tasks**: Display all pending and completed tasks.
- **Complete tasks**: Mark a task as completed by its ID.
- **Delete tasks**: Delete a task by its ID.
- **Persistence**: Tasks are automatically saved in a `task.json` file.
- **AI Assistance**: Uses OpenAI to divide complex tasks into simple subtasks.
- **CLI Interface**: Easy to use from the terminal.

## Project Structure

- `main.py`: Application entry point, handles the CLI user interface.
- `task_manager.py`: Contains the `Task` and `TaskManager` classes to manage tasks.
- `ai_service.py`: Handles integration with OpenAI to generate subtasks.
- `requirements.txt`: List of Python dependencies.
- `task.json`: Persistence file for tasks (generated automatically).
- `README.md`: This documentation file.

## Requirements

- Python 3.8 or higher.
- An OpenAI API key (configured in a `.env` file).

## Installation

1. Clone or download the repository.

2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

   Note: The current `requirements.txt` file may not include all dependencies. Make sure to also install:
   - `openai`
   - `python-dotenv`

   You can install them manually:
   ```
   pip install openai python-dotenv
   ```

3. Configure your OpenAI API key:
   - Create a `.env` file in the project root.
   - Add your API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Select an option from the menu:
   - 1: Add task (enter the description).
   - 2: List tasks.
   - 3: Complete task (enter the ID).
   - 4: Delete task (enter the ID).
   - 5: Exit.

### Usage Example

```
--- Intelligent Task Manager ---
1. Add task
2. List task
3. Complete task
4. Delete task
5. Get out
Take one option: 1
Describe your task: Prepare presentation for the project
Task has been added: Prepare presentation for the project with id: 1
```

## AI Functionality

The `create_simple_task` function in `ai_service.py` uses OpenAI to break down a complex task into 3-5 subtasks. For example:

- Task: "Prepare presentation for the project"
- Generated subtasks:
  - Research the topic
  - Create slides
  - Practice the presentation
  - etc.

Note: Currently, this functionality is not integrated into the main menu, but it can be extended.

## Contribution

If you want to contribute:
1. Fork the project.
2. Create a branch for your feature.
3. Send a pull request.

## License

This project is open source. Check the license file if applicable.

## Future Improvements

- Integrate AI functionality into the main menu.
- Change persistence to a database (SQL or NoSQL).
- Improve the user interface (GUI or web).
- Add more functionalities like priorities, deadlines, etc.
- Use local AI models like Ollama instead of OpenAI.

## Contact

For questions or suggestions, contact the developer.