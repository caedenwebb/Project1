class Student:
    def __init__(self):
        self.name = ""
        self.score = 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return (self.name, self.score, self.get_grade())
      #  return f"{self.name} has a score of {self.score} so their grade is {self.get_grade()}"
