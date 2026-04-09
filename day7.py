# #sort dictionary by key or value
# ip= {"A":1,"B":2,"C":3}
# #op ={c,b,a}
# desc = dict(sorted(ip.items(),reverse=True))
# asc = dict(sorted(ip.items()))
# print(asc)
# print(desc)


#remove all element from dict
# ip = {"A":1,"B":2,"C":3}
# a = ip.clear()
# print(ip)

# count the number of non empty values
# ip = {"A":1,"B":"","C":3,"D":None,"E":"five"}
# count = 0
# for i in ip:
#     if ip[i] !="" and ip[i] != None:
#         count += 1
# print(count)



#----------------------------------------queue----------------------------------
# import sys
# class Queue:
#     def __init__(self, queuesize):
#         self.queuelist =[]
#         self.Queuesize = queuesize

#     def isFull(self): 
#         if len(self.queuelist) == self.Queuesize:
#             return True
#         else:
#             return False
#                                                 #stack implementation with size limit
#     def enqueue(self, value):
#         if self.isFull():
#             print("queue is full")
#         else:
#             self.queuelist.append(value)
        
        
#     def displayqueue(self):
#         print("----------------------")
#         print(self.queuelist)
#         print('--------------------')

#     def isempty(self):
#         if self.queuelist == []:
#             return True
#         else:
#             return False
        
#     def dequeue(self):
#         if self.isempty():
#             return "queue is empty: "
#         else:
#             return self.queuelist.pop()
        
#     def deletequeue(self):
#         self.queuelist = None
#         return "queue is deleted" 
#         if self.dequeue == True:
#             self.enqueue()
            

    
#     def peek(self):
#         if self.isempty():
#             return "queue is empty"
#         else:
#             return self.queuelist[0]
        
# size = int(input("enter the size of queue"))            
# queueobj = Queue(size)                                            

# while True:

#     print("1.enqueue element in queue")
#     print("2.display element in queue")
#     print("3.check queue isempty")
#     print("4.dequeue operation")
#     print("4.delete operation")
#     print("6.peek operation")
#     print("7. Create New Queue")
#     print("exit")

#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#         val = int(input("Enter the value for queue :"))
#         queueobj.enqueue(val)
#     elif choice == 2:
#         queueobj.displayqueue()
#     elif choice == 3:
#         print(queueobj.isempty())
#     elif choice == 4:
#         print(queueobj.dequeue())
#     elif choice == 5:
#         print(queueobj.deletequeue())
#     elif choice == 6:
#         print(queueobj.peek())
#     elif choice == 7:
#         size = int(input("Enter new queue size: "))
#         queueobj = Queue(size)
#         print("New queue created!")
#     else:
#         sys.exit()              
 

#-----------------------------------time complexity---------------------------------

# 1)    constat time :- o(1) for accessing single element 
# 2)    o(n) is liner complexity. it visits every element of an array  e.g for loop for an array 
# 3)    o(log) is logarthmic time .it is visiting only some elements e.g:-binary search . 
# 4)    o(n^2) is quadratic time. it looking array every index in the array twice eg.for x in arr:
#                                                                                      for y in arr:
#                                                                                          print(x,y)
# 5)    o(2^n) is exponantial .it is double recursion. e.g fibonaci
                                                            #def fib(n):
                                                            # if n <=1 :
                                                            #   return n
                                                            #return fib(n-1) + fib(n-2)


#                                   time complexity           space complexity
#create stack                           o(1)                        o(1)
# push                                  o(1)/o(n^2)                 o(1)
# pop                                   o(1)                        o(1)
# peek                                  o(1)                        o(1)
# isempty                               o(1)                        o(1)
# delete enter stack                    o(1)                        o(1)


# there is 2 way to implelement stack list and linked list in python

# In python

# stack using list:
# -easy to implement
# -speed problem when it grows

# stack using linked list:
# -fast performance
# -implementation is not easy


#                                   time complexity           space complexity
#create queue                           o(1)                        o(1)
# enqueue                               o(n)                        o(1)
# dequeue                               o(n)                        o(1)
# peek                                  o(1)                        o(1)
# isempty                               o(1)                        o(1)
# delete entier Queue                   o(1)                        o(1)


#find biggest number
# def findbiggestNumber(arr):
#     first_value = arr[0]            #o(1)
#     for i in range(1,len(arr)):     #o(n) 
#         if arr[i] > first_value :   #o(1)
#             first_value = arr[i]     #o(1)
#     return first_value              #o(1)
    
        
# arr = [2,3,4,4,1,7,9,2,5,6,1,8]  
# print(findbiggestNumber(arr))

# #time cmplexity :o(1)+o(n)+o(1) = o(n)



#special chracter
# ip = "jdbs54@#jvd$dh!"
# count = 0
# for i in ip:
#     if not i.isalnum():
#         count+=1
# print(count)

# import math
# size = int(input("Enter the number of elements: "))
# a = []

# for i in range(size):
#     element = int(input(f"Enter element {i+1}: "))
#     a.append(element)

# count = 0
# for i in a:
#     if math.sqrt(i).is_integer():
#         count += 1
# print("square roots count:", count)




# def linearSearch(array,target):                 #o(n)
#     for i in range (len(array)):                #o(n)
#         if array[i] == target:                  #o(1)
#             return i                            #o(1)
#     return -1                                   #o(1)
    
# array =[1,2,3,4,5,6,7,8,9]
# target = 4
# result=linearSearch(array, target)
# if result == -1:
#     print("not found")
# else:
#     print('Element found at index no=',result)




#-------------------------------------------binary search-------------------------------
# def binarySearch(array,target): 
#     start = 0
#     end = len(array)-1
#     while start <= end:
#         mid = (start+end) //2
#         if array[mid] == target:
#             return mid
#         elif array[mid]< target:
#             start = mid+1
#         else:
#             end = mid -1
#     return -1 
    
# sorted_array =[1,2,3,4,5,6,7,8,9]
# target = 44
# result=binarySearch(sorted_array, target)
# if result == -1:
#     print("not found")
# else:
#     print('Element found at index no=',result)




#----------------------------------------linked list-------------------------------------
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

# linkedlist = LinkedList()

# linkedlist.head = Node(5)  # first node
# second = Node(10)
# third = Node(15)
# fourth = Node(20)

# #linking part
# linkedlist.head.next = second
# second.next = third
# third.next=fourth

# print(linkedlist.head.data)
# print(second.data)
# print(third.data)
# print(fourth.data)




# #display linkedlist
# while linkedlist.head != None:
#     print("|",linkedlist.head.data,"|",linkedlist.head.next,"->", end=" ")
#     linkedlist.head =linkedlist.head.next



# import sys
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        

# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def addNode(self,value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node

#     def addNodeBeggining(self, value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             node.next = self.head
#             self.head = node

#     def addNodeinBetween(self,index, value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         elif index == 0:
#             node.next = self.head
#             self.head - node
#         else:
#             temp = self.head
#             for _ in range(index - 1):
#                 temp = temp.next
#             node.next = temp.next
#             temp.next = node


#     def addNodeatEnd(self,value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node

#     def displayNode(self):
#         print("------------------------")
#         while self.head is not None:
#           print("|",self.head.data,"|","===>",end=" ")
#           self.head=self.head.next
#         print("------------------------")

#     def searchNode(self, value):
#         current = self.head
#         while current is not None:
#             if current.data == value:
#                 return print("Node search successfully")
#             current = current.next
#         return print("node is not found")

    

# #link list add,del,
# if __name__ =='__main__':
#     object = Linkedlist()

#     while True:
#         print("1. Add node linkedlist:")
#         print("2. Add node in begining:")
#         print("3. Add node in between:")
#         print("4. Add node in end:")
#         print("5. Display linkedlist:")
#         print("6. Search Node:")
#         print("7.exit")

#         ch = int(input("Enter your choice:"))
#         if ch == 1:
#             value = int(input("enter value for node:"))
#             object.addNode(value)
#             print("node added successfully insingle linkedlist")

#         elif ch == 2:
#             value = int(input("enter value for node:"))
#             object.addNodeBeggining(value)
#             print("node added successfully insingle linkedlist")

#         elif ch == 3:
#             value = int(input("enter value for node:"))
#             index = int(input("enter position after that you have to insert"))
#             object.addNodeinBetween(index,value)
#             print("node added successfully insingle linkedlist")


#         elif ch == 4:
#             value = int(input("enter value for node:"))
#             object.addNodeatEnd(value)
#             print("node added successfully insingle linkedlist")



#         elif ch == 5:
#             object.displayNode()

#         elif ch == 6:
#             value = int(input("enter value for node:"))
#             object.searchNode(value)
            


#         elif ch == 7:
#             sys.exit()

#         else:
#             print("Invalid choice")
