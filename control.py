from student import Student

students = [] #creates a list to store student objects

def add_student(window):
    scores = []  # creates a list to store students scores
    '''
    Adds a Student
    :param window: Takes in the MainWindow
    :return: None
    '''
    s = Student(window.nameInput.text(), float(window.scoreInput.text()))
    students.append(s)
    print(f'Students: {students}')
    for student in students:
        scores.append(student.get_score())
    print(f'Scores: {scores}')
    best = max(scores)
    print(f'Best: {best}')
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
def delete_student(window):
    '''
    Deletes a student
    :param window: takes in the MainWindow
    :return: None
    '''
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
    if (studentFound == True):
        pass
    else:
        window.errorLabel.setText(f'Error: Student "{window.nameInput.text()}" not found.')
    for i in range(len(students)):
        window.studentNamesList.setText(window.studentNamesList.text() + '\n' + students[i].get_name())
        window.studentScoresList.setText(window.studentScoresList.text() + '\n' + str(students[i].get_score()))


