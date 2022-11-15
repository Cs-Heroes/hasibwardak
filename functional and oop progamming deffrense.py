#functional programming in python
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def do_math(action,a,b):
    return action(a,b)

print(add(44,5))
print(mul(4,5))
print(do_math(add,44,5))
my_list=[1,2,3,4]
double_list=[2*val for val in my_list]
print(my_list)
print(double_list)
#Object oreinted programming
class do_math:
    def __init__(self,val1,val2):
         self.val1=val1
         self.val2=val2
    def add(self):
        return self.val1+self.val2
    def mul(self):
        return self.val1*self.val2
    def double_input(self):
        self.val1*=2
        self.val2*=2
math=do_math(4,4)
print(math.add())
print(math.mul())
print(math.double_input())
print(math.add())