Will need to pip install requirements.txt, redo symlinks, specifically sensors/static and sensors/templates/index.html to point to the appropriate directories from the grapes-react project
db.sqlite3 is also not committed, will need to recreate and run migrations

python manage.py runserver 0.0.0.0:8000 to run
