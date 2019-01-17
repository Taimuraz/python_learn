class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)

    def __str__(self):
        return '[Manager: %s, %s]' % (self.name, self.pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)



if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='developer', pay=100000)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    bob.giveRaise(0.5)
    sue.giveRaise(0.5)

    dep = Department(bob, sue, tom)
    dep.giveRaises(.20)
    dep.showAll()

