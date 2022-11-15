from threading import*
# def show():
#     print("this is a child threed")
# t=Thread(target=show())
# t.start()
# print("this is parent class")
# class myclass(Thread):
#     def run(self):
#         for i in range(5):
#             print("This is a child class ")
# t=myclass()
# t.start()
# for i in range(5):
#     print("this is the main threed")
#
# class demo:
#     def show(self):
#         for i in range(5):
#             print("this is the child class")
#
# ob=demo()
# t=Thread(target=ob.show())
# t.start()
# for i in range(5):
#     print("this is the parent class")
import time
class demo:
    def run(self):
        for i in range(1,5):
            print("the number is  ",i)
            time.sleep(1)
    def double(self):
       for i in range(1, 5):
           print("the double of the number ",2*i)
           time.sleep(1)

    def squre(self):
       for i in range(1, 5):
          print("the squre of the number ", i*i)
          time.sleep(1)
obj=demo()
t=Thread(target=obj.run())
t1=Thread(target=obj.double())
t2=Thread(target=obj.squre())
t.start()
time.sleep(0.2)
t1.start()
time.sleep(0.2)
t2.start()
t.join()
t1.join()
t2.join()

print("This is the main Threed ")

