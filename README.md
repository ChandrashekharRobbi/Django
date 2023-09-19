# Django


start command

To create new Project
```py
django-admin startproject demoproject
```

To Create new App
```py
python manage.py startapp lemonslame
```

To run the server
```py
python manage.py runserver
```

Migrations
```py
# it is similar like ge4t ready with set of statements to change the models
python manage.py makemigrations
# it is similar to execute all the commands 
python manage.py migrate
# it is similar to viewing all changes made
python manage.py showmigrations


```



Traverse Back to Previous Model
```py
# it will tell what all things will undo 
python manage.py migrate lemmonslame 0002 --plan
# it will go back to the stage of 0002
python manage.py migrate lemmonslame 0002

# if we want to see SQL statement where Django performs by using OOPS
python manage.py sqlmigrate lemmonslame 0001 # it will show all sql code for 0001 file
```


