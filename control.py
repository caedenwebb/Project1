from student import Student

students = [] #creates a list to store student objects
scores = [] #creates a list to store students scores
grades = [] #creates a list to store student grades
def calculate_grades(window):

    #gets Student Names and Scores from User; places Student Names and Scores in a list
    StudentDataText = window.StudentData.toPlainText().split('\n')
    #loop through the StudentDataText list and splits the string in each index position on ','
    i = 0
    while i < len(StudentDataText):
        StudentDataText[i] = StudentDataText[i].split(',')
        i = i + 1
    #fills students list with student objects for each Student Name and Score
    for ind_student in StudentDataText:
        s = Student(ind_student[0], int(ind_student[1]))
        students.append(s)

    #retrieves scores and places them in scores list
    for ind_student in students:
        scores.append(ind_student.get_score())
    #calculates best score
    best_score = max(scores)



