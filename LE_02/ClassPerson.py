class Person:
    def __init__(self, name, age, pnum, email, address):
        self.__name = name
        self.__age = age
        self.__pnum = pnum
        self.__email = email
        self.__address = address

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_pnum(self):
        return self.__pnum

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

    def set_name(self, edit_value):
        self.__name = edit_value

    def set_age(self, edit_value):
        self.__age = edit_value

    def set_pnum(self, edit_value):
        self.__pnum = edit_value

    def set_email(self, edit_value):
        self.__email = edit_value

    def set_address(self, edit_value):
        self.__address = edit_value


class Customer(Person):
    def __init__(self, name, age, pnum, email, address, cid):
        Person.__init__(self, name, age, pnum, email, address)
        self.__cid = cid

    def get_cid(self):
        return self.__cid

    def set_id(self, edit_value):
        self.__cid = edit_value

    def to_dict(self):
        return {
                'name': self.get_name(),
                'age': self.get_age(),
                'pnum': self.get_pnum(),
                'email': self.get_email(),
                'address': self.get_address(),
                'cid': self.get_cid()
            }


class Employee(Person):
    def __init__(self, name, age, pnum, email, address, eid):
        Person.__init__(self, name, age, pnum, email, address)
        self.__eid = eid

    def get_eid(self):
        return self.__eid
        # Nice

    def set_id(self, edit_value):
        self.__eid = edit_value

    def to_dict(self):
        return {
                'name': self.get_name(),
                'age': self.get_age(),
                'pnum': self.get_pnum(),
                'email': self.get_email(),
                'address': self.get_address(),
                'eid': self.get_eid()
            }
