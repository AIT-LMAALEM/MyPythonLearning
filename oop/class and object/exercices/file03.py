class Task:
    def __init__(self,title,description,due_date,status):
        self.title=title
        self.description=description
        self.due_date=due_date
        self.status=status
    
    def display_task(self):
        print(f" Title :{self.title}")
        print(f" Description :{self.description}")
        print(f" Due Date :{self.due_date}")
        print(f"Status :{self.status}")
    
    def mark_as_complete(self):
        self.status="complete"
    

task1=Task("reviw synthax","review how to create a class and an object","2024/08/13","incomplete")

task1.display_task()

task1.mark_as_complete()

task1.display_task()