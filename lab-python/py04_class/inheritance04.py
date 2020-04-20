class Person:
    pass


class BusinessPerson(Person):
    pass


if __name__ == '__main__':
    oh_ssam = Person()
    print(isinstance(oh_ssam, Person))
    print(isinstance(oh_ssam, BusinessPerson))

    gildong = BusinessPerson()
    print(isinstance(gildong, BusinessPerson))
    print(isinstance(gildong, Person))

