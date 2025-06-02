from models.person import Person 

class Employee(Person):
    def __init__(self,name:str,age:int ,emp_id:int, department:str,salary:int):
        super().__init__(name,age) ##use person.py name and age by calling super which uses person.py
        self.department =department
        self.emp_id =emp_id
        self.salary=salary
    
    def __repr__(self):
        return f"{self.name} ({self.age} yrs) - {self.department} - ${self.salary}"

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "salary": self.salary
        }