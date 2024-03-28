

class Teacher:
    
    teacher_list = []

    def add(self, first_name, last_name, gender, branch):
            name = first_name + " " + last_name
            teacher_info = {
                "name": name,
                "gender": gender,
                "branch": branch
            }
            self.teacher_list.append(teacher_info)
            print(f"{name} added successfully.")

    def remove(self, name):
        for index, std in enumerate(self.teacher_list):
            if std["name"] == name:
                removed = self.teacher_list.pop(index)
                print(f"Removed: {removed['name']}")
                break

    def list(self, teacher_list):
        if not teacher_list:
            print(f"No teachers registered yet.")
            return
        print(f"{'Name':<18}{'Gender':<9}{'Branch':<10}")
        for teacher in teacher_list:
            print(f"{teacher['name'][:15]:<16}| {teacher['gender'][:5]:<7}| {teacher['branch']:<10}")