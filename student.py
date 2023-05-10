class Student:
    """
    A class to represent a student.

    Attributes:
    ----------
    name : str
        The name of the student.
    score : float
        The score of the student.
    """
    def __init__(self, name: str, score: float) -> None:
        """
        Initializes a new instance of the Student class.

        Parameters:
        ----------
        name : str
            The name of the student.
        score : float
            The score of the student.
        """
        self.name = name
        self.score = score
        self.__grade = None

    def set_name(self, name: str) -> None:
        """
        Sets the name of the student.

        Parameters:
        ----------
        name : str
            The name of the student.
        """
        self.name = name

    def get_name(self) -> str:
        """
        Returns the name of the student.

        Returns:
        ----------
        str
            The name of the student.
        """
        return self.name

    def set_score(self, score: float) -> None:
        """
        Sets the score of the student.

        Parameters:
        ----------
        score : float
            The score of the student.
        """
        self.score = score

    def get_score(self) -> float:
        """
        Returns the score of the student.

        Returns:
        ----------
        float
            The score of the student.
        """
        return self.score

    def set_grade(self, grade: str) -> None:
        """
        Sets the grade of the student.

        Parameters:
        ----------
        grade : str
            The grade of the student.
        """
        self.__grade = grade

    def get_grade(self) -> str:
        """
        Returns the grade of the student.

        Returns:
        ----------
        str
            The grade of the student.
        """
        return self.__grade

    def __str__(self) -> str:
        """
        Returns a string with the student, their score, and their grade.

        Returns:
        ----------
        str
            A string representation of student info.
        """
        return f"{self.name} has a score of {self.score} so their grade is {self.get_grade()}"
