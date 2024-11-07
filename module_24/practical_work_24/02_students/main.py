from stud_database import stud_base


class Student:
    average_rating = 0

    def __init__(self, info_lst):
        self.name_surname = info_lst[0]
        self.num_groupe = info_lst[1]
        self.evaluations_lst = info_lst[2]
        self.cal_average_score()

    def show_student(self):
        print('Имя студента: {}\nНомер группы: {}'.format(
            self.name_surname, self.num_groupe
        ))
        print('Успеваемость студента:', end=' ')
        for grade in self.evaluations_lst:
            print(grade, end=' ')
        print(f'\nСредняя оценка у {self.name_surname.split()[0]}: {self.average_rating}\n')

    def cal_average_score(self):
        for grade in self.evaluations_lst:
            self.average_rating += grade
        self.average_rating /= len(self.evaluations_lst)
        
        
class AllStudents:
    def __init__(self, in_dict):
        self.students = [
            Student([param for param in info.values()])
            for info in in_dict.values()
        ]
        
    def show_all_students(self):
        for student in self.students:
            student.show_student()
        print()

    def babble_sorting(self):
        len_lst = len(self.students)
        for i in range(len_lst):
            for j in range(0, len_lst-i-1):
                if self.students[j].average_rating < self.students[j+1].average_rating:
                    self.students[j], self.students[j+1] = self.students[j+1], self.students[j]

    def quick_sorting(self):
        self.students = self.start_quick_sort(self.students)

    def start_quick_sort(self, objects_lst):
        if len(objects_lst) < 1:
            return objects_lst

        sub_elem = objects_lst[len(objects_lst) - 1].average_rating

        min_lst = [obj for obj in objects_lst if sub_elem > obj.average_rating]
        max_lst = [obj for obj in objects_lst if sub_elem < obj.average_rating]
        equal_lst = [obj for obj in objects_lst if sub_elem == obj.average_rating]

        result_1 = self.start_quick_sort(min_lst)
        result_2 = self.start_quick_sort(max_lst)

        return  result_1 + equal_lst + result_2

    def ready_made_sorting(self):
        self.students = sorted(self.students, key=lambda student: student.average_rating)

groupe_1 = AllStudents(stud_base)

# Bubble sorting test
# groupe_1.show_all_students()
# groupe_1.babble_sorting()

# Quick sort operation test
# groupe_1.quick_sorting()
# groupe_1.show_all_students()

# Ready-made sort operation test
groupe_1.ready_made_sorting()
groupe_1.show_all_students()

# зачет!
