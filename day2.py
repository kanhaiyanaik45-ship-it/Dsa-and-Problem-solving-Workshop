#indexing
# name = "sagarnaik"
# print(name[0])  
# print(name[1])
# print(name[-1])
# #print(name[15])       #error
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[0:8:2])
# print(name[::-1])



#functions
# s = "Python is a programming Language"
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.capitalize())
# print(s.swapcase())



#formatting
# print("subject marks:")
# phys = 50
# math= 50
# chem = 50
# print("physics={} chemistry={} math={}".format(phys,chem,math))
# print("physics={0} chemistry={1} math={2}".format(phys,chem,math))
# print("physics={x} chemistry={y} math={z}".format(x=phys, y=chem, z=math))
# total = phys + chem + math
# print("total marks={}".format(total))
# print("roll no = {}".format("7".zfill(4)))




#looping
# for i in range(5):
#     print(i)  
# for i in range(1,5):
#     print(i)
# for i in range(1,10,2):
#     print(i)
# for i in range(1,11):       # table of 2
#     print(i*2)
# for i in range(1,11):       # table of 3
#     print(i*2,"",i*3,"", i*4,"", i*5,"", i*6, "",i*7, "",i*8, "",i*9, "",  i*10)
# print("---------------------------------------------------------------------")    

# for i in range(1,11): 
#     print("  ",i*11,"  ",i*12,"  ",i*13,"  ",i*14,"  ",i*15,"  ",i*16,"  ",i*17,"  ",i*18,"   ",i*19,"  ",i*20)


# name = "sagarnaik"
# for i in name:
#     print(i)



#wap to remove duplicates
# name = "sagarnaik"
# new_name = ""
# for i in name:
#     if i not in new_name:
#         new_name = new_name + i

# print(new_name)




#
# for i in range(10,0,-2):
#     print(i)



# wap toreverse a string
# name = "Mumbai"
# n= len(name)
# new_name = ""
# for i in range(n-1,-1,-1):
#     new_name += name[i]
# print(new_name)





#wap to palindrome
# name = "mumbai"
# n= len(name)
# new_name = ""
# for i in range(n-1,-1,-1):
#     new_name += name[i]
# print(new_name)

    
# if new_name == name:
#     print("string is palindrome")
# else:
#     print("sring is not palindrome")




#+----------------+-----------------+-------tuple---------+----------------+----------------+
from turtle import listen


mytuple = ("sagar","bhaskar","vishram","tushar",45,"nana",12,19,"sanjiv")
# print(mytuple)
# print(type(mytuple))

# mytuple[2] = "sunil"
# print(mytuple)

# init_tuple = ()
# print(init_tuple.__len__())





# init_tuple_a= 'a','b'
# init_tuple_b=('a','b')
# print(init_tuple_a == init_tuple_b)
# print(id(init_tuple_a))
# print(id(init_tuple_b))





# a=('1','2')
# b=('3','4')
# print(a+b)




# init_tuple = ('python',)*3
# print(type(init_tuple))





# init_tuple = (1,)*3
# init_tuple[0] = 2
# print(init_tuple)





# init_tuple = ((1,2),)*7
# print(len(init_tuple[3:8]))


# a = [4,0,2,5,0,1]
# for i in a:
#     if i == 0:
#         a.remove(i)
#         a.append(i)
# print(a)





# ip=[1,2,2,3,4,4,5]
# eo=[]
# for i in ip:
#     if i not in eo:
#         eo.append(i)
# print(eo)




#common element
# a=[1,2,3] 
# b=[2,3,4]
# c=[3,4,5]
# op=[]
# for i in a:
#     if i in b and i in c:
#         op.append(i)

# print(op)



# n=int(input("enter the size of elements in list: "))
# arr=[]
# for i in range(n):
#     val = int(input("enter the element: "))
#     arr.append(val)
# sum =0
# for i in range(n):
#     if i+1 in range(n):
#         sum += abs(arr[i]-arr[i+1])
# print(sum)



# for i in range(1,6):
#     if i==3:
#         continue
#     print(i)


# for i in range(5,0,-1):
#     if i==3:
#         continue
#     print(i)

#this code is for both upper code
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i,j)





# a = "sagar*is*a*good*programmer"
# newname = ""
# val =""
# for i in a:
#     if i != "*":
#         newname += i
#     else:
#         val += i

# print(newname)
# print(str(val+newname))





# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print((a+(b*c)/d))



# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x !=z)
# print(id(x))
# print(id(y))
# print(id(z))    




# a = "listen"
# b = "silent"
# if sorted(a) == sorted(b):
#     print("anagram")



#counts words in string
# a = "this is a sentence"
# count = 1
# for i in a:
#     if i == " ":
#         count += 1
# print(count)



ip = [1,2,3,4]
for i in ip:
    if i == i:



    
    

























