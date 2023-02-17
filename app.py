# Importing the required libraries
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialsed app
app = Flask(__name__)

# Set the database name in app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Database access provided
db = SQLAlchemy(app)


# Database model for Todo table contains id(primary key), content, completed(check), dat
class Todo(db.Model):
    # id of a task and primary key(unique)
    # content of the task to be done, can't be empty
    # completed is a flag to check if task is completed(initialised to 0)
    # date_time stores time and date when the task was created
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)

    # def __repr__(self):
    #     return '<Task %r>' % self.id


# Initial entry point of the application, POST and GET both requests allowed
@app.route('/', methods=['POST', 'GET'])
def index():
    if (request.method == 'POST'):
        # if the request is POST that means a new task is added
        task_content = request.form['content']
        if(task_content == ""):
            # content should not be empty
            print("Empty task is not allowed")
            return redirect('/')
        new_task = Todo(content=task_content)
        try:
            # add the new task to database
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            # if not added return adding error
            return "There was an issue adding your task"
    else:
        # if GET request print all the tasks sorted by creation date from old to new
        tasks = Todo.query.order_by(Todo.date_time).all()
        return render_template('index.html', tasks=tasks)


# Function to mark any task done
@app.route('/done/<int:id>', methods=['POST', 'GET'])
def done(id):
    if (request.method == 'POST'):
        # print(id)
        # id is taken and the completed column is updated
        task = Todo.query.get_or_404(id)
        # if task is marked done, unmark it and vice versa
        task.completed = 1-task.completed
        try:
            # commit changes to database
            db.session.commit()
            # print("done")
            return redirect('/')
        except:
            # if not changed return error
            return "There was an issue in marking the task"
    else:
        tasks = Todo.query.order_by(Todo.date_time).all()
        return render_template('index.html', tasks=tasks)


# api to delete a particular task using its id
@app.route('/delete/<int:id>')
def delete(id):
    # id is passed when task is to be deleted
    task_to_delete = Todo.query.get_or_404(id)
    try:
        # delete the task from database
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        # if not able to delete return error
        return "There was a problem deleting that task"


# api to update a particular task using its id
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    # id is passed when task is to be updated
    task = Todo.query.get_or_404(id)
    if (request.method == 'POST'):
        # new content is taken from the form
        task_content = request.form['content']
        if(task_content == ""):
            # updated content should not be empty
            print("Empty task is not allowed")
            return redirect("/update/"+str(id))
        task.content = task_content
        try:
            # commit changes to database
            db.session.commit()
            return redirect('/')
        except:
            # if no changes commited due to some error print message
            return "There was an issue updating your task"
    else:
        return render_template('update.html', task=task)


# if (__name__ == "main"):
    # run the application(server)
app.run(host='0.0.0.0', port=80)
