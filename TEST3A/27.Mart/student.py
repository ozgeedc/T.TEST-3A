

class Student:

    student_list = []

    def add(self, first_name, last_name, gender, number):
        for std in self.student_list:
            if std["number"] == number:
                std["name"] = first_name + " " + last_name
                std["gender"] = gender
                print(f"{std['name']} updated successfully.")
                return

        name = first_name + " " + last_name
        student_info = {
            "name": name,
            "gender": gender,
            "number": number
        }
        self.student_list.append(student_info)
        print(f"{name} added successfully.")

    def remove(self, number):
        for index, std in enumerate(self.student_list):
            if std["number"] == number:
                removed = self.student_list.pop(index)
                print(f"Removed: {removed['name']}")
                break

    def list(self, student_list):
        if not student_list:
            print(f"No students registered yet.")
            return
        print(f"{'Name':<18}{'Gender':<9}{'Number':<10}")
        for student in student_list:
            print(f"{student['name'][:15]:<16}| {student['gender'][:5]:<7}| {student['number']:<10}")