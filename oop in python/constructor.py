#Constructors in fython
class mclass:
   sut="ali"
   def __init__(self,name):
      print("this is first constructor or zero ")
      k=49
      s=44
      ds=k+s
      print(ds)
      print(name)
      self.ds=ds
      self.name=name
   def method1(self):
      print("method ",self.name)
obj=mclass("hasibullah")
obj.method1()

#second constructor a simple program in this constructur
class operation:
   def __init__(self,vall,vall1):
      print("Welcome to operation ")
      self.vall=vall
      self.vall1=vall1
   def add(self):
      print(" value1+value2 = ",self.vall+self.vall1)
   def mult(self):
      print(" value1*value2 = ", self.vall * self.vall1)

obj=operation(33,44);
obj.add()
obj.mult()
#Other constructor in python
class test:
   def __init__(self,name ,address,salary):
      self.name=name
      self.address=address
      self.salary=salary

   def desply1(self):
      print("name:{} address:{} salary:{}".format(self.name,self.address,self.salary) )
   def desply2(self):
      print(" Name%s address%s salary%g" % (self.name,self.address,self.salary))
   def __str__(self):
      print("program done successfully ")
obj=test("hasibullah","wardak",444444)
obj.desply1()
obj.desply2()
print(obj)

#del function in constructor by python
class test:
   def __init__(self):
      print("hay constructor ")
   def method1(self):
      print("hay function ")
   def __del__(self):
      print("hay del,destry object")
ob=test()

ob2=ob
ob3=ob
print(ob)
print(ob2)
print(ob3)
