class Student:
    name="abc"
    roll=111
    marks=85
    division="1st"
    def dis(self):
        print("Name:",Student.name)
        print("Roll:",Student.roll)
        print("Marks:",Student.marks)
        print("Division:",Student.division)
adam=Student()
adam.dis()