# encoding: utf-8

'''

    本节练习：面向对象基础

            类的创建
            类的实例化
            类成员：成员变量、成员方法（类方法、实例方法、静态方法）

            1. 构造器，每次生成实例都会调用。
            2. 类变量，类和实例都可以访问和修改，使用类修改则以该类为基类的所有实例都相应改变，若使用实例修改，则仅对于当前实例修改。
            3. 实例变量，仅实例可访问
            2. 实例方法，必须以self作为第一个参数，指向实例出来的对象，类调用报错，仅能实例调用。
            3. 类方法，采用 @classmethod 装饰器，以 cls 作为第一个参数，实例和类都可以访问，类调用会报错。
            4. 静态方法，采用 @staticmethod 装饰器，无需传self或者cls，实例和类都可以访问。

'''



class Group:

    # 类变量
    total = 0
    belone = 1

    # todo 构造器，每次生成实例都会调用
    def __init__(self, firstName, lastName, sex):   # 实例变量

        # todo 在构造器中修改类成员变量的值，计数实例化多少个对象
        Group.total += 1

        self.firstName = firstName
        self.lastName = lastName
        self.sex = sex

    # todo 实例方法，必须以self作为第一个参数，指向实例出来的对象，类调用报错，仅能实例调用。
    def fullName(self):

        return '{} {}'.format(self.firstName, self.lastName)

    def group_belone(self):

        return self.belone

    @classmethod
    def set_member_from_str(cls, str):

        (firstName, lastName, sex) = str.split('-')
        return cls(firstName, lastName, sex)

    # todo 类方法，实例和类都可以访问，cls作为第一个参数
    @classmethod
    def members_total(cls):

        return cls.total

    # todo 静态方法，实例和类都可以访问，无需传self或者cls
    @staticmethod
    def is_weekday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        else:
            return True

# todo 实例化对象
member_01 = Group('张', '三', '男')

# print(Group.firstName)   # 报错，实例变量只能实例访问
print(Group.members_total())  # 1   total为类成员变量，类和实例都可以访问，在构造器中设置计数，每实例化一个对象计数+1

member_02 = Group('李', '四', '女')

print(member_01.fullName())  # 张 三
print(member_02.fullName())  # 李 四
print(member_01.group_belone())  # 1
print(member_02.group_belone())  # 1
print(Group.members_total())  # 2

# todo 类成员变量类和实例都可以访问和修改，使用类修改则以该类为基类的所有实例都相应改变，若使用实例修改，则仅对于当前实例修改。
# 类变量belone值为1，实例member_02修改其值为2，实例member_01依然沿用类中的默认值1
member_02.belone = 2
print(member_01.group_belone())  # 1
print(member_02.group_belone())  # 2   belone为类成员变量，类和实例都可以访问

member_03 = Group('', '', '').set_member_from_str('王-五-男')
print(dir(member_03))
print(member_03.fullName())
print(member_03.sex)

# todo datetime是python处理的日期的模块之一，datetime(year,month,day).weekday()返回int类型数据，表示一周中的第几天，0表示周一，依次类推
import datetime

day1 = datetime.datetime(2019, 1, 13)  # 周日
day2 = datetime.datetime(2019, 1, 14)  # 周一

print(Group.is_weekday(day1))  # False
print(Group.is_weekday(day2))  # True


# todo 类的继承
class sub_Group(Group):

    def __init__(self, first, last, sex, members=None):
        super().__init__(first, last, sex)
        if members == None:
            self.members = []
        else:
            self.members = members

    def get_members(self):
        arr = []
        for item in self.members:
            arr.append(item.fullName())
        return arr

person1 = Group('bb','bb01','女')
person2 = Group('cc','cc01','男')
sub_Group_02 = sub_Group('aa','aa01','男',[person1,person2])

print(sub_Group_02.get_members())   # ['bb bb01', 'cc cc01']