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