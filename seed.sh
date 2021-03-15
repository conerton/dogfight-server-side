rm -rf dogfightapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations dogfightapi
python manage.py migrate dogfightapi
python manage.py loaddata users 
python manage.py loaddata tokens 
python manage.py loaddata hot_dogs
python manage.py loaddata user_hot_dogs