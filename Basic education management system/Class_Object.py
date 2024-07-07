class Student:
    def __init__(self, id, name, surname, age):
        self.__id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.grade = {}
    
    def info(self):
        print("###### Student info ######")
        print(f"Student ID: {Student.get_id(self)}\nStudent name \"{self.name} {self.surname}\" and {self.age} years old.")
        print(f"Course enrolled: {self.grade}\n")

    def calGrade(self, course):
        if course.id in self.grade:
            if self.grade[course.id]["Grade"] >= 80 and self.grade[course.id]["Grade"] <= 100:
                print(f"\"{self.name} {self.surname}\" got grade \"A\" in course \"{course.name}\" .")
            elif self.grade[course.id]["Grade"] >= 70:
                print(f"\"{self.name} {self.surname}\" got grade \"B\" in course \"{course.name}\" .")
            elif self.grade[course.id]["Grade"] >= 60:
                print(f"\"{self.name} {self.surname}\" got grade \"C\" in course \"{course.name}\" .")
            elif self.grade[course.id]["Grade"] >= 50:
                print(f"\"{self.name} {self.surname}\" got grade \"D\" in course \"{course.name}\" .")
            else:
                print(f"\"{self.name} {self.surname}\" got grade \"F\" in course \"{course.name}\" .")
        else:
            print(f"You didn't enroll course \"{course.name}\" ")
    
    def get_id(self):
        return self.__id   
    
class Teacher(Student): 
    def __init__(self, id, name, surname, age, major, faculty, max_course):
        super().__init__(id, name, surname, age)
        self.major = major
        self.faculty = faculty
        self.teach = []
        self.max_course = max_course

    def info(self):
        print("###### Teacher info ######")
        print(f"Teacher ID: {Teacher.get_id(self)}, Teacher name \"{self.name} {self.surname}\" and {self.age} years old \nFrom faculty {self.faculty}, Major {self.major}, Max course: {self.max_course}")
        print("Course responsibilty:")
        for x in range(0,len(self.teach)):
            print(" -",self.teach[x].name)
        print("")

    def addCourse(self, course):
        if self.max_course <= len(self.teach):
            print("Schedule of teacher is full!")
        else:
            self.teach.append(course)
            print("Course added successfully")
    
    def removeCourse(self, course):
        for x in range(0, len(self.teach)):
            if course == self.teach[x]:
                print(f"Course \"{course.name}\" have been remove from schedule of teacher name \"{self.name}\" .")
                del self.teach[x]
                return True
        print("Course isn't found!")

    def giveScore(self, course, student, score):
        for x in range(0, len(self.teach)):
            if course == self.teach[x]:
                for i in range(0, len(course.student)):
                    if course.student[i] == student:
                        student.grade[course.id] = {"Course" : course.name, "Grade" : score }
                        print(f"Score added successfully")
                        return None 
                print(f"\"{student.name} {student.surname}\" isn't enroll for course \"{course.name}\"")
                return None         
        print(f"Course \"{course.name}\" is out of teacher \"{self.name} {self.surname}\" responsibility!")
        return None       
    
class Course:
    def __init__(self, id, name, capacity):
        self.id = id
        self.name = name 
        self.capacity = capacity
        self.student = []
    
    def info(self):
        print("####### Course info #######")
        print(f"Course ID: {self.id}, Course name: {self.name}\nCourse capacity: {self.capacity}")
        print("Students enroll this course:")
        for x in range(0,len(self.student)):
            print(" -",self.student[x].name ,self.student[x].surname)
        print("")

    def addStudent(self, student):
        if self.capacity <= len(self.student):
            print("Course is full right now.")
        else:
            self.student.append(student)
            print("Student added successfully.")
    
    def removeStudent(self, student):
        for x in range(0, len(self.student)):
            if student == self.student[x]:
                print(f"Student name \"{student.name} {student.surname}\" have been remove from course name \"{self.name}\" .")
                del self.student[x]
                return True
        print("Student isn't found!")

    def averageGrade(self): # Careful! make sure you give score to all student in the course before call this method.
        averageGrade = 0
        num = 0
        for x in range(0, len(self.student)):
            if self.student[x].grade[self.id]["Course"] == self.name:
                averageGrade = averageGrade + self.student[x].grade[self.id]["Grade"]
                num += 1
        if num == 0:
            return None
        else:
            print(f"Average grade of course \"{self.name}\" is {averageGrade/num} .")
            return averageGrade/num

