#a =5
def F1():
    print("Inside some_func")
    def F2():
        a=5
        print("Inside inner function, value of var:",a)
    F2()
    #print("Try printing var from outer function: ",a)
F1()

""" a =10
def F1():
    print("Inside some_func")
    def F2():
        global a
        print("Inside inner function, value of var:",a)
    F2()
    print("Try printing var from outer function: ",a)
F1() """