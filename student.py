class Student:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        self.__grade = ''
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self, name):
        pass
    def set_score(self, score):
        pass
    def set_grade(self, grade):
        self.__grade = grade
    def get_grade(self):
        return self.__grade
    def __str__(self):
        return f''