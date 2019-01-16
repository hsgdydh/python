# encoding: utf-8


class Group:
    total = 0
    belone = 1

    # todo 构造器，每次生成实例都会调用
    def __init__(self, firstName, lastName, sex):

        # todo 在构造器中修改类成员变量的值，计数实例化多少个对象
        Group.total += 1

        self.firstName = firstName
        self.lastName = lastName
        self.sex = sex

    def fullName(self):

        return '{} {}'.format(self.firstName, self.lastName)

    def group_belone(self):

        return self.belone

    @classmethod
    def set_member_from_str(cls, str):

        (firstName, lastName, sex) = str.split('-')
        return cls(firstName, lastName, sex)

    # todo 类方法，实例和类都可以访问，若去掉@classmethod装饰器则为实例方法，类调用会报错
    @classmethod
    def members_total(self):

        return self.total

    # todo 静态方法，实例和类都可以访问，无需传self或者cls
    @staticmethod
    def is_weekday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        else:
            return True


member_01 = Group('张', '三', '男')

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
        for item in self.members:
            return item.fullName

sub_Group_01 = sub_Group('aa','aa01','男')
print(sub_Group_01.fullName())

person1 = Group('bb','bb01','女')
person2 = Group('cc','cc01','男')
sub_Group_02 = sub_Group('aa','aa01','男',[person1,person2])
print(sub_Group_02.get_members())