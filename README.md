# Portfolio
Website portfolio for programming projects

## Running the App
This application uses the Flask framework therefore can be run locally using the command:
```
flask run
```

This app was hosted on heroku using the following commmands:

First make sure everything in conda envrinoment is already installed(becuase new packages added wont be reflected on Heroku)

Gunicorn is a server that runs these.
```
$ pip install gunicorn
```

Freeze is used to view to packages inside of an environment and '>' this charcter is used 'pipe' which means install files into the file requirements.txt
```
$ pip freeze > requirements.txt
```
The Procfile specifies the commands that are executed by the app on startup. 
```
$ touch `Procfile`
```

The first app refers to the file name of your main app(app.py), the second app refers to the object inside the main file which in this case is set to enable flask.Gunicorn runs the app file.
```
$ web: gunicorn app:app
```

This command is only used if you do not have an app already setup.
```
heroku create
```

