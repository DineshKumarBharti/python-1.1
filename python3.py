# Constructor

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