cd task_tracker

python3.8 -m venv venv

. venv/bin/activate

pip install -r requirements.txt

docker run -d --name redis -p 6379:6379 redis

cd src

python manage.py migrate

python manage.py create_users_and_teams

python manage.py runserver

in two separate terminals:

celery -A tracker worker

celery -A tracker beat

* Postman collection attached with this project
* Login with any user mentioned in users/management/commands/create_users_and_teams.py
* First get the list of users created and note their ids
* Then hit the api for listing members and leaders
* Then log in with user credentials
* First create a team using the api in the postman collection
* Then create a task using the api
* Log in with leader credentials for the team to which task was allotted to allot it to team members
* Log in with member credentials for the team to update status of the task

Requirements:
-----------------------------------------------------------------------------------------------

A Simple Task tracker Application

Objective
Build a simple web application which helps users to create a task and associate it with a team.
The team leader of the team will assign the team member or team members to the task. The
team member will update the status of the task.
Note: Only Users will be able to create tasks and teams.
ORM guidelines:
1. Custom User model with roles User, Team leader, Team member ( hint: use
AbstractUser model of django)
2. Create a Task model
(hint: model fields - id, name, team, team members, status, started_at, completed_at)
3. Create a Team model
(hint: model fields - id, name, team leader, team members)
Note: If you need to create any other models or database tables feel free to do so. Above 3 are
just the basic requirements.
Backend flow:
Users/team leaders/team members can be created using the django admin interface or
command line and assign them specific roles mentioned above.
Use Token Authentication for all the APIs provided by DRF.
1. Create Team API with necessary fields (name, team leader and team members)
2. Create Task API with necessary fields (name and team) - Once task is created, send an email
to the team leader of the associated team with task details (async background task)
3. Update Task API
- team leaders will be able to update all task fields
- team members will be able to update the status only (status can be “Assigned”, “In
progress”, “Under Review” and “Done”)
4. Retrieve Tasks API
- Retrieve a list of all tasks (all fields of Task model included)
Requirements:
Use Django as the project framework and Django rest framework for building RESTful APIs.
Use Celery for any background tasks and console backend for sending email
Maintain the proper code structure, naming conventions etc.
