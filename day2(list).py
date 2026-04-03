# mylist = ["sagar","bhaskar","vishram","tushar",45,"nana",12,19,"sanjiv"]
# print(mylist)
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])        
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[2:6:2])
# print(mylist[::2])
# print(mylist[:])


# mylist[5] = "arjun"
# print(mylist)

# if "dayanand" in mylist:
#     print("yes dayanand is present in list")
# else:
#     print("no dayanand is not present in list")


# mylist.append("dayanand")
# mylist.append("subhash")
# print(mylist)

# mylist.insert(2,"shankar")
# print(mylist)


# mylist.remove("sagar")
# print(mylist)


# newList= mylist
# print(mylist)
# print(newList)


 


# #multidimensional list
# list = [["sagar",45],[16.30],["bhaskar",12]]
# print(list)
# print(list[0][0])
# print(list[0][1])
# print(list[1][0])
# print(list[2][0])
# print(list[2][1])




# list=["sagar","nik"]
# # print(list*2)

# list2=[50,89,56]
# print(list+list2)



# list2=[50,30,4,67,'sagar']
# # del list2
# # del list2[2]
# # list2.clear()
# print(list2)





# name="sagar"
# print(name)
# myname=list(name)
# print(myname)



# mylist=[49,90,6,98]
# mylist.sort()
# print(mylist)
# mylist.sort(revrse=True)
# print(mylist)
# mylist.reverse()
# print(mylist)


# mylist=[49,90,6,98]
# newlist=mylist
# print(id(mylist))
# print(id(newlist))
# mylist[0]="sagar"
# print(mylist)
# print(newlist)



# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())



# arr =[1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]
# for i in range(0,6):
#     print(arr[i])





# a = [1,2,3,4,5,6,7,8,9,10,11]         #value error
# a[::2]=[10,20,30,40,50,60]
# print(a)                          



a=[1,2,3,4,5]
print(a[3:0:-1])
