class Member:
    def __init__(self, new_gender, new_major, new_id):
        self.__gender = new_gender  # __gender對外不公開
        self.major = new_major
        self.id = new_id

    def get_gender(self):
        return self.__gender

    def set_gender(self, new_gender):
        if new_gender == 'M' or new_gender == 'F':
            self.__gender = new_gender
        else:
            print('=========')

    def borrow_resources(self):
        pass

    def check_auth(self):
        pass


class Student(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)


    def borrow_resources(self):
        print('student borrow')

    def join_class(self):
        pass

    def quit_class(self):
        pass


class professor(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def borrow_resources(self):
        print('professor borrow')


studentA = Student('M', '工管系', 'M10721223')
studentB = Student('F', '經濟系', 'M107212239')
professorA = professor('M', '工系', 'M10721255')
professorB = professor('M', '工系', 'M10721258')
ls = [studentA, studentB, professorA, professorB]
for item in ls:
