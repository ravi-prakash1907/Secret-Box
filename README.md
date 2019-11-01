# TODO-List-App-Flask
It's my first Flask project


This is a todo-list app, developed using **Flask** that lets user to add new tasks that are to be done.
Also, you can update or delete the tasks, as well!


## Requirements

To run this app, we need following:

1. Flask (python)
2. virtual environment for flask i.e. ```virtualenv```
3. SQLAlchemy

## Steps to run 
_Make sure you have all the dependancies installed_
Open this project directory in the terminal/console

#### Once (only, while running for first time)
```
virtualenv env
source env/bin/activate

pip install flask flask-sqlalchemy

from app import db
db.create_all()
exit()
```
#### Before opening the browser
```
source env/bin/activate
```
```
python3 app.py
```
