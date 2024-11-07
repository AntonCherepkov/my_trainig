class MyStack:
    def __init__(self):
        self.my_stack = []

    def add_elem(self, element):
        new_tuple = (element)
        self.my_stack.append(new_tuple)

    def empty(self):
        if self.my_stack:
            return True
        return False

    def get(self):
        if self.empty():
            del_elem = self.my_stack.pop()
            return del_elem
