#inheratince in python
class test1:
   def __init__(self):
      print("constructor test1")
   def method1(self):
      print("method 1")
class test2(test1):
   def __init__(self):
      print("constructor test2")
   def method2(self):
      print("method 2 ")

obj2=test2()
obj2.method2()
obj2.method1()
#other inheratince in python deffrence type of varible
d,e=48,44
class parent:
   x,y=29,49
class child(parent):
   z,w=3,4
   def add(self,a,b):
      print("a+b ",a+b)
      print("z+w",self.z+self.w)
      print("parent class varible  ",super().x,super().y)
      print("globle barible ",globals() ['d'],globals() ['e'])
w,h=33,55
class A:
   w,h=66,88
class B(A):
   w,h
   def __init__(self,w,h):
      self.w=w
      self.h=h
   def gerarea(self,w,h):
      return w*h
   def getarea(self):
      return self.w*self.h;
   def getarea2(self):
      return super().h*super().w;
obj=B(33,66);
print(obj.gerarea(4,5))
print(obj.getarea())
print(obj.getarea2())
obj=child()
obj.add(44,55)
class parent:
   salary=0
   def __init__(self,x):
      self.salary=x
      print("parent class constructor")
   def method2(self):
      print("Hay method of parent class,salary = ",self.salary)

class child(parent):
   def __init__(self):
      super().__init__(49999)

      print("child class constructor ")
   def method(self):
      print("method of child")
      super().method2()

obj=child()
obj.method()
#multiple inheratance in python
class box:
   width,height=0,0

class two(box):
   color='green'
   def __init__(self,width,height,color):
      self.width=width
      self.height=height
      self.color=color
   def displaybox(self):
       print("box width  ",self.width)
       print("box height  ", self.height)
       print("box coloe ", self.color)
       print("box area ",self.width*self.height)


class threed(two):
   zAxis=0
   def __init__(self,w,h,z):
      self.width=w
      self.height=h
      self.zAxis=z
   def displaybox(self):
       print("box width  ",self.width)
       print("box height  ", self.height)
       print("box coloe ", self.color)
       print("zAxis ",self.zAxis)
       print("box area ",self.width*self.height*self.zAxis)

bo=two(3,5,"greeee")
bo.displaybox()
print("000000000000000000000000000")
obj=threed(44,44,5)
obj.displaybox()

