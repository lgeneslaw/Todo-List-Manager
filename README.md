# Todo-List-Manager

##Author
Luke Geneslaw

##About
The Todo List Manager is a web service built in Django, meant to fulfill the following requirements:

 - Create, Update, Delete
 - Show Items Completed On A Given Day
 - Show Uncompleted Items
 - Show Items Due Soon - visual Indication
 - Show Items Past Due - visual Indication
 - Week View
 - Day View

##Stack
Backend - SQLlite3, Python 2.7

Frontend - JQuery

##Notable Files

The following files are found within todolist/todolist_app
 - models.py - Contains the Task object model. A Task has a name, due date, completion flag, and optional completion date
 - views.py - Interracts with models.py to serve pages
 - urls.py - maps URL regular expressions to target methods in views.py
 - forms.py - defines the form for creating/editing a Task
 - templates/todolist_app - directory containing the page templates served by views.py
