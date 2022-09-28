#python program for creation of list

list=[]
print("Blank list")
print(list)
print("=====================================================================================================")


list=[10,20,30,40]
print("list of numbers")
print(list)
print("=====================================================================================================")

list=["java","python","linux"]
print("List items")
print(list[0])
print(list[1])
print(list[2])
print("=====================================================================================================")


#creating a multiple_dimension List
list=[['java','python'],['Ict','oop']]
print("Multidimensional list")
print(list)
print("=====================================================================================================")



#creating a list with multiple distinct or duplicate elements
list=[1,2,3,"java","python","linux",7,8,9]
print("List with integer and string elements")
print(list)
print("=====================================================================================================")

#printing length of list
#creating a list with multiple distinct or duplicate elements
list=[1,2,3,"java","python","linux",7,8,9]
print("List with integer and string elements")
print(list)
print("length of list is:  ",len(list))
print("=====================================================================================================")


#Adding element in the list using append()method
list=[]
list.append("oop"),list.append("java"),list.append("22"),list.append("33"),list.append("44")
print("After additiion of eleent in list")
print(list)
print("=====================================================================================================")

#adding element through a loop
list=[]
for i in range(1,4):
    list.append(i)
print("additin of element from 1-3")
print(list)
print("=====================================================================================================")

#Adding a tupple to list
list=[]
list.append((5,6))
print("additin of tuples")
print(list)
print("=====================================================================================================")


# Addition of Element at specific Position (using Insert Method)
List=["husnain","java","ict","oop","Mehrban"]
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List)
print("=====================================================================================================")

# Addition of multiple elements to the List at the end (using Extend Method)
List=["husnain","java","ict","oop","Mehrban"]
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List)
print("=====================================================================================================")


# Creating a Multi-Dimensional List (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]
# accessing an element from the
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])
print("=====================================================================================================")


# Removal of elements in a List
# Creating a List
List = [1, 2, 3, 4, 5, 6,
 7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)
# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)
# Removing elements from List
# using iterator method
for i in range(1, 5):
 List.remove(i)
print("\nList after Removing a range of elements: ")
print(List)
print("=====================================================================================================")

# Removing element from the Set using the pop() method
List = [1,2,3,4,5]
List.pop()
print("\nList after popping an element: ")
print(List)
# Removing element at a specific location from the Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List)
print("=====================================================================================================")


# Python program to demonstrate Removal of elements in a List Creating a List
List = ['G', 'E', 'E', 'K', 'S', 'F',
 'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List: ")
print(List)
# Print elements of a range using Slice operation
Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)
# Print elements from a pre-defined point to end
Sliced_List = List[5:]
print("\nElements sliced from 5th "
 "element till the end: ")
print(Sliced_List)
# Printing elements from
# beginning till end
Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)
print("=====================================================================================================")

# Creating a List
List = ['G', 'E', 'E', 'K', 'S', 'F',
 'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List: ")
print(List)
# Print elements from beginning to a pre-defined point using Slice
Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)
# Print elements of a range using negative index List slicing
Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)
# Printing elements in reverse
# using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)
print("=====================================================================================================")


# Python program to demonstrate list comprehension in Python below list contains square of all odd numbers from range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)
print("=====================================================================================================")


# for understanding, above generation is same as,
odd_square = []
for x in range(1, 11):
 if x % 2 == 1:
     odd_square.append(x**2)
print(odd_square)
print("=====================================================================================================")


# Creating a Dictionary with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
# Creating a Dictionary with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)
print("=====================================================================================================")


# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)
# Creating a Dictionary with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)
print("=====================================================================================================")


# Creating a Nested Dictionary
# as shown in the below image
Dict = {1: 'Geeks', 2: 'For',
 3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}}
print(Dict)
print("=====================================================================================================")


# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)
# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)
# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
print("=====================================================================================================")


# Adding Nested Key value to Dictionary
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}}
28
print("\nAdding a Nested Key: ")
print(Dict)
print("=====================================================================================================")


# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])
# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])
print("=====================================================================================================")


# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3))
print("=====================================================================================================")


# Creating a Dictionary
Dict = {'Dict1': {1: 'Geeks'},
 'Dict2': {'Name': 'For'}}
# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])
print("=====================================================================================================")


# Initial Dictionary
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',
 'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
 'B' : {1 : 'Geeks', 2 : 'Life'}}
print("Initial Dictionary: ")
print(Dict)
# Deleting a Key value
del Dict[6]
30
print("\nDeleting a specific key: ")
print(Dict)
# Deleting a Key from
# Nested Dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)
print("=====================================================================================================")

# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# Deleting a key using pop() method
pop_ele = Dict.pop(1)
print('\nDictionary after deletion: ' + str(Dict))
print('Value associated to poped key is: ' + str(pop_ele))
print("=====================================================================================================")


# Creating Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# Deleting an arbitrary key using popitem() function
pop_ele = Dict.popitem()
print("\nDictionary after deletion: " + str(Dict))
print("The arbitrary pair returned is: " + str(pop_ele))
print("=====================================================================================================")


# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# Deleting entire Dictionary
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)
print("=====================================================================================================")


"""
                                # Lab 2 Activity -----------Accept two lists from user and display their join------
#Solution
list1=[]
print("Enter values for first list.....")
for i in range(5):
    value=int(input("Enter value for list1 :"))
    list1.append(value)
list2 = []
print("Enter values for 2nd list.....")
for i in range(5):
    value=int(input("Enter value for list2 :"))
    list2.append(value)
list3=list1+list2
print(list3)
print("=====================================================================================================")
"""


"""
Activity 2:
A palindrome is a string which is same read forward or backwards.
For example: "dad" is the same in forward or reverse direction. Another example is "aibohphobia" 
which literally means, an irritable fear of palindromes.
Write a function in python that receives a string and returns True if that string is a palindrome and 
False otherwise. Remember that difference between upper and lower case characters are ignored 
during this determination.
"""


def isPalindrome(word):
    temp=word[::-1]
    if temp.capitalize()==word.capitalize():
        return True
    else:
        return False
print(isPalindrome("deed"))
print("=====================================================================================================")



"""
Activity 3:
Imagine two matrices given in the form of 2D lists as under; a = [[1, 0, 0], [0, 1, 0], [0, 0, 1] ]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
Write a python code that finds another matrix/2D list that is a product of and b, i.e., C=a*b
Solution:          
"""

"""
# program will print matriculation of matrix
rows=int(input("number of rows : "))
colm=int(input("number of colm : "))
A=[]
B=[]
C=[]
temp=[]
for i in range(0,rows):
    for j in range(0,colm):
        val=int(input("enter value of A : "))
        temp.append(val)
    A.append(temp)
    print(temp)
    temp=[]

for i in range(0,rows):
    for j in range(0,colm):
        val=int(input("enter value of B : "))
        temp.append(val)
    B.append(temp)
    print(temp)
    temp=[]
sum=0
for i in range(rows):
    for j in range(colm):
        for  k in range(0,rows):
            sum=sum+A[i][k]*B[k][j]
        temp.append(sum)
        sum=0
    C.append(temp)
    temp=[]
print("First input matrix is : ",A)
print("Second input matrix is : ",B)
print("Resultant matriculation of matrix is : \n",C)
for n in C:
    print(n)
print("=====================================================================================================")
"""


"""Activity 4:
A closed polygon with N sides can be represented as a list of tuples of N connected coordinates, i.e.,
[ (x1,y1), (x2,y2), (x3,y3), . . . , (xN,yN) ]. A sample polygon with 6 sides (N=6) 
"""

def perimeter(listing):
    length=len(listing)
    perimeter=0;
    for i in range(0,length-1):
        dist=(((listing[i][0]-listing[i+1][0])**2)+((listing[i][1]-listing[i+1][1])**2)**0.5)
        perimeter=perimeter+dist
        perimeter=perimeter+(((listing[0][0]-listing[length-1][0])**2)+((listing[0][1]-listing[length-1][1])**2))**0.5
        return perimeter
L=[(1,3),(2,7),(3,9),(-1,8)]
print(perimeter(L))
print("=====================================================================================================")


"""Activity 5:
Imagine two sets A and B containing numbers. Without using built-in set functionalities, write your 
own function that receives two such sets and returns another set C which is a symmetric difference 
of the two input sets. (A symmetric difference between A and B will return a set C which contains 
only those items that appear in one of A or B. Any items that appear in both sets are not included in 
C). Now compare the output of your function with the following built-in functions/operators.
✓ A.symmetric_difference(B)
✓ B.symmetric_difference(A)
✓ A ^ B
✓ B ^ A  """

def symmdif(a,b):
    e=set()  #empty set
    for i in a:
        if i not in b:
            e.add(i)
    for i in b:
        if i not in a:
            e.add(i)
    return e
set1={0,1,2,3,4,5}
set2={4,5,7,8,9}
print(symmdif(set1,set2))
#verification
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))
print(set1^set2)
print(set2^set1)
print("=====================================================================================================")

"""Activity 6:
Create a Python program that contains a dictionary of names and phone numbers. Use a tuple of 
separate first and last name values for the key field. Initialize the dictionary with at least three 
names and numbers. Ask the user to search for a phone number by entering a first and last name. 
Display the matching number if found, or a message if not found.
Solution:    """

sample={("shoaib","ali"):"053454654",("hassan","khan"):"05876868554",("ahmad","bajwa"):"45346533454654",}
FName=input("Enter first name:")
LName=input("Enter Last name:")
searchTuple=(FName,LName)
if searchTuple in sample:
    print(sample[searchTuple])
else:
    print("Name not found..")
print("=====================================================================================================")













