class Node:
    def __init__(self, nextNode, prevNode, data):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode


class LinkedList:
    def __init__(self):
        self.head = None


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active


db = LinkedList()


def init(cars):
    for car in cars:
        add(car)


def add(car):
    new = Node(None, None, car)
    foo = db.head
    if foo is None:
        db.head = new
    elif car.price < foo.data.price:
        new.nextNode = db.head
        db.head = new
        new.nextNode.prevNode = new
    else:
        # vkládám ZA foo
        while (foo.nextNode is not None) and (foo.nextNode.data.price <= car.price):
            foo = foo.nextNode
        new.nextNode = foo.nextNode
        foo.nextNode = new
        new.prevNode = foo
        if foo.nextNode is None:
            new.nextNode.prevNode = new


def updateName(identification, name):
    foo = db.head
    while (foo is not None) and (identification != foo.data.identification):
        foo = foo.nextNode
    if foo is not None:
        foo.data.name = name


def updateBrand(identification, brand):
    foo = db.head
    while (foo is not None) and (identification != foo.data.identification):
        foo = foo.nextNode
    if foo is not None:
        foo.data.brand = brand


def activateCar(identification):
    foo = db.head
    while (foo is not None) and (identification != foo.data.identification):
        foo = foo.nextNode
    if foo is not None:
        foo.data.active = True


def deactivateCar(identification):
    foo = db.head
    while (foo is not None) and (identification != foo.data.identification):
        foo = foo.nextNode
    if foo is not None:
        foo.data.active = False


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    foo = db.head
    price = 0
    while foo is not None:
        if foo.data.active:
            price += foo.data.price
        foo = foo.nextNode
    return price


def clean():
    db.head = None


def printDatabase():
    foo = db.head
    while foo is not None:
        print(str(foo.data.identification) + " " + foo.data.name + " " + foo.data.brand + " " + str(foo.data.price) + " " + str(foo.data.active))
        foo = foo.nextNode


# add(Car(1, 'Model S', 'Tesla', 1500, True))
# add(Car(5, 'Superb', 'Škoda', 1200, True))
# add(Car(3, 'ZR1', 'Corvette', 2300, True))
#
# printDatabase()
