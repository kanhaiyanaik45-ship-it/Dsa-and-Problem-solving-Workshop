# n = int(input("Enter size of matrix: "))

# matrix = []
# a = []
# for i in range(n):
#     row = list(map(int, input(f"Enter row {i+1} elements: ").split()))
#     matrix.append(row)

# print("Matrix is:")
# for row in matrix:
#     print(row)
#     a.append(max(row))

# print("---------------------")
# print(a)
# remove leading zeros 
# ip = [0, 0, 1, 2, 0, 3, 0, 4]
# while ip and ip[0] == 0:
#     ip.pop(0)
# print(ip)
        

#--------------------------------------------regular expression----------------------------------------------------

# import re

# count = 0
# pattern = re.compile("function")
# # print(pattern)
# matcher = pattern.finditer("function in python is defined by a def statement. python the function is a block of code that is used to perform a single, related action. functions are used to organize code into reusable blocks.")
# # print(matcher)
# for i in matcher:
#     count += 1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurrences:",count)


# import re
# count = 0
# matcher = re.finditer("Hi","HiHiHiHi")

# for i in matcher:
#     count += 1
#     print(i.start(),".......",i.end(),".....",i.group())
# print("the number of ocrance",count)




# import re
# obj =input("Enter any chracter")
# objmatch = re.finditer(obj,"a45b @k9z")

# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())



# match function used at starting or begining to match the word

# import re
# a = input("Enter string to perform match operation:")
# match = re.match(a,"python is very important language")
# print(match)

# if match != None:
#     print("match found at begining level")
#     print(match.start()," ",match.end())
# else:
#     print("match not found at begining level")
    



# fullmatch function used to full string matching. sometimes used in validation
# import re
# a = input("Enter string to perform match operation:")
# match = re.fullmatch(a,"pythonisvery")
# print(match)

# if match != None:
#     print("match found ")
#     print(match.start()," ",match.end())
# else:
#     print("match not found ")


# #search function is used if the match is found anywhere in string
# import re
# a = input("Enter string to perform match operation:")
# match = re.search(a,"python is very important language")
# print(match)

# if match != None:
#     print("match found ")
#     print(match.start()," ",match.end())
# else:
#     print("match not found ")




# import re
# a = input("enter string:")
# f = open("paragraph.txt", "r")
# c = f.read()
#    # define what you want to match
# mtch = re.search(a, c)
# print(mtch)
# if mtch != None:
#     print("match found")
#     print(mtch.start(), mtch.end())
# else:
#     print("match not found")


# #findall
# import re
# mtch = re.findall('[^A-Za-z0-9]',"ASJrwrugyefiaU3726587@#$")  #^it  is used to not taken in []
# print(mtch)



#substitution function (expression,replacement,string)
# import re 
# obj = re.sub('[a-zA-Z]','*','1234 dskg dshJ kgUD')
# print(obj)

# subn()similar to sub diffrent is it return number of replacement
# import re
# obj = re.subn('[0-7]','@','asd987tr234@#$')
# print(obj)
# print("the string is = ",obj[0])
# print("the number of replacement is = ",obj[1])



#mobile novalidation
# import re
# mo = input("enter mobile no")
# obj = re.fullmatch("[0-9]\d{9}",mo)
# if obj != None:
#     print("valid mobile number")
# else:
#     print("invalid mobile number")



#gmail validation
# import re
# s = input("Enter email id: ")
# m = re.fullmatch("\w[a-zA-Z0-9_.]*@gymail[.]com", s)
# if m != None:
#     print("valid email id")
# else:
#     print("invalid email id")



# import os,sys
# fname = input("Enter file name:")
# if os.path.isfile(fname):
#     print("file exist:",fname)
#     f = open("fname",'r')
# else:
#     print("file dosen't exist",fname)
#     sys.exit(0)
# print("the content of file is:")
# data = f.read()
# print(data)