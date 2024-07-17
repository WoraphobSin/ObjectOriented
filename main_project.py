from Class_Object import *

# Create Student
oStudent1 = Student("123", "Bill", "Gate", 21)
oStudent2 = Student("000", "Mary", "Fox", 19)
oStudent3 = Student("550", "Man", "Above", 19)
oStudent4 = Student("851", "Bob", "Stuart", 22)
oStudent5 = Student("120", "Jimmy", "Geo", 20)

# Create Teacher
oTeacher1 = Teacher("100-00", "Gary", "Alpha", 32, "Math", "Sciene", 3)
oTeacher2 = Teacher("200-00", "German", "Oliver", 40, "Electrical", "Engineering", 3)

# Create Courses
oCourse1 = Course("S-10", "Physic", 3)
oCourse2 = Course("M-02", "Math", 2)
oCourse3 = Course("E-00", "English", 5)
oCourse4 = Course("G-50", "Social", 5)
oCourse5 = Course("I-50", "Industial", 2)

# Add student into course1 "Physic"
oCourse1.addStudent(oStudent1)
oCourse1.addStudent(oStudent2)
oCourse1.addStudent(oStudent3)
oCourse1.addStudent(oStudent4) # Cant add student because course cap is 3.

# Add student into course4 "Social"
oCourse4.addStudent(oStudent1)
oCourse4.addStudent(oStudent2)
oCourse4.addStudent(oStudent3)
oCourse4.addStudent(oStudent4)
oCourse4.addStudent(oStudent5)

# Add student2 into all course
oCourse1.addStudent(oStudent2)
oCourse2.addStudent(oStudent2)
oCourse3.addStudent(oStudent2)
oCourse4.addStudent(oStudent2)
#oCourse5.addStudent(oStudent2)

# Add course for teacher1 "Gary Alpha"
oTeacher1.addCourse(oCourse1)
oTeacher1.addCourse(oCourse2)
oTeacher1.addCourse(oCourse3)

# Add course for teacher2 "German Oliver"
oTeacher2.addCourse(oCourse3)
oTeacher2.addCourse(oCourse4)
oTeacher2.addCourse(oCourse5) # Cant add course because teacher2 can teach max at 2 course

oCourse1.info()
oStudent2.info()
oTeacher1.info()


# Remove course2 "Math" from teacher1 "Gary Alpha"
# oTeacher1.removeCourse(oCourse2)
# oTeacher1.info() # Show result

# Remove student4 "Bob Stuart" from course4 "Social"
# oCourse4.removeStudent(oStudent4)
# oCourse4.info() # Show result

# Give score to student2 
oTeacher1.giveScore(oCourse1,oStudent1,50)
oTeacher1.giveScore(oCourse1,oStudent2,60)
oTeacher1.giveScore(oCourse2,oStudent2,91)
oTeacher1.giveScore(oCourse3,oStudent2,11)
oTeacher1.giveScore(oCourse4,oStudent2,63) # Teacher1 "Gary Alpha" doesn't teach this course
oTeacher1.giveScore(oCourse1,oStudent3,85)
oTeacher1.giveScore(oCourse1,oStudent5,10) # Student5 "Jimmy Geo" isn't enroll in course1 "Physic"
oTeacher2.giveScore(oCourse1,oStudent2,75) # Teacher2 "German Oliver" doesn't teach this course
oTeacher2.giveScore(oCourse5,oStudent2,75) # Student2 "Marry Fox" isn't enroll in course5 "Industrial"
oTeacher2.giveScore(oCourse4,oStudent1,77)
oTeacher2.giveScore(oCourse4,oStudent2,75)
oTeacher2.giveScore(oCourse4,oStudent3,37)
oTeacher2.giveScore(oCourse4,oStudent4,100)
oTeacher2.giveScore(oCourse4,oStudent5,42)

oStudent1.info()
oStudent2.info()
oStudent3.info()
oStudent4.info()
oStudent5.info()
# print(oStudent1.grade)
# print(oStudent2.grade)
# print(oStudent3.grade)
oCourse1.info()
oCourse4.info()

oCourse1.averageGrade() # (50+60+85)/3 = 65
oCourse4.averageGrade() # (77+75+37+100+42)/5 = 66.2
oCourse3.averageGrade()
oStudent2.calGrade(oCourse1)
oStudent2.calGrade(oCourse2)
oStudent2.calGrade(oCourse3)
oStudent2.calGrade(oCourse4)
oStudent4.calGrade(oCourse5)