from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from EncryptIt import encoder
from EncryptIt import decoder

app = Flask(__name__)

####    Dependancies for DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'     #can be 'sqlite:////<path for database>'
db = SQLAlchemy(app)

#####   Model for DATABASE

class Todo(db.Model):
    # columns in the table of todo list
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    
    #completed = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # returns a string, every time as a new element is created
    def __repr__(self):
        return '<Task %r>' %self.id

#####   Ends Model



@app.route('/', methods=['POST', 'GET'])        # methods (a list) = adds 2 methods that app can accept --> GET is default
def index():
    # form handling
    if request.method == 'POST':
        task_content = request.form['content']   # grab data from form using 'ID-Name'
        task_content = encoder.mainFun(task_content)
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)        # adds new_task
            db.session.commit()             # saves/commits new_task into database
            return redirect('/')            # loads/redirects to the page i.e. root dir. using redirect()
        except:
            return 'Oops!! Something is bad!'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()    # an instance of the database model to query it, all() or first()-><for first data>
        for task in tasks:
            task.content = decoder.mainFun(task.content)
        return render_template('index.html', tasks=tasks)       # not just 'tasks' ---> it'd be:  'tasks=tasks'


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)  # either grabs(if exixts) the task - to be deleted, or 404

    try:
        db.session.delete(task_to_delete)       # deletes the grabbed task
        db.session.commit()                     # commits the changes to the database
        return redirect('/')                    # loads the page i.e. root i.e. /
    except:
        return 'Oops!! Error occured while deleting!'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):    
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']  # there is nothing like --> session.update()
        task_content = encoder.mainFun(task_content)

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Oops!! Error occured while updating!'
    
    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)