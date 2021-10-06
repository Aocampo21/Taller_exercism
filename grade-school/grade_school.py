from collections import defaultdict


class School:
    def __init__(self):
        self.students = defaultdict(list)

    def add_student(self, name, grade):
        self.students[grade].append(name)

    def roster(self):
        return [student
                for key in sorted(self.students.keys())
                for student in sorted(self.students[key])]

    def grade(self, grade_number):
        aux = self.students[grade_number]
        return sorted(aux)
