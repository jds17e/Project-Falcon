# DMapp

## Running the flask api server

cd into the dm_api direcotry

`cd dm_api`

activate the python evnvironment

`source api/bin/activate`

cd out of the dm_api directory and set the flask app to run

`export FLASK_APP=dm_api`

run the server

`flask run`

the following text should print:

 * Serving Flask-SocketIO app "dm_api/"
 * Forcing debug mode off
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/flask_sqlalchemy/__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
 * Serving Flask app "dm_api/"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/flask_sqlalchemy/__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)