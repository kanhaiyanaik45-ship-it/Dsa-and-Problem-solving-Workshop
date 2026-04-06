# #reverse a list
# # list = [1,2,3,4,5]
# # list.reverse()
# print(list[::-1])
# # print(list)



#palindrome
# list =[1,2,3,2,1]
# if list == list[::-1]:
#     print("palindrome")
# else:
#   

#class
# class Student:
#     roll_no = 101

#     def student_data(self):
#         print("Student Informatin")

# obj= Student()
# print(obj.roll_no)
# obj.student_data()



# class Demo:
#     def __init__(self):
#         print("I am  a constructor")
    
#     def msg(self):
#         print("Hello Class")
# obj = Demo()
# obj2=Demo()
# obj.msg()


# class Hod:
#     def __init__(self):
#         self.name='sagar naik'
#         self.age=21
#         self.empid=101

    # def info(self):
    #     print("My name is",self.name)
    #     print("My age is",self.age)
    #     print("My emp id is",self.empid)
# obj = Hod()
# obj.info()




# class Hod:
#     def __init__(self,name,age,empid):
#         self.name= name
#         self.age=age
#         self.empid=empid

#     def show(self):
#         print("My name is",self.name)
#         print("My age is",self.age)
#         print("My emp id is",self.empid)
# obj = Hod("arjun",45,101)
# obj.show()


# class New:
#     def __init__(self):
#         self.a = 10
# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# obj1.a = 20
# print()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)


# class Student:
#     def __init__(self):
#         self.s_name = "Kanhaiya Naik"
#         self.s_rollNo = "45"

#     def getdata(self):
#         self.s_mb = 9529784765

# obj = Student()
# obj.getdata()
# del obj.s_mb
# obj.s_branch = "cs"
# print(obj.__dict__)



# class New:
#     a =10

#     def __init__(self):
#         self.name="sagar"

# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj1.a)
# print(obj1.a)
# New.a = 50
# print(obj1.a)
# print(obj1.a)
# print(obj1.a)




# #CRUD operations
# import sys

# class CRUD:
#     def __init__(self):
#         print("Student Management System:")
#         self.studentID=[]
#         self.studentname=[]
#         self.studentrollno=[]
#         self.studentcity=[]

#     def addStudent(self):
#         self.studentID.append(input("Enter student ID:"))
#         self.studentname.append(input("Enter student Name:"))
#         self.studentrollno.append(input("Enter student Roll No:"))
#         self.studentcity.append(input("Enter student City:"))

#     def deleteStudent(self):
#         self.studentID.remove()
#         self.studentname.remove()
#         self.studentrollno.remove()
#         self.studentcity.remove()

#     def updateStudent(self):
#         self.studentID[0] = input("Enter student ID:")
#         self.studentname[0] = input("Enter student Name:")
#         self.studentrollno[0] = input("Enter student Roll No:")
#         self.studentcity[0] = input("Enter student City:")
        

#     def displayStudent(self):
#         print("studentID",self.studentID)
#         print("studentrollno",self.studentrollno)
#         print("studentname",self.studentname)
#         print("studentcity",self.studentcity)

# obj = CRUD()
# while True:
#     print("1. Add student")
#     print("2. Delete student")
#     print("3. Update student")
#     print("4. Display student")
#     print("5. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         obj.addStudent()
#     elif choice == 2:
#         obj.deleteStudent()
#     elif choice == 3:
#         obj.updateStudent()
#     elif choice == 4:
#         obj.displayStudent()
#     elif choice == 5:
#         sys.exit()
#     else:
#         print("Invalid choice")






#instance method
# class Student:
#     def __init__(self,name,roll_no,mob):
#         self.name = name
#         self.roll_no = roll_no
#         self.mob =mob

#     def display(self):
#         print(self.name,"",self.roll_no,"",self.mob)

# stud = Student("sagar",101,64916143)
# stud.display()    



# class Student:
#     @staticmethod
#     def get_personal_detail(firstname, lastname):
#         print("Your personal Detail",firstname,lastname)
#     @staticmethod
#     def constant_detail(mobile_no, roll_no):
#         print("Your Constant Detail",mobile_no,roll_no)

# Student.get_personal_detail("sagar","naik")
# Student.constant_detail(984916143,101)
    



#inheritance
#extending property from one class to another classis called inheritance
#base class:a class which inherit its property to another is called base/parent class
#derived class: a class which properties is inheroted are claled derived/child class
# type: single multple multilevel



#single level
# class college:
#     def college_name(self):
#         print("modern college")

# class Student(college):
#     def student_info(self):
#         print("Name: sagar naik")
#         print("Branch: cs")
# obj = Student()
# obj.college_name()
# obj.student_info()




#multilevel
# class college:
#     def college_name(self):
#         print("modern college")

# class Student(college):
#     def student_info(self):
#         print("Name: sagar naik")
#         print("Branch: cs")

# class Exam(Student):
#     def subject(self):
#         print("Subject1: c++")
#         print("Subject2: pyhon")
#         print("Subject3: java")
# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()



#multiple inheritnce
# class SubMarks:
#     math = int(input("Enter paper mark of Math:"))
#     De = int(Input("enter paper mark of c languag:"))
#     english =int(input("enter marks of english:"))

# class PracMarks:
#     cprac = int(Input("enter paper mark of c languag:"))

# class Result(SubMarks,PracMarks):
#     def total(self):
#         if self.math >= 40 and self.DE >=40 and self.c>=40 and self.english >=40 and self.cprac >=20:
#             print("pass")
#         else:
#             print("fail")

# obj =Result()
# obj.total()

#polymorphism
# class Principle:
#     def role(self):
#         print("I am managing all acivity of collage")

# class Deam:
#     def role(self):
#         print("I am decision taking person")
# class Hod:
#     def role(self):
#         print("I have responsibility to take decision")
# class faculty:
#     def role(self):
#         print("I am responsible for teaching")

# def func(obj):
#     obj.role()
# campus=[Principle(),Deam(),Hod(),faculty()]
# for obj in campus:
#     func(obj)



#python does not support method and constructor overloading
# class Arithmatic:
#     def add(self,a):      #type error which meanse consrtuctor does not understand where to add element
#         print(a)

#     def add(self,a,b):
#         print(a+b)

#     def add(self,a,b,c):
#         print(a+b+c)
# obj = Arithmatic()
# obj.add(10)
# obj.add(20,30)
# obj.add(10,20,30)

# above problem handling
# class Arithmetic:
#     def add(self,a=None,b=None,c=None):
#       if a!=None and b==None and c==None:
#         print(a)
#       elif a!=None and b!=None and c==None:
#         print(a+b)
#       elif a!=None and b!=None and c!=None:
#         print(a+b+c)
# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)



# class Arithmatic:
#     def __init__(self):
#         print("here is no argument")      #error same as above
#     def __init__(self,a):
#         print("here is one argument")
#     def __init__(self,a,b):
#         print("here is two argument")

# obj = Arithmatic()
# obj = Arithmatic(10)
# obj = Arithmatic(2,2)




#method overriding(parent & child relationship must be there)    
# class Rbi:
#     def home_loan(self):
#         print("home loan = 7.5%")

#     def car_loan(self):
#         print("car loan= 8%")

# class Sbi(Rbi):
#     def home_loan(self):
#         print(" provide home loan = 6.5%")
#         super().home_loan()             # using super method you can access the parent class method in child class

# obj = Sbi()  
# obj.home_loan()     #child class method override the parent class method




#constructor overriding
# class Father:
#     def __init__(self):
#         print("father: i am already at breakfast table")

# class Child(Father):
#     def __init__(self):
#         print("child:i will be late for breakfast")
#         super().__init__()       # using super method you can access the parent class method in child class


# obj = Child()



    