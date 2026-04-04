# #rearrange postive to negative in alternating way
# ip = [-1,2,-3,4,5,-6]
# op = []
# for i in ip:
#     if i < 0:
#         op.append(-i)
#     else:
#         op.append(-i)
# print(op)








#dictionaryyy

# mydict = {101:"sagar",
#           102:"vishram",
#           103:"sanjiv",
#           104:"tushar",
#           107:"bhaskar",
#           104:"nana",
#           "104":"dayanand"}
# # print(mydict)
# a = mydict[102]
# print(a)

# mydict[101] = "sunil"
# print(mydict) 

# for x in mydict:
    # print(x)

# for x in mydict.values():
#     print(x)


# for x,y in mydict.items():
#     print(x,y)

# mydict["mobile_number"] = 9529784765
# print(mydict)

# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# a={'a':1,'b':2,'c':3}    #error
# print(a['a','b'])  


# arr={}
# arr[1]= 1
# arr['1']= 2
# arr[1]+= 1
# print(arr)
# sum = 0
# for i in arr:
#     sum+= arr[i]
# print(sum)


# my_dict ={}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# print(my_dict)
# sum = 0
# for i in my_dict:
#     sum+= my_dict[i]    
# print(sum)



# my_dict ={}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for i in my_dict:
#     sum+= my_dict[i]
# print(sum)





# box = {}   #type error
# jars = {}
# crates = {}
# box['Biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))




# dict={'c':97,'a':96,'b':98 }
# for _ in sorted(dict):
#     print(dict[_])


# rec = {"name":"Python","age":20}
# r = rec.copy()
# print((id(r)) ==(id(rec)))
# print(id(r))
# print(id(rec))




# rec = {"name":"Python","age":20,"Addr":"New York"}
# id1 = id(rec)
# print(id1)
# del rec
# rec = {"name":"Python","age":20,"Addr":"New York"}
# id2 = id(rec)
# print(id1 == id2)
# print(id1)
# print(id2)


# ip = {"x":20,"y":10,"z":30 }
# op = min(ip,key=ip.get)
# print(op)



# mydict = {101:"sagar",
#           "profession":"developer",
#           "empid":12345,}
# mydict.pop(101)
# print(mydict)




# for i in range(1,4):         #outer loop
#     for j in range(1,4):       #inner loop
#         print(i, end=" ")
#     print()

    


# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")


# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):     
#     for j in range(1,1+i):     
#         print(chr(64+i), end=" ")       ##in print we use i for same  in row
#     print()


# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):           #n+1=6 
#     for j in range(1,n+2-i):     #7-1=6, 7-2=5, 7-3=4, 7-4=3, 7-5=2
#         print("*", end=" ")
#     print()


# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):           #n+1=6 
#     for j in range(1,n+2-i):     #7-1=abcde, 7-2=abcd, 7-3=abc, 7-4=ab, 7-5=a   
#         print(chr(64+j), end=" ")    #in print we use j for same  in column
#     print()




# import time
# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):           #n+1=6 
#     for j in range(1,n+2-i):
#         time.sleep(2)
#         print(n+1-i, end=" ")     
#     print()





# import time
# n = int(input("enter the number of rows: "))
# for i in range(1,n+1): 
#     print(" "*(n-i),end=" ")          
#     for j in range(1,i+1):
#         time.sleep(2)
#         print("*", end=" ")     
#     print()


#-------------+----------+-----------functions in python+--------------+-------------+--------+

# def msg():
#     print("hello world")

# msg()
# msg()


# def arithmatic():
#     a = int(input("enter the first number: "))
#     b = int(input("enter the second number: "))
#     add = a + b
#     sub = a - b
#     mul = a * b
#     div = a / b 
#     return add,sub,mul,div

# # print(arithmatic())
# result = arithmatic()
# print("arithmatic ",result)




# how many times arugument we passed
# ->1.positinal
# 2.keywords
# 3.default
# 4.variable number /variable length


#positional argument
# def login(username, password):
#     if username == password:
#         print("login successfully")
#     else:
#         print("login failed")

# username = input("enter the username: ")
# password = input("enter the password: ")
# login(username, password)


#keyword argument
# def login(username, password):
#     if username == password:
#         print("login successfully")
#     else:
#         print("login failed")

# login(username="admin", password="admin")



# #default argument
# def cityName(city="goa"):      #default argument
#     print(city)

# cityName("pune")
# cityName("mumbai")  
# cityName()


#variable length of argument
# def nameofcities(*city):
#     print("city names =",city)
# nameofcities("pune","mumbai","goa","delhi")

#wap for menu driven code

# import sys
# def add():
#     a = int(input("enter the first number: "))
#     b = int(input("enter the second number: ")) 
#     print("Add:-",a+b)

# def sub():
#     a = int(input("enter the first number: "))
#     b = int(input("enter the second number: ")) 
#     print("Sub:-",a-b)

# def mul():
#     a = int(input("enter the first number: "))
#     b = int(input("enter the second number: ")) 
#     print("Mul:-",a*b)

# def div():
#     a = int(input("enter the first number: "))
#     b = int(input("enter the second number: ")) 
#     print("Div:-",a/b)


# while True:
#     print(" 1.Addition")
#     print("2.Substraction")
#     print("3.Multiplication")
#     print("4.Division") 
#     print("5.exit")
#     choice = int(input("enter your choice:-"))

#     if choice ==1:
#         add()
#     elif choice ==2:
#         sub()
#     elif choice == 3:
#         mul()
#     elif choice == 4:
#         div()
#     elif choice == 5:
#         sys.exit()
#     else:
#         print("invalid choice")





#rstrip() ===> to remove space at right hand side
#lstrip() ===> to remove space at left hand side
# strip() ===> o remove space both side


programming = input("Enter your programming name:-")
p_name = programming.rstrip()
if p_name =='python':
    print(p_name)
elif p_name == 'Java':
    print(p_name)
elif p_name == 'Cpp':
    print(p_name)
else:
    print("Wrong programming name:")
