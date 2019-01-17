class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
        print("giveRaise from Developer.")

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)

    def __str__(self):
        return '[Manager: %s, %s]' % (self.name, self.pay)

    def giveRaise(self, percent, bonus=.10):
        print("giveRaise from Manager.")
        Person.giveRaise(self, percent + bonus)

    def __getattr__(self, item):
        print("No such attribute.")


class Department:
    def __init__(self, *args):
        self.members = list(args)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='developer', pay=100000)

    bob.giveRaise(0.5)
    sue.giveRaise(0.5)

    print(bob)
    print(sue)

    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)

    print("--All three--")
    for object in (bob, sue, tom):
        object.giveRaise(.10)
        print(object)


