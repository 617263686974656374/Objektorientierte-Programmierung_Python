from ClassManage import *


def add_employee(mp):
    name = input("Enter name: ")
    age = input("Enter age: ")
    pnum = input("Enter phone number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    eid = input("Enter Employee ID: ")
    mp.add_people(Employee(name, age, pnum, email, address, eid))


def add_customer(mp):
    name = input("Enter name: ")
    age = input("Enter age: ")
    pnum = input("Enter phone number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    cid = input("Enter Customer ID: ")
    mp.add_people(Customer(name, age, pnum, email, address, cid))
