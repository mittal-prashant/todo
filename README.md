# TODO List

##### Note:

- Docker should be installed on the system.
- Python version used - 3.10.2.
- All the files should be present in the directory.
- The database file "test.db" is present in the instance folder.
- Requirements are mentioned in requirements.txt file.

##### To run the app follow following steps:

1. First of all open the terminal in the Project directory.
2. Create a docker image using the following command:

   ```
   docker build --tag todo-app .
   ```

3. Create a docker container in which the app would run using following command:

   ```
   docker run --name todo-app -p 5000:5000 todo-app
   ```

4. Now the flask app would be running on http://localhost:5000/ or http://127.0.0.1:5000/
