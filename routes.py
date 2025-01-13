from flask import Blueprint, jsonify, request
from models import db, TodoItem

todo_routes = Blueprint('todo_routes', __name__)

# get all todos
@todo_routes.route('/', methods=['GET'])
def get_todos():
    todo = TodoItem.query.get_or_404(id)
    return jsonify(todo.to_dict())

# get a todo with its ID
@todo_routes.route('/<int:id>', methods=['GET'])
def get_todo(id):
    todo = TodoItem.query.get.get_or_404(id)
    return jsonify(todo.to_dict())

# create a new todo
@todo_routes.route('/', methods=['POST'])
def create_todo(id):
    data = request.get_json()
    new_todo = TodoItem(title=data['title'], description=data.get('description'))
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201

# edit an existing todo
@todo_routes.route('/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = TodoItem.query.get_or_404(id)
    data = request.get_json()
    todo.title = data['title']
    todo.description = data.get('description')
    todo.completed = data.get('completed', todo.completed)
    db.session.commit()
    return jsonify(todo.to_dict())

# delete a todo
@todo_routes.route('/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = TodoItem.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return'', 204

