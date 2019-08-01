import datetime


class Person(object):

    def __init__(self, name):
        """创建一个人"""
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        """返回self的全名"""
        return self.name

    def getLastName(self):
        """返回self的姓"""
        return self.lastName

    def setBirthday(self, birthday):
        """"""
        self.birthday = birthday

    def getAge(self):
        """返回self的当前年龄，用日表示"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """"""
        if self.lastName == other.lastName:
            return self.name < other.lastName
        return self.lastName < other.lastName

    def __str__(self):
        return self.name


class MITPerson(Person):

    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other):
        return self.idNum < other.idNum


class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year


class Grad(Student):
    pass


###########################  RUN  ###########################
me = Person('Fei Zhang')
g1 = Person('BB Fang')
g2 = Person('Lili Wang')

mit1 = MITPerson('Eric Cartman')
mit2 = MITPerson('Jim Green')
mit3 = MITPerson('Super Man')
mit4 = MITPerson('Super Man')
print(mit3 > mit4)

# print(me.getLastName())
# me.setBirthday(datetime.date(1982, 3, 8))
# print(me.getName(), 'is', me.getAge(), 'days old')

# pList = [me, g1, g2]
# for p in pList:
#     print(p)
# pList.sort()
# for p in pList:
#     print(p)
