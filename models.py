from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500))
    completed = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<TodoItem {self.title}>'