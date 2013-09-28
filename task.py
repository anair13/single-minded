from db import *

class Task:
    
    def __init__(self, userid, title, description, deadline, priority, effort):
        timestamp = None # this is autogenerated
        ordinality = None 
        pass
        
    def save_to_db(self):
        """Save this task to the tasks table"""
        cur = get_db().cursor()
        # cur.execute("INSERT INTO tasks VALUES (?, ?, ?)", task.get_values())
        get_db().commit()
        
    def render(self):
        """Return the HTML rendering of a task with a template"""
        pass
    
    def get_values(self):
        """Return all the values for insertion into databases
        (taskid, userid, title, description, timestamp, deadline, priority, effort, ordinality, complete)
        """
        pass
