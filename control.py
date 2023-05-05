def calculate_grades(students: int, scores: list[int]) -> None:
    """Calculate grades for a given number of students and their scores.

    Args:
        students (int): The number of students.
        scores (list[int]): A list of the scores of the students.

    Returns:
        None.
    """
    while len(scores) < students:
        score_str = input(f"Enter score {len(scores) + 1}/{students}: ")
        score = int(score_str)
        scores.append(score)

    best = max(scores)

    for i, score in enumerate(scores):
        if score >= best - 10:
            grade = "A"
        elif score >= best - 20:
            grade = "B"
        elif score >= best - 30:
            grade = "C"
        elif score >= best - 40:
            grade = "D"
        else:
            grade = "F"
        print(f"Student {i+1} score is {score} and grade is {grade}.")


students_str = input("Enter the number of students: ")
students = int(students_str)

scores = []
calculate_grades(students, scores)
