# Constructor
'''
class Employee:
    eid=0
    def getdetails(self):
        print("Id is :",self.eid)
        print("Name is :",self.ename)
        print( "Monthaly salary is:",self.esal)
ajay=Employee()
ajay.eid=1
ajay.ename="dk"
ajay.esal=25000
ajay.getdetails()


rakes=Employee()
rakes.eid=2
rakes.ename="skkkk"
rakes.esal=23000
rakes.getdetails()

# Id is : 1
# Name is : dk
# Monthaly salary is: 25000
# Id is : 2
# Name is : skkkk
# Monthaly salary is: 23000

'''
class Employee():
    def __init__(self):
        print("Constructor called.")
    def getdetails(self):
        print("ID:",self.eid)
        print("NAME:",self.ename)
        print("SALARY:",self.esal)

vijay=Employee()
vijay.eid=1
vijay.ename="sanjeet"
vijay.esal=30000
vijay.getdetails()


john=Employee()
john.eid=2
john.ename="jeet"
john.esal=40000
john.getdetails()

# ID: 1
# NAME: sanjeet
# SALARY: 30000
# Constructor called.
# ID: 2
# NAME: jeet
# SALARY: 40000

