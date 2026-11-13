class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality
    def print(self):
        print(f"{self.name} {self.family} is {self.nationality}")

class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy
    def print(self):
        print(f"{self.name} {self.family} is {self.nationality}. They study at {self.university}. Year of study: {self.yearofstudy} year(s).")

class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience
    def print(self):
        print(f"{self.name} {self.family} is {self.nationality}. They work at {self.university}. Years of experience: {self.experience} year(s).")

person1 = Person("Mariyan", "Savov", 19, "Bulgarian")
person2 = Person("Ivaylo", "Andonov", 19, "Italian")
person1.print()
person2.print()

student1 = Student("Mariyan", "Savov", 19, "Bulgarian", "TU-Sofia", 1)
student2 = Student("Ivaylo", "Andonov", 19, "Italian", "SU", 3)
student1.print()
student2.print()

lecturer1 = Lecturer("Mariyan", "Savov", 19, "Bulgarian", "TU-Sofia", 10)
lecturer2 = Lecturer("Ivaylo", "Andonov", 19, "Italian", "SU", 13)
lecturer1.print()
lecturer2.print()