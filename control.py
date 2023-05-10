from student import Student

students = [] #creates a list to store student objects

def add_student(window) -> None:
    '''
    Adds a Student
    :param window: Takes in the MainWindow
    :return: None
    '''
    scores = []  # creates a list to store students scores
    score = 0.0
    if (window.scoreInput.text() == '' and window.nameInput.text() == ''):
        window.errorLabel.setText('Error: Please enter a name and score.')
        return None
    elif (window.nameInput.text() == ''):
        window.errorLabel.setText('Error: Please enter a name.')
        return None
    elif (window.scoreInput.text() == ''):
        window.errorLabel.setText('Error: Please enter a score.')
        return None
    try:
        score = float(window.scoreInput.text())
    except:
        window.errorLabel.setText(f'Error: Please enter an integer or decimal value to the score field.')
        window.scoreInput.setText('')
        return None
    check_if_student_exists = False
    check_if_student_first = False
    if (students == []):
        s = Student(window.nameInput.text(), score)
        students.append(s)
        check_if_student_first = True
    else:
        for student in students:
            if (student.get_name() == window.nameInput.text()):
                check_if_student_exists = True
                student.set_score(score)
                break
            else:
                continue
    if (check_if_student_exists == False and check_if_student_first == False):
        s = Student(window.nameInput.text(), score)
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

    if (window.nameInput.text() == ''):
        window.errorLabel.setText('Error: Please enter a name.')
        window.scoreInput.setText('')
        return None
    else:
        pass

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



