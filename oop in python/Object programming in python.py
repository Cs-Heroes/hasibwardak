class myclass():
    def method1(self):
        print("first function")
    def method2(self):
        print("second method in this class")
obj=myclass();
obj.method1()
obj.method2()
class mclass2():
    def mothod2(self,name):
        print("This is your name ",name)
obj1=mclass2();
obj1.mothod2('hasibullah')

#instant and static method in the class
class mclass():
    def method(self,name,address):
        print("class instance methods ")
        print("name : ",name," address ; ",address)
    @staticmethod
    def method2(id,stdname):
        print("static method ")
        print("id : ",id," student name  ",stdname)
mclass.method2(22,"wardak")
obj=mclass();
obj.method("hasibyullah","kabul")

print("rest of my code  ")
#local , global varible in python
name="hasibullah"
address="wardak"
class mclass():
    a=90
    b=20
    def method1(self):
        x=30
        y=20
        print("method varible : x+y  =",x+y)
        print("local class varible in method 1 : a+b = ",self.a+self.b)
        print("Global varible in method 1  ",name,address)
    def method2(self,z,i):#passed varible to this function
        print("method varible : z+i =",z+i)
        print("local class varible in method 2 : a+b = ", self.a + self.b)
        print("Global varible in method 2  ", name, address)
obj=mclass();
obj.method1()
obj.method2(20,44)

class mclass2():
    def method3(self):
        print("global varible in class2 method 3 : name & address  ",name,address)
obj2=mclass2();
obj2.method3()
name="hasib"   #Global varible
address="wardak"
class mclass1():
    name="bilal"   #local varible
    address="kabul"
    def show_all(self,name,address):
        print("local method varible " ,name," : ",address)
        print("local class varible " ,self.name,self.address)
        print("local global varible " ,globals() ['name'],globals() ['address'])

obj=mclass1();
obj.show_all("ahmad","ningarhar")

#Object creation
class mclass():
    name="hasibullah"
    address="wardak"
    def method(self,salary):
        print("name : ",self.name)
        print("address : ",self.address)
        print("salary : ",salary)
#named object
obj=mclass();
obj.method(30000)
obj.name="ahmad"
obj.address="ningarhar"
obj.method(6000)
#name less object
mclass().method(40000)
#Conversion varible one to another
class Test():
    Tax=10
    def getdata(self,name,salary):
        print("name : ",name,"salary : ",salary)
        self.salary=salary
        self.name=name
        self.desplayrecordinoneline()
    def showtax(self):
        print("Tax = ",self.Tax)
        print("payable ",self.Tax- self.salary)
    def desplayrecordinoneline(self):
        print("name ",self.name," salary ",self.salary," tax ",self.Tax," payble ",self.salary-self.Tax)
obj=Test();
nam=input("Enter your name ")
sal=int(input("Enter your salary"))
obj.getdata(nam,sal)