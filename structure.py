from fastapi import FastAPI

app = FastAPI()


class Member:
    def __init__(self, id, firstname, lastname, M_name, email, phone_number, person_id, college_id, major, address):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.M_name = M_name
        self.email = email
        self.phone_number = phone_number
        self.person_id = person_id
        self.college_id = college_id
        self.major = major
        self.address = address

    def Outputvals(self):
        vals = (
            self.id, self.firstname, self.lastname, self.M_name, self.email, self.phone_number, self.person_id,
            self.college_id, self.major, self.address)
        return vals


class College:
    def __init__(self, id, name, address, website):
        self.id = id
        self.name = name
        self.address = address
        self.website = website

    def Outputvals(self):
        vals = (
            self.id, self.name, self.address, self.website)
        return vals

class Person:
    def __init__(self, id, joined_date, position):
        self.id = id
        self.joined_date = joined_date
        self.position = position

    def Outputvals(self):
        vals = (
            self.id, self.joined_date, self.position)
        return vals

@app.get("/")
def welcome():
    return {'message': "Welcome to SEDS API"}


@app.get("/api/members")
def members():
    member = Member(1, "John", "Locker", "Vincent", "john@example.com",
                    9878906752, 1,
                    1, "Mathematics", "KTM")
    return member


@app.get("/api/colleges")
def colleges():
    college = College(1,"St. Lawrence", "KTM", "stlawrence.edu.np")
    return college


@app.get("/api/person")
def person():
    personnel = Person(1,"12/12/20","member")
    return personnel
