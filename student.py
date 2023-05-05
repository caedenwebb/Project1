class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.__grade = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_score(self, score):
        self.score = score

    def set_grade(self, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def __str__(self):
        return f"{self.name} has a score of {self.score} so their grade is {self.get_grade()}"
