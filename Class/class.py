from typing import Union, Dict
class Student:
    """
    Student class that stores marks for any number of subjects
    and provides total and average score calculations.

    Benefits:
    - SRP (Single Responsibility Principle)
    - Validations included
    - Extensible to any number of subjects
    """
    
    def __init__(self, name : str, **marks : Dict [str,Union[int,float]]):
        self.name = name
        self.marks = marks
        self.overall_score = 0
        self.avg_score = 0

    def validate(self):
        for subject,score in self.marks.items():
            if not isinstance(score,(int,float)):
                raise ValueError(f'Invalid score {score} with {subject}')
                
    def calculate_total(self):
        self.overall_score = sum(self.marks.values())
        return self.overall_score

    def calculate_average(self):
        if len(self.marks) == 0:
            self.avg_score = 0
        else:
            self.avg_score  = self.overall_score / len(self.marks)
        return self.avg_score
    
    def get_infomation(self):
        print(f'{self.name} scored total {self.overall_score} and Avg is {self.avg_score}')
        


data = [
    {"name":"Pugazhendhi","tamil":90,"english":60, "maths":90, "science" : 80, "social_science" :100},
    {"name":"Ashwin","tamil":60,"english":70, "maths":80, "science" : 90, "social_science" :100},
    {"name":"Siva","tamil":20,"english":30, "maths":40, "science" : 50, "social_science" :60}
]

for item in data:
    name = item.pop("name")
    student_details = Student(name,**item)
    student_details.validate()
    student_details.calculate_total()
    student_details.calculate_average()
    student_details.get_infomation()

 