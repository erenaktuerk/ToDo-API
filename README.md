ToDo API

A simple and efficient RESTful API built with Python and Flask to manage tasks (ToDos). This project is designed as a learning exercise and provides full CRUD (Create, Read, Update, Delete) operations for ToDo items.

Table of Contents
	1.	Features
	2.	Getting Started
	•	Prerequisites
	•	Installation
	3.	Usage
	4.	API Endpoints
	5.	Project Structure
	6.	Contributing
	7.	License

Features
	•	Full CRUD functionality for managing tasks:
	•	Add a new ToDo
	•	Retrieve all tasks or a single task
	•	Update an existing task
	•	Delete a task
	•	RESTful API design for simplicity and scalability.
	•	Built with Python and Flask.

Getting Started

Prerequisites

Make sure you have the following installed:
	•	Python (>= 3.7)
	•	pip (Python package installer)

You can verify the installations by running:

python --version
pip --version

Installation
	1.	Clone the repository to your local machine:

git clone https://github.com/erenaktuerk/todo-api.git
cd todo-api


	2.	Install the required Python packages:

pip install flask


	3.	Run the Flask application:

python app.py


	4.	The API will be available at http://127.0.0.1:5000/.

Usage

You can interact with the API using tools like Postman, cURL, or any REST client. Below are the available endpoints.

API Endpoints

1. Get all ToDos
	•	URL: /todos
	•	Method: GET
	•	Description: Retrieve a list of all ToDo items.
	•	Response Example:

[
  {
    "id": 1,
    "title": "Buy groceries",
    "completed": false
  }
]



2. Get a single ToDo
	•	URL: /todos/<id>
	•	Method: GET
	•	Description: Retrieve a specific ToDo item by its ID.
	•	Response Example:

{
  "id": 1,
  "title": "Buy groceries",
  "completed": false
}



3. Create a new ToDo
	•	URL: /todos
	•	Method: POST
	•	Request Body:

{
  "title": "Clean the house",
  "completed": false
}


	•	Description: Add a new ToDo item.
	•	Response Example:

{
  "id": 2,
  "title": "Clean the house",
  "completed": false
}

4. Update a ToDo
	•	URL: /todos/<id>
	•	Method: PUT
	•	Request Body:

{
  "title": "Clean the house",
  "completed": true
}


	•	Description: Update an existing ToDo item by its ID.
	•	Response Example:

{
  "id": 2,
  "title": "Clean the house",
  "completed": true
}

5. Delete a ToDo
	•	URL: /todos/<id>
	•	Method: DELETE
	•	Description: Delete a ToDo item by its ID.
	•	Response Example:

{
  "message": "ToDo deleted successfully"
}

Project Structure

The project has the following structure:

todo-api/
├── app.py            # Main Flask application
├── README.md         # Project documentation
├── requirements.txt  # (Optional) Dependencies file

Contributing

Contributions are welcome! If you’d like to improve this project:
	1.	Fork the repository.
	2.	Create a new branch:

git checkout -b feature-name


	3.	Make your changes and commit them:

git commit -m "Add some feature"


	4.	Push to the branch:

git push origin feature-name


	5.	Open a Pull Request.

License

This project is licensed under the MIT License - see the LICENSE file for details.
