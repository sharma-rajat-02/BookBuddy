#print role in college, home, among friends

class me:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def teacher(self):
        print(f"My teacher is: {self.name}\nShe teaches: {self.subject}")
class college(me):
    def __init__(self):
            print("I am an above average student")
class home(me):
    def home(self):
        print("I am a responsible son as well as a responsible elder brother")
class friends(me):
    def friends(self):
        print("I am a trustworthy friend")

obj1=me("Python","Dr. E. Nirmala")
obj1.teacher()