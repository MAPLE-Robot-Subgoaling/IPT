import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///labeler.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("admin","admin")
session.add(user)

label = Label("admin","A","a sample description")
session.add(label)

label = Label("admin","B","a sample description")
session.add(label)

label = Label("admin","C","a sample description")
session.add(label)

line = Line("admin", "hw3_69.py", 4, "A")
session.add(label)

line = Line("admin", "hw3_69.py", 6, "B")
session.add(label)

line = Line("admin", "hw3_69.py", 8, "C")
session.add(label)

# commit the record the database
session.commit()
 
session.close()
