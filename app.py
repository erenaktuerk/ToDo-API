from flask import Flask
from routes import todo_routes

app = Flask(__name__)
app.config.from_object('config.Config')

# register routes
app.register_blueprint(todo_routes, url_prefix='/api/todos')

if __name__ == '__main__':
    app.run(debug=True)