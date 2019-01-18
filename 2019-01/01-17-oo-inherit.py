# encoding: utf-8


'''

    本节练习：类的继承

    1. 子类没有定义自己的构造函数和方法，则完全继承父类构造函数和方法，实例化对象时必须按照父类构造器要求传参，否则会报错
    2. 子类定义了自己的构造函数，未显式继承父类构造函数，则子类构造函数覆盖父类，父类不可用，实例传参需根据子类构造函数传
    3. 使用super（）函数显式的继承父类的属性和方法，先继承再重构（重构的含义包括新建和覆盖）

'''


class Parent:

    total = 0
    def __init__(self, firstName, lastName):
        Parent.total += 1
        self.firstName = firstName
        self.lastName = lastName

    def fullName(self):

        return '{} {}'.format(self.firstName, self.lastName)


# todo 类的继承，子类没有定义自己的构造函数和方法，则完全继承父类构造函数和方法，实例化对象时必须按照父类构造器要求传参，否则会报错
class Child(Parent):
    pass

child = Child('hello','world')
print(child.fullName())   # hello world

# 未按照父类构造器传参，会报错
# child_01 = Child('hello')   # TypeError: __init__() missing 1 required positional argument: 'lastName'


# todo 类的继承，子类定义了自己的构造函数，未显式继承父类，则子类构造函数全覆盖父类，父类构造函数不可用，实例传参需根据子类构造函数传
class Child02(Parent):

    def __init__(self,firstName):
        self.firstName = firstName

#  报错，子类定义了自己的构造函数且未显示继承父类构造函数，父类构造函数不可用
# child02_01 = Child02('aa','bb')   #  TypeError: __init__() takes 2 positional arguments but 3 were given



# todo 类的继承，使用super（）函数显式的继承父类的属性和方法
class Child01(Parent):

    # 显式继承，先继承再重构（重构的含义包括新建和覆盖），继承父类first,last属性,fullName()方法，重构子类members属性和get_members()方法
    def __init__(self, first, last, members=None):
        super().__init__(first, last)
        if members == None:
            self.members = []
        else:
            self.members = members

    def get_members(self):
        arr = []
        for item in self.members:
            arr.append(item.fullName())
        return arr

person1 = Parent('bb','bb01')
person2 = Parent('cc','cc01')
child01_01 = Child01('aa','aa01', [person1,person2])

print(child01_01.get_members())   # ['bb bb01', 'cc cc01']
