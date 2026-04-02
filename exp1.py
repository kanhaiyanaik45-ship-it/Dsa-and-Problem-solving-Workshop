# math= 50
# chem = 50
# name = "sagar"
# pi = 3.14
# result = True
#print(type(math))           for type
#print(type(name))
#print(type(pi))
#print(type(result))

#print(id(math))           for address
#print(id(name))
#print(id(pi))
#print(id(result))

#print(id(math))         for same address
#print(id(pi))

# print(id(math))         for diffrent address
# print(id(chem))
# print(id(pi))


# part 2

# list = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]

# print(list[1][1])


# part3 typecasting
# print(2+2)
# print("2" + "2")
# val1 = input("enter value of val1:") #2 
# val2 = input("enter value of val2:") #4
# print(val1 + val2) # ans is 24 bcz input function bydefaults accepts only string value

# val1 = int(input("enter value of val1:")) #2 
# val2 = int(input("enter value of val2:")) #4
# print(val1 + val2) # ans is 6



#1.int
# print(int(3.14))
# #print(int(10+5j))   error
# print(int(True))          
# print(int(False))
# #print(int("10.23"))    error
# print(int("4"))
# #print(int("sagar"))  error


#2.float
# print(float(3))
# #print(float(10+5j))    error   
# print(float(True))          
# print(float(False))
# print(float("10.23"))    
# print(float("4"))
# #print(float("sagar"))     error



#complex
# print(complex(3))
# print(complex(12.5))
# print(complex(True))          
# print(complex(False))
# print(complex("10.23"))    
# print(complex("4"))
# #print(complex("sagar"))     #error
# print(complex(True,False))


#bool
# print(bool(0.0))
# print(bool(0))
# print(bool(True))          
# print(bool(False))
# print(bool(10.23))    
# print(bool("4"))
# print(bool("sagar"))     
# print(bool())

#swaping
# val1 = int(input("enter 1st no:-"))
# val2 = int(input("enter 1st no:-"))
# print("before swapping",val1,",",val2)
# a=val1
# val1= val2
# val2 = a
# print("after swapping",val1,",",val2)

#using 2var
# val1 = int(input("enter 1st no:-"))
# val2 = int(input("enter 1st no:-"))
# print("before swapping",val1,",",val2)
# val1= val1+val2
# val2=val1-val2
# val1=val1-val2
# print("after swapping",val1,",",val2)


#total and percentage
# val1 = int(input("enter 1st no:-"))
# val2 = int(input("enter 2nd no:-"))
# val3 = int(input("enter 3rd no:-"))
# total = val1+val2+val3
# per = total/3.0
# print("Total=",total)
# print("Percentage",per)



#simple intrest
# p_amount=int(input("enter the principle amount:"))
# rot=int(input("enter the rate  amouof interesnt:"))
# time=int(input("enter the duration of loan amt:"))
# si=p_amount*rot*time/100
# print("simple interest",si)


#height of user and convert into inches and cm
# feet=float(input("enter the height in feet :"))
# inch = feet*12
# cm = inch*2.54
# print("in inch",inch)
# print("in centimeter",cm)


#reverse a number   
# num = 123456
# a = num%10
# num = num//10
# b = num%10
# num = num//10
# c = num%10
# num = num//10
# d= num%10
# num = num//10
# e = num%10
# num = num//10
# f = num%10
# num = num//10
# rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f 
# print("reverse of a number is",rev)



#idenity opratror
# a=10
# b=10
# print(a is b)   #true
# print(a is not b)   #false



# membership operator
# name="sagar"
# print("s" in name)  #true
# print("z" in name)  #false


#acept any no and check pos neg 0
# no = int(input("enter any number:"))
# if no>0:
#     print("number is positive")
# if no<0:
#     print("number is negative")
# if no==0:
#     print("number is zero")



#maximum no 5
# a=int(input("enter 1st no:"))
# b=int(input("enter 2nd no:"))
# c=int(input("enter 3rd no:"))
# d=int(input("enter 4th no:"))
# e=int(input("enter 5th no:"))
# if a>b and a>c and a>d and a>e:
#     print(a," is maximum")
# if b>a and b>c and b>d and b>e:
#     print(b," is maximum")
# if c>a and c>b and c>d and c>e:
#     print(c," is maximum")
# if d>a and d>b and d>c and d>e:
#     print(d," is maximum")
# if e>a and e>b and e>c and e>d:
#     print( e,"is maximum")   




# username= input("enter username:")
# password= input("enter password:")
# if username == password:
#     print("login successful")
# else:    print("login failed")



#wap to accpt physics,chemestry and math subject marks calculate total and percentage and if percentage is grater than eqal to60 and gender is equal to mail eligible for placement else eligible for data ntry

# phy = int(input("enter physics marks:"))
# chem = int(input("enter chemistry marks:")) 
# math = int(input("enter math marks:"))
# gender = input("enter gender:")
# total = phy + chem + math
# per = total/3.0
# if per >= 60 and gender == "male":
#     print("eligible for placement") 
# else:    print("eligible for data entry")





#wap to accept a,,c and find max
# a = int(input("enter 1st no:"))
# b = int(input("enter 2nd no:"))
# c = int(input("enter 3rd no:"))
# if a>b :
#     print(a," is maximum")
#     if a>c:
#        print(a," is maximum")
#     else: 
#         print(c," is maximum")
# else: 
#     if b>c :
#         print(b," is maximum")
#     else:
#         print(c," is maximum")





#wap to find if itis weekend or weekday
# day = input("enter your day name:")
# if day == "saturday" or day =="SATURDAY" or day == "sunday" or day == "SUNDAY" :
#     print("it is weekend")
# else:
#     print("it is weekday")




# #wap to accept enter num char and special char and find which one is it
# char = ord(input("enter any char:"))
# if char >=65 and char<=91:
#      print("it is a character is in uppercase")
# elif char>=97 and char<=122:
#      print("it is a character is in lowercase")
# elif char>=48 and char<=57:
#      print("it is a number")
# else:
#     print("it is a special character")



# # notes 
# amt = int(input("enter amount to withdraw:"))
# print("number of 100 notes",amt//100)
# print("number of 50 notes",(amt%100) //50)
# print("number of 20 notes",((amt%100) %50) //20)
# print("number of 10 notes",(((amt%100) %50) %20) //10)
# print("number of 5 notes",((((amt%100) %50) %20) %10) //5)



