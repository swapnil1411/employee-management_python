class Person:
    def __init__(self,name:str,age:int):
        self.name =name
        self.age=age
    def __repr__(self):
        return f"{self.name}:{self.age}"