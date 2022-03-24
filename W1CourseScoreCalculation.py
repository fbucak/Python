studentName=input("Please enter your name")
studentSurname=input("Please enter your surname")
studentNumber=input("Please enter your student number")
courses={}
for i in range(0,4):
    name=input("please enter a course name")
    visa=int(input("Please enter visa grade"))
    final=int(input("Please enter final grade"))
    average=visa*0.4+final*0.6
    if average<50:
        courses.update({name:"FAILED"})
    else:
        courses.update({name: "PASSED"})
print("StudentNumber:{} Name:{} Surname:{}".format(studentNumber,studentName,studentSurname))
for course,status  in courses.items():
                print("Course Name: {}, Status: {}".format(course, status))