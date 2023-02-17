
# TODO List

To run the app follow following steps:

1. First of all open the terminal in the Project directory
2. Activate the virtual environment using following command:

   ```
   .\venv\Scripts\activate
   ```
3. Open Python terminal in the project folder.
4. Write following script in Python terminal:

   ```
   from app import app, db
   app.app_context().push()
   db.create_all()

   ```
5. Now run the flask app using following command:

   ```
   flask --app app run
   ```
6. Deactivate the virtual environment using following command:

   ```
   deactivate
   ```
