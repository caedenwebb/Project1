class Student:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self, name):
        pass
    def set_score(self, score):
        pass
    def set_grade(self, grade):
        pass
    def get_grade(self):
        pass
    def __str__(self):
        return f''