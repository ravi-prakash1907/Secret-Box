# Secret-Box : A Secure Task Manager
![assets/banner.jpg](assets/banner.jpg)  

Introducing _Secret-Box_ app, that is a very basic application made to keep a track on the tasks (more similar to the _totdo list manager_). The app is developed on [Flask](https://flask.palletsprojects.com/) web-framework of python.  

The Secret-Box provieds following features to the end-user:  
1. Store and remove a task.  
2. Update a task statement.  
3. View all the remaining tasks.  

### Key Features:  
> **1. Modularity:** The project is kept moduler where an rendered web-page inharites it's sections from different static template.  
> **2. Database:** It uses the SQL database to store the task lists efficiently.  
> **3. Data Security:** The tasks are encrypted using _EncryptIt_ cryptographic algorithm, before being stored in the database.  
>   * The [_EncryptIt_](https://github.com/ravi-prakash1907/EncryptIT) is a **route-cipher based algorithm**, designed by [me](http://ravi-prakash1907.gitlab.io/) myself. It is inspired from the enigma machine. Please refer to [ravi-prakash1907.github.io/EncryptIT/](https://ravi-prakash1907.github.io/EncryptIT/) to know more about EncryptIt.  

The Web-UI is splitted into three pages kept very basic as I have implemented the same through a single master `CSS` script.  


## Dependencies and Initial Set-up
The **Secret-Box** requires a very less external dependacy to run on the system. Although the application can work on the main environment, still it's **recommand** to install this application on a _python virtual environment_. To run this app, we need following:  
1. Flask (python)  
2. virtual environment for flask i.e. ```virtualenv```  
3. SQLAlchemy  

### Installation  
_Here I'm giving 5 easy steps to install the application using **bash** terminal_  

> Step 1. Open the _bash terminal_ and navigate inside the ```Secret-Box``` directory.  
>   - ```
>        $ cd <download location>/Secret-Box/  
>     ```  
>   
> Step 2. Create a python virtual environment (say **env**):  
>   - ```
>        $ virtualenv env  
>     ```  
>   
> Step 3. Activate _env_ and install dependancies:  
>   - ```
>        $ source env/bin/activate  
>        $ pip install flask flask-sqlalchemy  
>     ```  
>   
> Step 4. Open python console:  
>   - ```
>        $ python  
>     ```  
>   
> Step 5. Initialize the database:  
>   - ```
>       >> from app import db  
>       >> db.create_all()  
>       >> exit()  
>     ```  
>  

Althogh, we can make the installation more easier with the containerized version of this application, I am keeping it very simple for this submission.  

_We are all set to run the **Secret-Box!**_

## Steps for Execution
Everytime, in order to use the applicaation, following 3 easy steps will be required to be folloed:  
> Step 1. Open the _bash terminal_ and navigate inside the ```Secret-Box``` directory.  
>   - ```$ cd <download location>/Secret-Box/```  
>   
> Step 2. Activate _env_ and run ```app.py```:  
>   - ```$ source env/bin/activate  
>        $ python app.py  
>     ```  
>   
> Step 3. The application's web portal will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)    
>   
