# def powerofTwo(n):
#     if n == 0:
#         return 1
#     else:
#         power = powerofTwo(n-1)
#         return power*2

  
# #factorial
# def factorial(num):
#     if num <= 1:
#         return 1
#     return num * factorial(num - 1)
# print(factorial(4))
# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return isPalindrome(strng[1:-1])    
# print(isPalindrome('awesome'))
# print(isPalindrome('foobar'))
# print(isPalindrome('tacocat'))


# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent-1)
# print(power(2,0))
# print(power(2,2))
# print(power(2,4))

        
# def  capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])
# print(capitalizeFirst(['car','taco','banana']))


# def productofArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productofArray(arr[1:])
# print(productofArray([1,2,3]))
# print(productofArray([1,2,3,10]))


# def fib(num):
#     if (num < 2):
#         return num 
#     return fib(num - 1) + fib(num - 2)
# print(fib(4))
# print(fib(10))
# print(fib(28))
# print(fib(35))


# class Node:
#     #create a node in the tree
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None


# class Node:
#     # create a node in the tree
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.root = None
         
#     def insert(self, value):
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self.insertNode(self.root, value)

#     def insertNode(self, rootNode, value):
#         if value < rootNode.value:
#             if rootNode.left is None:
#                 rootNode.left = Node(value)
#             else:
#                 self.insertNode(rootNode.left, value)
#         else:
#             if rootNode.right is None:
#                 rootNode.right = Node(value)
#             else:
#                 self.insertNode(rootNode.right, value)   #

# # Testing
# btObj = BinaryTree()
# btObj.insert(50)   
# btObj.insert(30) 
# btObj.insert(70) 

# print(btObj.root.value)        # 50
# print(btObj.root.left.value)   # 30
# print(btObj.root.right.value)  # 70