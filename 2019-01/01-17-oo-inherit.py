# encoding: utf-8


'''

    本节练习：类的继承
    https://blog.csdn.net/brucewong0516/article/details/79121179

'''


class Group:

    total = 0
    def __init__(self, firstName, lastName, sex):

        Group.total += 1
        self.firstName = firstName
        self.lastName = lastName
        self.sex = sex

    def fullName(self):

        return '{} {}'.format(self.firstName, self.lastName)


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