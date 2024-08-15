# Flask To-Do List Application

## Description

This is a simple To-Do List application built using Flask, Flask-RESTful, and SQLAlchemy. It allows users to manage their tasks with functionalities to add, update, delete, and view tasks.

## Features

- **Add Tasks**: Add new tasks with a description and summary.
- **Update Tasks**: Update existing tasks.
- **Delete Tasks**: Remove tasks from the list.
- **View Tasks**: View all tasks associated with a specific user.

## Technologies Used

- **Flask**: Web framework for Python.
- **Flask-RESTful**: Extension for Flask that adds support for quickly building REST APIs.
- **Flask-SQLAlchemy**: SQLAlchemy integration for Flask.
- **SQLite**: Lightweight database used for storing tasks.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**

    ```bash
    python app.py
    ```

    The application will be accessible at `http://127.0.0.1:5000/`.

## Application Structure

- `app.py`: The main application file where Flask routes and API resources are defined.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory containing static files such as CSS.
- `requirements.txt`: File listing required Python packages.

## Web Interface


## RESTful API

- **GET `/todos`**: Retrieve all tasks.
- **GET `/todos/<int:todo_id>`**: Retrieve a specific task by ID.
- **POST `/todos/<int:todo_id>`**: Create a new task.
- **PUT `/todos/<int:todo_id>`**: Update an existing task.
- **DELETE `/todos/<int:todo_id>`**: Delete a task.

## Contributing

Feel free to fork the repository and submit pull requests. For any issues or feature requests, please open an issue on GitHub.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
