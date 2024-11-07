from stack import MyStack

class TaskManager:
    def __init__(self):
        self.user_stack = MyStack()

    def new_task(self, task, priority=0):
        self.user_stack.add_elem(element=(task, priority))

    def del_task(self, task):
        save_list = []
        del_task = None

        while self.user_stack.empty():
            current_elem = self.user_stack.get()
            if current_elem[0] != task:
                save_list.append(current_elem)
            else:
                del_task = current_elem[0]
        else:
            if del_task:
                print(f'Удалена задача: {del_task}')

        for elem in save_list[::-1]:
            self.user_stack.add_elem(elem)

    def __str__(self):
        result = ''
        if self.user_stack.empty():
            sort_tasks = sorted(self.user_stack.my_stack, key=lambda x: x[1])
            for task, priority in sort_tasks:
                result += ' '.join([str(priority), task, '\n'])
            return result
        else:
            return None
