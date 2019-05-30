"""
Data Types in Python :

Name:               Type:         About:                                        Examples:
Integer             int            Whole numbers                                   1,2,100
Floating point      float          Decimal numbers                                 1.23, 333.33
String              str            Ordered collection of characters                "ONE" "123" "@@"
list                list           Ordered collection of objects                   [1,"one","@"]
Tuples              tup            Ordered collection of modifiable objects        (1,"one","@")
Sets                set            Unordered collection of unique objects          {"1,"one"}
Dictionary          dict           Unordered (key : value) pair                    {"key":"value","Name":"Raviraj"}
Boolean             bool           logical True & False                            True or False

"""

userdata = {}
amount= 1000
am= int(input())
userdata["Amount"] = amount
userdata["Amount"]=userdata["Amount"] -am

print(userdata["Amount"])
print((2+3)+(4*5))

#Print_formatting:
x="string1:{} sting2:{}  sting3:{}".format("cat","df","23")
print(x)

String = 'ABC'
print(String[-1])

#Slicing:
print(String[::2])
String[0]='X' #Erroor
x= String.upper()
x= String.lower()
x= String.capitalize()
x= String.split()




