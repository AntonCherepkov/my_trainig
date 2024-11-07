from manager import TaskManager

manager = TaskManager()
manager.new_task('помыть посуду', 1)
manager.new_task('прибраться в комнате', 5)
manager.new_task('почистить зубы', 4)
manager.new_task('сделать уроки', 2)

print(manager)

deleted_task = 'почистить зубы'
print(f'Удаляем задачу: {deleted_task}')
manager.del_task(deleted_task)

print(manager)
