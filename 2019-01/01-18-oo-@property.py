# encoding = utf-8

'''

    今日练习：面向对象-类-装饰器函数，使用装饰器 @property 将方法变属性，配合 @x.setter 和 @x.deleter 实现将方法当作属性一样修改和删除，不必采取函数调用的方法，十分方便

    @property： 只读

    @property && @x.setter: 可读可写   x表示装饰器函数名

    @property && @x.setter && @x.deleter: 可读可写可删除  x表示装饰器函数名


'''

# todo 不使用装饰器函数封装学生类，实现对学生成绩的增删改查
class Student:

    def __init__(self,score):
        self.score = score

    def get_score(self):
        return self.score

    def set_score(self,value):
        self.score = value

    def delete_score(self):
        self.score = None

student = Student(100)
print(student.get_score())    # 100

student.set_score(60)
print(student.get_score())    # 60

student.delete_score()
print(student.get_score())     # None


# todo 使用装饰器函数封装学生类，采用属性操作方式实现对学生成绩的增删改查
class Student2:

    def __init__(self,score):
        self.score = score

    @property
    def grade(self):
        return self.score

    @grade.setter
    def grade(self, value):
        self.score = value

    @grade.deleter
    def grade(self):
        self.score = None

student2 = Student2(100)
print(student2.grade)       # 100

student2.grade = 90
print(student2.grade)       # 90

del student2.grade
print(student2.grade)      # None







