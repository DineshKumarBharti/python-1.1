# OPPs  Concepts 
'''
class animal:
    def run(self,name):
        print("hello ...! :" ,name)
    def fast(self):
        print(" dinesh ")

dog=animal()
dog.run("dabar")          # funtion inside pass----  "dabar" 
                          # funtion is side use -------------- (self,name)
dog.fast()                # print in pass---------------------- ,name

cat=animal()
cat.run("hunny")
cat.fast() 

'''
# ------------------------------

'''
class animal:
    def run(self):
        print( self.color)
    def fast(self):
        print(" dinesh ")

# as a variable attributes pass----  "red" 
# print in pass side use -------------- (self.color)



dog=animal()
dog.color="red"
dog.run()
dog.fast()

cat=animal()
cat.color="blue"
cat.run()
cat.fast()

'''


'''

class animal:
    def run(self):
        print( self.color)
        self.name="animal"
    def fast(self):
        print(" dinesh ")
dog=animal()
dog.color="red"
dog.run()
dog.fast()
print(dog.name)

cat=animal()
cat.color="blue"
cat.run()
cat.fast()
print(cat.name)   # call outside the funtion


'''
'''
class Calculator:
    def add(self,a,b):
        self.c=a+b
        c=10
        print("the addition of :" ,self.c)
        print("c is value :",c)
    def display(self):
        print("the addition of :" ,self.c)

obj=Calculator()
obj.add(1000,20)

obj.display()
'''
'''
output

the addition of : 1020
c is value : 10
the addition of : 1020

'''
'''
'''
'''
class Calculator:
    x=0
    y=50  #obj.y
    z=70  #obj.z
    p=700
  
    def add(self,a,b):
        self.x=a+b
        print("the addition of :" ,self.x)
    def display(self):
        print("the addition of :" ,self.x)
        
        print("this is value of - ",self.y)
        print("this is value of - ",self.z)

obj=Calculator()
obj.add(1000,20)
obj.z=140
obj.display()
print("this is outside value :",obj.p)

output 
the addition of : 1020
the addition of : 1020
this is value of -  50
this is value of -  140
this is outside value : 700

'''

class Calculator:
    __a=20   # private __ double uderscope no access
    _b=500   # pubic   _ single underscope access anywhare
    c=200
    def add(self):
        # self.a=10
        print("this is a 1st add of",self._b )
    def run(self):
        print("this is a 2nd value",self.__a)
        print("this is a 3nd value",self._b)
        print("this is a 4nd value",self.c)

obj=Calculator()
obj.add()
obj.__a=100
obj.run()
print(obj._b)
print(obj.c)

# output :-
# this is a 1st add of 500
# this is a 2nd value 20
# this is a 3nd value 500
# this is a 4nd value 200
# 500
# 200