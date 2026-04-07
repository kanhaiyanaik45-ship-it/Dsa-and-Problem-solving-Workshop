#reverse each word in string
# ip = ("hello world")
# list = ip.split()
# new_list=[]
# for item in list:
#     new_list.append(item[::-1])
# print(" ".join(new_list))



#by relacing consicutive character
# string = "aaabbbccc"
# newstring = ""
# count = 1
# for i in range(len(string)-1):
#     if string[i] == string[i+1]:
#         count = count + 1
#     else:
#         newstring = newstring + string[i] + str(count) 
#         count = 1
# newstring = newstring +   string[len(string)-1] +str(count)
# print(newstring)


#Abstraction
#at least one abstract methodin class



# from abc import ABC,abstractmethod
# class Help4code(ABC):
#     @abstractmethod
#     def training(self):
#         pass

#     @abstractmethod
#     def placement(self):
#         pass

# class Ashish(Help4code):
#     def training(self):
#         print("c,c++,java")

#     def placement(self):
#          print("java")

# class Ankush(Help4code):
#     def training(self):
#         print("python,Django")

#     def placement(self):
#          print("python")

# class Vishal(Help4code):
#     def training(self):
#         print("practice learning")
#     def placement(self):
#         print("Python placement")

# obj1 = Ashish()
# obj2 = Ankush()
# obj3 = Vishal()
# obj1.training()
# obj1.placement()
# obj2.training()
# obj2.placement()
# obj3.training()
# obj3.placement()



# from abc import ABC,abstractmethod
# class Irctc(ABC):
#     @abstractmethod
#     def bookticket(self):
#         pass

# class Makemytrip(Irctc):
#     def bookticket(self):
#         print("=============================================")
#         print("welcom to makemytrip.com")
#         sorce = input("Enter a source station name:")
#         destination = input("Enter a destination station name:")
#         date = input("Enter date:")
#         print("=============================================")

# class Goibibo(Irctc):
#      def bookticket(self):
#         print("=============================================")
#         print("welcom to Goibibo.com")
#         sorce = input("Enter a source station name:")
#         destination = input("Enter a destination station name:")
#         date = input("Enter date:")
#         print("=============================================")

# class yatra(Irctc):
#      def bookticket(self):
#         print("=============================================")
#         print("welcom to yatra.com")
#         sorce = input("Enter a source station name:")
#         destination = input("Enter a destination station name:")
#         date = input("Enter date:")
#         print("=============================================")

# obj1 = Makemytrip()
# obj2 = Goibibo()
# obj3 = yatra()
# obj1.bookticket()
# obj2.bookticket()
# obj3.bookticket()   




# class Base:
#     def __init__(self):
#         print("Parent class consturctor called")
#         self.a ="prashant"
#         self.__c = "Ashish"    #__c is privet varriable 
#         self._c = "sagar"    #_ is protected variable
# class Derived:
#     def __init__(self):
#         Base.__init__(self)
        # print("calling privet member of base class")
        # print(self.a)
        # print(self.__C)       #it is not accessable

# obj1 = Derived()
# print(obj1.a)
# print(obj1.__c)
# obj2 = Base()
# print(obj2.a)
# print(obj2.__c)     #it is not accessable


# class Rbi:
#     #delcaring public method
#     def publicPolicy(self):
#         print("check public poliocy of Rbi")

#     #declaring private method
#     def __privatepolicy(self):
#         print("there is some private policy which is not accesible for public")

# class Sbi(Rbi):
#     def __init__(self): #first sbi class const called
#         Rbi.__init__(self) #second parent class constr called
    
#     def callingPublicMethod(self): #childclass public method
#         print("\n inside child class")
#         self.publicPolicy() #calling parentclass public method

#     def callingPrivateMethod(self): #childclass public method
#         self.privatePolicy() #calling parentclass private method

# obj1 = Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()
# obj1.publicPolicy()
# obj1.__privatepolicy()
# obj2 = Rbi()
# obj2.publicPolicy()
# obj2.__privatepolicy()
# obj2 = Rbi()
# obj2.publicPolicy()
# obj2._Rbi__privatepolicy()      




# ip = [10,98,3,33,12,22,21,11]
# even =[]
# odd = []
# for i in ip:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even+odd)



#----------------------------------------------DATA STRUCTURE----------------------------------------------
#1.stack implementation without size limit
# import sys
# class Stack:
#     def __init__(self):
#         self.stacklist =[]                                  #1.stack implementation without size limit
#     def push(self, value):
#         self.stacklist.append(value)
        
#     def displayStack(self):
#         print("----------------------")
#         print(self.stacklist)
#         print('--------------------')

#     def isempty(self):
#         if self.stacklist == []:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isempty():
#             return "stack is empty: "
#         else:
#             return self.stacklist.pop()
        
#     def deletestack(self):
#         self.stacklist = None
#         return "stcak is deleted" 
    
#     def peek(self):
#         if self.isempty():
#             return "stcak is empty"
#         else:
#             return self.stacklist[-1]
           
# stackobj = Stack()                                            #2.stack implementation with size limit

# while True:

#     print("push element in stack")
#     print("display element in stack")
#     print("check isempty")
#     print("pop operation")
#     print("delete operation")
#     print("peek operation")
#     print("exit")

#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#         val = int(input("Enter the value for stack :"))
#         stackobj.push(val)
#     elif choice == 2:
#         stackobj.displayStack()
#     elif choice == 3:
#         print(stackobj.isempty())
#     elif choice == 4:
#         print(stackobj.pop())
#     elif choice == 5:
#         print(stackobj.deletestack())
#     elif choice == 6:
#         print(stackobj.peek())
#     elif choice == 7:
#         sys.exit()


#1.stack implementation with size limit
# import sys
# class Stack:
#     def __init__(self, stacksize):
#         self.stacklist =[]
#         self.stacksize = stacksize

#     def isFull(self): 
#         if len(self.stacklist) == self.stacksize:
#             return True
#         else:
#             return False
#                                                 #stack implementation with size limit
#     def push(self, value):
#         if self.isFull():
#             print("stack is full")
#         else:
#             self.stacklist.append(value)
        
        
#     def displayStack(self):
#         print("----------------------")
#         print(self.stacklist)
#         print('--------------------')

#     def isempty(self):
#         if self.stacklist == []:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isempty():
#             return "stack is empty: "
#         else:
#             return self.stacklist.pop()
        
#     def deletestack(self):
#         self.stacklist = None
#         return "stcak is deleted" 
    
#     def peek(self):
#         if self.isempty():
#             return "stcak is empty"
#         else:
#             return self.stacklist[-1]
        
# size = int(input("enter the size of stack"))            
# stackobj = Stack(size)                                            

# while True:

#     print("1.push element in stack")
#     print("2.display element in stack")
#     print("3.check isempty")
#     print("4.pop operation")
#     print("4.delete operation")
#     print("6.peek operation")
#     print("exit")

#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#         val = int(input("Enter the value for stack :"))
#         stackobj.push(val)
#     elif choice == 2:
#         stackobj.displayStack()
#     elif choice == 3:
#         print(stackobj.isempty())
#     elif choice == 4:
#         print(stackobj.pop())
#     elif choice == 5:
#         print(stackobj.deletestack())
#     elif choice == 6:
#         print(stackobj.peek())
#     elif choice == 7:
#         sys.exit()


# Tower of Hanoi
#   Rules 
#  1. we can move only one disk at a time
#  2. we have to pick upper disk from any one pipe 
#  3. we have to place on top of any disk 
#  4. we can not place any large disk on top of samller disk

# def tower_of_hanoi(n, source, middle, destination):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {destination}")
#         return
#     tower_of_hanoi(n-1, source, destination, middle)
#     print(f"Move disk {n} from {source} to {destination}")
#     tower_of_hanoi(n-1, middle, source, destination)

# n = 3
# tower_of_hanoi(n, 'A', 'B', 'C')


# import time
# class tower:
#     def __init__(self):
#         print("welcome to tower of hanoi game")
#         print()
#         print("given problem A=[3,2,1]     B=[]    c[]  ")
#         print()
#         print("expected output")

# class Tower:
#     def tower(self,item):
#         self.A.append(item)
#         time.sleep()
#         print("A:",self.A)
#         print("items in tower A \n")

#     def pass1(self):
#         self.temp = self.A.pop(2)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A :",self.A   ,"  ","B :",self.B  ,"  ","C :",self.C)
#         print("Pass one completed..............\n")

#     def pass2(self):
#         self.temp = self.A.pop(2)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A :",self.A   ,"  ","B :",self.B  ,"  ","C :",self.C)
#         print("Pass two completed..............\n")

#     def pass3(self):
#         self.temp = self.A.pop(2)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A :",self.A   ,"  ","B :",self.B  ,"  ","C :",self.C)
#         print("Pass two completed..............\n")








