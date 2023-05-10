from student import Student

students = [] #creates a list to store student objects

def add_student(window) -> None:
    '''
    Adds a Student
    :param window: Takes in the MainWindow
    :return: None
    '''
    scores = []  # creates a list to store students scores
    s = Student(window.nameInput.text(), float(window.scoreInput.text()))
    students.append(s)
    for student in students:
        scores.append(student.get_score())
    best = max(scores)
    for student in students:
        if (student.get_score() >= (best - 10)):
            student.set_grade('A')
            continue
        elif (student.get_score() >= (best - 20)):
            student.set_grade('B')
        elif (student.get_score() >= (best - 30)):
            student.set_grade('C')
        elif (student.get_score() >= (best - 40)):
            student.set_grade('D')
        else:
            student.set_grade('F')
    window.studentNamesList.setText('')
    window.studentScoresList.setText('')
    window.studentGradesList.setText('')
    for student in students:
        window.studentNamesList.setText(window.studentNamesList.toPlainText() + f'{student.get_name()}\n')
        window.studentScoresList.setText(window.studentScoresList.toPlainText() + f'{student.get_score()}\n')
        window.studentGradesList.setText(window.studentGradesList.toPlainText() + f'{student.get_grade()}\n')
    window.nameInput.setText('')
    window.scoreInput.setText('')
def delete_student(window) -> None:
    '''
    Deletes a student
    :param window: takes in the MainWindow
    :return: None
    '''
    scores = []
    i = 0
    studentFound = False
    for student in students:
        if (student.get_name() == window.nameInput.text()):
            studentFound = True
            students.pop(i)
            break
        else:
            i = i + 1
            continue
    if (studentFound == True and len(students) > 0):
        for student in students:
            scores.append(student.get_score())
        best = max(scores)
        for student in students:
            if (student.get_score() >= (best - 10)):
                student.set_grade('A')
                continue
            elif (student.get_score() >= (best - 20)):
                student.set_grade('B')
            elif (student.get_score() >= (best - 30)):
                student.set_grade('C')
            elif (student.get_score() >= (best - 40)):
                student.set_grade('D')
            else:
                student.set_grade('F')
        window.studentNamesList.setText('')
        window.studentScoresList.setText('')
        window.studentGradesList.setText('')
        for student in students:
            window.studentNamesList.setText(window.studentNamesList.toPlainText() + f'{student.get_name()}\n')
            window.studentScoresList.setText(window.studentScoresList.toPlainText() + f'{student.get_score()}\n')
            window.studentGradesList.setText(window.studentGradesList.toPlainText() + f'{student.get_grade()}\n')
        window.nameInput.setText('')
        window.scoreInput.setText('')
    elif (studentFound == True and len(students) == 0):
        students.clear()
        window.nameInput.setText('')
        window.scoreInput.setText('')
        window.studentNamesList.setText('')
        window.studentScoresList.setText('')
        window.studentGradesList.setText('')
    else:
        window.errorLabel.setText(f'Error: Student "{window.nameInput.text()}" not found.')
        window.nameInput.setText('')
        window.scoreInput.setText('')



