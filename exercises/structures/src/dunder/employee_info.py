class EmployeeInfo(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address

# represents the string of object address
    def __str__(self):
        address = '(email address{}'.format(self.address)
        return'{}{}'.format(self.name, address)

# TODO - add dunder methods?
