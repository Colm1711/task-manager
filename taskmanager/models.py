from taskmanager import db


class Category(db.Model):
    # we want each tables to have it's own unique ID acting as primary key
    # schema for the Category Model and will act as PK
    id = db.Column(db.Integer, primary_key=True)
    # add new column of 'category name' set to standard db col, type of string at 25 characters, unique and can't be null.
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Task(db.Model):
    # we want each tables to have it's own unique ID acting as primary key
    # schema for the Task Model and will act as PK
    id = db.Column(db.Integer, primary_key=True)
    # add new column of 'task_name' set to standard db col, type of string at 50 characters, unique and can't be null.
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    # ondelete CASCADE will make sure that all instances connected to the category id will be deleted
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f'#{self.id} - Task:{self.task_name} | Urgent:{self.is_urgent}'