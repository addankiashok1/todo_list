from flask import Flask, render_template, request, redirect, url_for, jsonify
from db import db
from models import Todo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

# Add the rest of your routes here...

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
