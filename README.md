go in python shell

from app import app, db

app.app_context().push()

db.create_all()




flask --app app --debug run 

for continuous
