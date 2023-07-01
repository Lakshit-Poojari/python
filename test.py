"""def full_name(first_name , middle_name, last_name):
    fullname = first_name + middle_name + last_name
    print(fullname)
full_name("Lakshit ", "Channa " ,"Pooari")
"""
class college:
    name = ""
    add = ""
    stream = ""
    def __init__(self):
        print('This is a default constructer')
    def __init__(self, name, add, stream):
        print('This is a parameterised constructer')
        self.name = name
        self.add = add
        self.stream = stream
    def info(self):
        print(f"{self.name} college is located at {self.add} its stream is {self.stream} ")

a = college()
a.name = "SVP"
a.add = "Mumbai"
a.stream = "Science"

b = college( )
b.name = "universal"
b.add = "Palghar"
b.stream = "engi" 


a.info()
b.info()